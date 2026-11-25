
from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from app.core.config import settings


# ==========================================
# 1. Password Hashing
# ==========================================

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Generate a secure password hash."""
    return password_hash.hash(password)


# ==========================================
# 2. Password Verification
# ==========================================

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """Verify a password against its stored hash."""
    return password_hash.verify(
        plain_password,
        hashed_password
    )


# ==========================================
# 3. JWT Access Token Generation
# ==========================================

def create_access_token(data: dict) -> str:
    """Generate a signed JWT access token."""

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


# ==========================================
# 4. JWT Access Token Verification
# ==========================================

def decode_access_token(token: str) -> dict | None:
    """Decode and verify a JWT access token."""

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except InvalidTokenError:
        return None

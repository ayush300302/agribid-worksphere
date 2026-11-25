

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.role import Role
from app.schemas.auth import UserRegister, UserLogin
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def register_user(db: Session, user_data: UserRegister) -> User:
    existing_user = db.scalar(
        select(User).where(User.email == str(user_data.email))
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered"
        )

    developer_role = db.scalar(
        select(Role).where(Role.name == "Developer")
    )

    if developer_role is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Default Developer role is not configured"
        )

    hashed_password = hash_password(user_data.password)

    new_user = User(
        full_name=user_data.full_name,
        email=str(user_data.email),
        hashed_password=hashed_password,
        role_id=developer_role.id,
        is_active=True
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, user_data: UserLogin) -> dict:
    # 1. Find user by email
    user = db.scalar(
        select(User).where(User.email == str(user_data.email))
    )

    # 2. Verify password
    if user is None or not verify_password(
        user_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # 3. Check whether account is active
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive"
        )

    # 4. Generate JWT access token
    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    # 5. Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

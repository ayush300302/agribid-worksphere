
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth import (
    UserRegister,
    UserResponse,
    UserLogin,
    TokenResponse,
)

from app.services.auth import (
    register_user,
    login_user,
)

from app.api.dependencies import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# User Registration
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db, user_data)


# User Login
@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user_data)


# Get Current Authenticated User
@router.get(
    "/me",
    response_model=UserResponse
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user

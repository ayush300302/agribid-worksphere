
from pydantic import BaseModel, EmailStr, Field


# Registration request
class UserRegister(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=150
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128
    )


# Login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# User response
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }


# JWT token response
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

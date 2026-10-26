from pydantic import BaseModel,ConfigDict,EmailStr,Field

from datetime import datetime
import uuid

from app.db.models.users import UserRole


class LoginRequest(BaseModel):
    "Credential submitted during login"

    institution_code:str = Field(min_length=1,max_length=50,)
    email:EmailStr
    password:str = Field(min_length= 6,max_length= 50)


class UserResponse(BaseModel):
    """Public information about an authenticated user"""

    id: uuid.UUID
    institution_id:uuid.UUID
    full_name:str
    email:EmailStr
    role:UserRole
    is_active:bool

    model_config =ConfigDict(from_attributes=True)

class LoginResponse(BaseModel):
    "Succesfull Login response"
    access_token:str
    token_type:str = "bearer"
    expires_in :int
    user: UserResponse

class RefreshTokenResponse(BaseModel):
    "Response after successfully renewing tokens."

    access_token:str
    refresh_token:str
    token_type:str = "bearer"
    expire_in :int

class LogoutResponse(BaseModel):
    """Logout Result"""

    message: str = "Successfully Logged out"

class ErrorResponse(BaseModel):
    """Generic error response"""

    deatails:str

    
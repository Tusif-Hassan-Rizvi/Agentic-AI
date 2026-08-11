from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


# 1. User Registration Schema
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    mobile_number: Optional[str] = None


# 2. User Login Schema (Accepts JSON body: {"username": "...", "password": "..."})
class UserLogin(BaseModel):
    username: str
    password: str


# 3. User Response Schema (Returns safe user info - NO PASSWORD)
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: Optional[str] = None
    mobile_number: Optional[str] = None
    is_active: bool
    created_at: datetime


# 4. Token Response Schema
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# 5. Token Data Schema
class TokenData(BaseModel):
    username: Optional[str] = None
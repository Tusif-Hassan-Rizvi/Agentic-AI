from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr



# 1. Registration Schema (Data sent by client during sign up)
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None
    mobile_number: Optional[str] = None


# 2. User Response Schema (Data returned by API - NO PASSWORD!)
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: Optional[str] = None
    mobile_number: Optional[str] = None
    is_active: bool
    created_at: datetime



# 3. Token Response Schema (Returned after successful login)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# 4. Token Data Schema (Decoded data stored inside JWT)
class TokenData(BaseModel):
    username: Optional[str] = None    


import re
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse, Token
from app.utils.security import hash_password, verify_password, create_access_token
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


# 1. Register User Endpoint
@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # 1. Validate Username
    if not user_data.username or not user_data.username.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username is required")
        
    if len(user_data.username.strip()) < 3:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username must be at least 3 characters")

    # 2. Validate Password
    if not user_data.password or not user_data.password.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password is required")

    if len(user_data.password) < 6:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be at least 6 characters long")

    # 3. Clean and Validate Email Format (Optional)
    clean_email = user_data.email.strip() if user_data.email and user_data.email.strip() else None
    if clean_email:
        if not re.match(EMAIL_REGEX, clean_email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Please enter a valid email address")

    # 4. Check if Username already exists in Database
    existing_username = db.query(User).filter(User.username == user_data.username.strip()).first()
    if existing_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    # 5. Check if Email already exists in Database
    if clean_email:
        existing_email = db.query(User).filter(User.email == clean_email).first()
        if existing_email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Save User to PostgreSQL
    hashed_pwd = hash_password(user_data.password)
    new_user = User(
        username=user_data.username.strip(),
        hashed_password=hashed_pwd,
        email=clean_email,
        mobile_number=user_data.mobile_number
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 2. Login Endpoint (Supports standard JSON body: {"username": "...", "password": "..."})
@router.post("/login", response_model=Token)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    if not credentials.username or not credentials.username.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username is required")

    if not credentials.password or not credentials.password.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password is required")

    user = db.query(User).filter(User.username == credentials.username.strip()).first()
    
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Create signed JWT Token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


# 3. Get Current User Profile (Protected Route)
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
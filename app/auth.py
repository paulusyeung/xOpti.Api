# app/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer  # Switch to HTTPBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from .database import get_db
from .models import Staff
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from passlib.context import CryptContext

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

bearer_scheme = HTTPBearer()  # Replace OAuth2PasswordBearer

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except ValueError:
        return plain_password == hashed_password

def get_password_hash(password):
    return pwd_context.hash(password)

async def get_current_user(token: str = Depends(bearer_scheme), db: Session = Depends(get_db)):
    print ("\nToken: ", token, "\n")
    from .users import crud  # Move import here to avoid circular dependency
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # HTTPBearer returns HTTPAuthorizationCredentials, use .credentials
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        staff_code: str = payload.get("sub")
        # print ("staff_code: ", staff_code, "\nEmail: ", email, "\nusername: ", username)
        if email is None and staff_code is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        user = crud.get_user_by_staff_code(db, staff_code=staff_code)
    if user is None:
        raise credentials_exception
    return user
# app/users/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..auth import create_access_token, verify_password, get_current_user
from . import schemas, crud
from app.models import Staff

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

''' # Commented out to avoid registering new users
@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_staff_code(db, staff_code=user.StaffCode)
    if db_user:
        raise HTTPException(status_code=400, detail="StaffCode already registered")
    return crud.create_user(db=db, user=user)'
'''

@router.post("/token")
def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.get_user_by_staff_code(db, staff_code=form_data.StaffCode)
    if not user:
        user = crud.get_user_by_username(db, username=form_data.Username)
    if not user or not verify_password(form_data.Password, user.Password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect StaffCode or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.StaffCode})  # Use StaffCode as JWT subject
    return {"access_token": access_token, "token_type": "bearer"}
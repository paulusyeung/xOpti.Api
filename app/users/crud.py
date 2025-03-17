# app/users/crud.py
from sqlalchemy.orm import Session
from app.models import Staff  # Use Staff model
from . import schemas
from ..auth import get_password_hash

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.Password)  # Hash the password
    db_user = Staff(StaffCode=user.StaffCode, Password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_staff_code(db: Session, staff_code: str):
    return db.query(Staff).filter(Staff.StaffCode == staff_code).first()

def get_user_by_email(db: Session, email: str):
    return db.query(Staff).filter(Staff.StaffCode == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(Staff).filter(Staff.StaffCode == username).first()
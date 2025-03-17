# app/users/schemas.py
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import Optional

class UserBase(BaseModel):
    StaffCode: str | None

class UserCreate(UserBase):
    Password: str  # Raw password input

class UserLogin(UserBase):
    Password: str

class User(UserBase):
    StaffFirstName: str | None
    StaffLastName: str | None
    JobTitle_: str | None
    JobStatus_: str | None
    SecurityLevel: int | None
    DateHired: datetime | None

    class Config:
        orm_mode = True
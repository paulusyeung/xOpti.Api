# app/cities/schemas.py
from pydantic import BaseModel
from typing import Optional

class CityBase(BaseModel):
    CityPhoneCode: Optional[str] = None
    CityName: str
    ProvinceCode: str
    CountryCode: str

class CityCreate(CityBase):
    pass

class City(CityBase):
    Code: int

    class Config:
        orm_mode = True

class CityFilter(BaseModel):
    city_name: Optional[str] = None  # Partial match search
    province_code: Optional[str] = None
    country_code: Optional[str] = None
    skip: int = 0  # Pagination
    limit: int = 100  # Pagination
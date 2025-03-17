# app/cities/crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def create_city(db: Session, city: schemas.CityCreate):
    db_city = models.City(
        CityPhoneCode=city.CityPhoneCode,
        CityName=city.CityName,
        ProvinceCode=city.ProvinceCode,
        CountryCode=city.CountryCode
    )
    db.add(db_city)
    db.commit()
    db.refresh(db_city)
    return db_city

def get_city(db: Session, city_code: int):
    return db.query(models.City).filter(models.City.Code == city_code).first()

def get_cities(db: Session, filters: schemas.CityFilter):
    query = db.query(models.City)
    if filters.city_name:
        query = query.filter(models.City.CityName.ilike(f"%{filters.city_name}%"))
    if filters.province_code:
        query = query.filter(models.City.ProvinceCode == filters.province_code)
    if filters.country_code:
        query = query.filter(models.City.CountryCode == filters.country_code)
    return query.offset(filters.skip).limit(filters.limit).all()
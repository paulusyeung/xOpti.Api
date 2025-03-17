# app/cities/routers.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..auth import get_current_user, oauth2_scheme
from ..schemas import TokenData
from . import schemas, crud

router = APIRouter(
    prefix="/cities",
    tags=["cities"]
)

@router.post("/", response_model=schemas.City)
def create_city(
    city: schemas.CityCreate,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    return crud.create_city(db=db, city=city)

@router.get("/{city_code}", response_model=schemas.City)
def read_city(
    city_code: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    db_city = crud.get_city(db=db, city_code=city_code)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

@router.get("/", response_model=List[schemas.City])
def read_cities(
    filters: schemas.CityFilter = Depends(),
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user)
):
    cities = crud.get_cities(db=db, filters=filters)
    return cities
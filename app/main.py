from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Already available via FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from .database import SessionLocal, engine, get_db
from .auth import get_current_user
from .models import Base
from .schemas_auto import *
from .users.routers import router as users_router
import inspect
import sys
from importlib import import_module

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="xOpti API",
    description="REST API for xOpti database",
    version="1.0.0",
    docs_url=None,  # Disable Swagger UI
    redoc_url=None  # Disable Redoc
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

models_module = import_module("app.models")
models = {name: cls for name, cls in inspect.getmembers(models_module, 
        lambda x: inspect.isclass(x) and x.__module__ == 'app.models' and issubclass(x, Base) and x != Base)}

# Put the users > login at top for easy naigation
app.include_router(users_router)
# Loop for all endpoints from models.py
for model_name, model in models.items():
    schema = globals().get(model_name)
    if schema:
        router = SQLAlchemyCRUDRouter(
            schema=schema,
            db_model=model,
            db=get_db,
            prefix=f"/{model_name.lower()}s",
            dependencies=[Depends(get_current_user)],
            paginate=100
        )
        app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to xOpti API"}
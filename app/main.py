from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from routes.auth import auth_router
from database import Base, engine
from schemas import schemas
from models import models
from database import database
from routes import auth
from utils import token, password_utils


models.Base.metadata.create_all(bind=engine)

app = FastAPI( title= "HPcapstone")

app.include_router(auth_router,prefix="/auth",tags=["authentications"])
from fastapi import FastAPI
from .file_routes import router as files
from .authorization_routes import router as authorization_jwt

def init_routes(app: FastAPI):
    app.include_router(files)
    app.include_router(authorization_jwt)
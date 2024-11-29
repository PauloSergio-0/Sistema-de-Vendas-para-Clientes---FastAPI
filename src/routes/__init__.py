from fastapi import FastAPI
from .file_routes import router as files
from .authorization_routes import router as authorization_jwt
from .cliente_routes import router as cliente_routes
from .produto_routes import router as produto_routes
from .venda_routes import router as venda_routes

def init_routes(app: FastAPI):
    app.include_router(files)
    app.include_router(authorization_jwt)
    app.include_router(cliente_routes)
    app.include_router(produto_routes)
    app.include_router(venda_routes)
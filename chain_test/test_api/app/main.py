from fastapi import FastAPI
from api.v1.endpoints.vector_api import router as vector_router

app = FastAPI()

app.include_router(vector_router, prefix="/api/v1")


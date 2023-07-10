from fastapi import FastAPI

from src.presentation.routes import measurement
from painkiller import create_database

app = FastAPI(
    title="Painkiller AI - Measurement Microservice"
)

app.include_router(measurement)

create_database()
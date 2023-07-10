from fastapi import FastAPI

from src.presentation.routes import patient
from painkiller import create_database

app = FastAPI(
    title="Painkiller AI - Patient Microservice"
)

app.include_router(patient)

create_database()
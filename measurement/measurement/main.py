from fastapi import FastAPI

from painkiller import create_database

from measurement.presentation.routes import measurement

app = FastAPI(
    title="Painkiller AI - Measurement Microservice"
)

app.include_router(measurement)

create_database()
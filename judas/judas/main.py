from fastapi import FastAPI

from jonas.presentation.routes import jonas
from painkiller import create_database

app = FastAPI(
    title="Painkiller AI - Jonas"
)

app.include_router(jonas)

create_database()
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

DATABASE_URI=getenv("DATABASE_URI")
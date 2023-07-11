from enum import Enum
from dataclasses import dataclass


@dataclass
class Message:
    status_code: str
    detail: str


class ErrorMessage(Enum):
    NOT_FOUND = Message("404", "Resources not found")
    NOT_INSERTED = Message("500", "Could not insert")

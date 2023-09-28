from pydantic import BaseModel

from datetime import date


class SProject(BaseModel):
    id: int
    title: str
    created_at: date
from pydantic import BaseModel


class SProfile(BaseModel):
    id: int
    lastname: str
    firstname: str
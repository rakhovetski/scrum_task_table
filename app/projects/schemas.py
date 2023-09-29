from typing import Optional
from pydantic import BaseModel, Field

from datetime import date


class SProjectMinReturn(BaseModel):
    id: int
    title: str
    created_at: Optional[date] = Field(None, )


class SProjectDetailReturn(BaseModel):
    id: int
    title: str
    description: Optional[str] = Field(None, )
    created_at: Optional[date] = Field(None, )


class SProjectParams(BaseModel):
    title: str = Field(..., min_length=3, max_length=60)
    description: Optional[str] = Field(None, min_length=10)


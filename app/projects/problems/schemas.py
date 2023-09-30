from typing import Optional
from pydantic import BaseModel, Field

from app.projects.problems.models import TaskType


class SProblemMinReturn(BaseModel):
    id: int
    title: str
    task_type: Optional[TaskType] = Field(TaskType.NA)
    hard_level: Optional[int] = Field(None, ge=1, le=10)


class SProblemDetailReturn(BaseModel):
    id: int = Field(..., ge=0)
    title: str = Field(max_length=70)
    description: Optional[str] = Field(None, max_length=1000)
    task_type: Optional[TaskType] = Field(TaskType.NA)
    hard_level: Optional[int] = Field(None, ge=1, le=10)
    profile_id: Optional[int] = Field(None, ge=0)
    project_id: int = Field(..., ge=0)


class SProblemProjectProblemId(BaseModel):
    project_id: int = Field(..., ge=0)
    problem_id: int = Field(..., ge=0)


class SProblemParams(BaseModel):
    title: str = Field(..., min_length=3, max_length=70),
    description: Optional[str] = Field(None, max_length=1000)
    task_type: TaskType = Field(TaskType.NA)
    hard_level: Optional[int] = Field(None, ge=1, le=10)
    profile_id: Optional[int] = Field(None, ge=0)
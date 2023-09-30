from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query
from app.profiles.schemas import SProfileMinReturn

from app.projects.dao import ProjectDAO
from app.projects.problems.dao import ProblemDAO
from app.projects.problems.models import TaskType
from app.projects.problems.router import router as problems_router
from app.projects.problems.schemas import SProblemMinReturn
from app.projects.schemas import SProjectMinReturn, SProjectDetailReturn, SProjectParams


router = APIRouter(
    prefix='/projects',
    tags=['Projects']
)
router.include_router(problems_router)


@router.get('')
async def get_all_projects() -> list[SProjectMinReturn]:
    return await ProjectDAO.find_all()


@router.post('', response_model_exclude_none=True)
async def create_project(project_params: SProjectParams = Body()) -> SProjectDetailReturn:
    return await ProjectDAO.insert(title=project_params.title,
                                   description=project_params.description)


@router.get('/{project_id}')
async def get_project_by_id(project_id: int = Path(..., ge=0)) -> SProjectDetailReturn | None:
    return await ProjectDAO.find_by_id(project_id)


@router.put('/{project_id}', response_model_exclude_none=True)
async def update_project(project_id: int = Path(..., ge=0),
                         project_params: SProjectParams = Body()) -> SProjectDetailReturn:
    return await ProjectDAO.update(project_id,
                                   title=project_params.title,
                                   description=project_params.description)


@router.delete('/{project_id}')
async def delete_project(project_id: int = Path(..., ge=0)) -> dict:
    return await ProjectDAO.delete(project_id)


@router.get('/{project_id}/problems')
async def get_problems_by_project_id(project_id: int = Path(..., ge=0),
                                     hard_level: Optional[int] = Query(None, ge=1, le=10),
                                     task_type: Optional[TaskType] = Query(None, )) -> list[SProblemMinReturn]:
    return await ProjectDAO.find_ploblems_by_project_id(project_id,
                                                        hard_level=hard_level,
                                                        task_type=task_type)


@router.get('/{project_id}/profiles')
async def get_profiles_by_project_id(project_id: int = Path(..., ge=0)) -> list[SProfileMinReturn]:
    return await ProjectDAO.find_profiles_by_project_id(project_id)
from typing import Annotated
from fastapi import APIRouter, Body, Depends, Path, Query
from pydantic import ValidationError

from app.projects.dao import ProjectDAO
from app.projects.problems.router import router as problems_router
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
async def create_project(project_params: SProjectParams = Depends()) -> SProjectDetailReturn:
    return await ProjectDAO.insert(title=project_params.title,
                                   description=project_params.description)


@router.get('/{project_id}')
async def get_project_by_id(project_id: int = Path(..., ge=0)) -> SProjectDetailReturn | None:
    return await ProjectDAO.find_by_id(project_id)


@router.put('/{project_id}', response_model_exclude_none=True)
async def update_project(project_id: int = Path(..., ge=0),
                         project_params: SProjectParams = Depends()) -> SProjectDetailReturn:
    return await ProjectDAO.update(project_id,
                                   title=project_params.title,
                                   description=project_params.description)


@router.delete('/{project_id}')
async def delete_project(project_id: int = Path(..., ge=0)) -> dict:
    return await ProjectDAO.delete(project_id)
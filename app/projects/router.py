from fastapi import APIRouter

from app.projects.dao import ProjectDAO
from app.projects.schemas import SProject


router = APIRouter(
    prefix='/projects',
    tags=['Projects']
)


@router.get('')
async def get_all_projects() -> list[SProject]:
    return await ProjectDAO.find_all()

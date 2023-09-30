from sqlalchemy import select

from app.base.dao import BaseDAO
from app.projects.models import Project
from app.database import async_session_maker
from app.projects.problems.models import Problem
from app.profiles.models import Profile


class ProjectDAO(BaseDAO):
    model = Project


    @classmethod
    async def find_objects_by_project_id(cls,
                                         model,
                                         project_id: int,
                                         **kwargs):
        async with async_session_maker() as session:
            query = select(model).where(
                Project.id == project_id
            )
            for kwarg_key, kwarg_value in kwargs.items():
                if kwarg_value is not None:
                    query = query.filter(getattr(model, kwarg_key) == kwarg_value)
            result = await session.execute(query)
            return result.scalars().all()


    @classmethod
    async def find_ploblems_by_project_id(cls,
                                          project_id: int,
                                          hard_level,
                                          task_type):
        return await ProjectDAO.find_objects_by_project_id(model=Problem,
                                                           project_id=project_id,
                                                           hard_level=hard_level,
                                                           task_type=task_type)


    @classmethod
    async def find_profiles_by_project_id(cls,
                                          project_id: int):
        return await ProjectDAO.find_objects_by_project_id(model=Profile,
                                                           project_id=project_id)
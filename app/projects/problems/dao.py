from typing import Optional
from sqlalchemy import and_, delete, select, update

from app.base.dao import BaseDAO
from app.database import async_session_maker
from app.projects.problems.models import Problem, TaskType


class ProblemDAO(BaseDAO):
    model = Problem
        

    @classmethod
    async def find_problems_by_project_id_and_problem_id(cls,
                                                         project_id: int,
                                                         problem_id: int):
        async with async_session_maker() as session:
            query = select(Problem).where(
                and_(Problem.id == problem_id,
                     Problem.project_id == project_id)
            )
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def update(cls,
                     problem_id,
                     project_id,
                     **kwargs):
        async with async_session_maker() as session:
            query = update(Problem).where(
                and_(Problem.id == problem_id,
                     Problem.project_id == project_id)
            ).values(
                **kwargs
            ).returning(Problem.id)
            result = await session.execute(query)
            await session.commit()
            return {'id': result.fetchone()[0],
                    'project_id': project_id,
                    'problem_id': problem_id,
                    **kwargs}

    
    @classmethod
    async def delete(cls,
                     problem_id,
                     project_id):
        async with async_session_maker() as session:
            query = delete(Problem).where(
                and_(Problem.id == problem_id,
                     Problem.project_id == project_id)
            ).returning(Problem.id)
            result = await session.execute(query)
            id_from_result = result.fetchone()
            if id_from_result:
                await session.commit()
                return {'id': id_from_result[0]}
            return None
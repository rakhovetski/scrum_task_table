from fastapi import Body, Depends, Path, APIRouter

from app.projects.problems.dao import ProblemDAO
from app.projects.problems.schemas import SProblemParams, SProblemProjectProblemId, SProblemMinReturn, SProblemDetailReturn


router = APIRouter(
    prefix='/{project_id}/problems',
    tags=['Problems']
)


@router.get('')
async def get_problems_by_project_id(project_id: int = Path(..., ge=0)) -> list[SProblemMinReturn]:
    return await ProblemDAO.find_all(project_id=project_id)


@router.get('/{problem_id}')
async def get_problem_by_id_and_project_id(problem_project_id: SProblemProjectProblemId = Depends()) -> SProblemDetailReturn | None:
    return await ProblemDAO.find_problems_by_project_id_and_problem_id(project_id=problem_project_id.project_id,
                                                                       problem_id=problem_project_id.problem_id)


@router.post('')
async def create_problem_to_project(project_id: int = Path(..., ge=0),
                                    problem_params: SProblemParams = Depends()) -> SProblemDetailReturn:
    return await ProblemDAO.insert(project_id=project_id,
                                   title=problem_params.title,
                                   description=problem_params.description,
                                   task_type=problem_params.task_type,
                                   hard_level=problem_params.hard_level,
                                   profile_id=problem_params.profile_id)


@router.put('/{problem_id}')
async def update_problem_from_project(problem_project_id: SProblemProjectProblemId = Depends(),
                                      problem_params: SProblemParams = Depends()) -> SProblemDetailReturn | None:
    return await ProblemDAO.update(problem_id=problem_project_id.problem_id,
                                   project_id=problem_project_id.project_id,
                                   title=problem_params.title,
                                   description=problem_params.description,
                                   task_type=problem_params.task_type,
                                   hard_level=problem_params.hard_level,
                                   profile_id=problem_params.profile_id)


@router.delete('/{problem_id}')
async def delete_problem_from_project(problem_project_id: SProblemProjectProblemId = Depends()) -> dict | None:
    return await ProblemDAO.delete(problem_id=problem_project_id.problem_id,
                                   project_id=problem_project_id.project_id)


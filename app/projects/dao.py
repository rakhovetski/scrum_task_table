from sqlalchemy import select

from app.base.dao import BaseDAO
from app.projects.models import Project
from app.projects.problems.models import Problem
from app.profiles.models import Profile
from app.database import async_session_maker


class ProjectDAO(BaseDAO):
    model = Project

    
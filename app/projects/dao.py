from app.dao.base import BaseDAO
from app.projects.models import Project


class ProjectDAO(BaseDAO):
    model = Project
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from typing import TYPE_CHECKING
from datetime import date

from app.database import Base


if TYPE_CHECKING:
    from app.profiles.models import Profile
    from app.projects.problems.models import Problem


class ProjectProfile(Base):
    __tablename__ = 'project_profiles'

    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), primary_key=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey('profiles.id'), primary_key=True)
    role: Mapped[str] = mapped_column(String(32), nullable=False)
    is_creator: Mapped[bool] = mapped_column(default=False)


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str] = mapped_column()
    created_at: Mapped[date] = mapped_column(default=date.today())

    profiles: Mapped['Profile'] = relationship(
        back_populates='projects',
        secondary='project_profiles'
    )
    problems: Mapped[list['Problem']] = relationship(
        back_populates='project'
    )
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from app.database import Base


if TYPE_CHECKING:
    from app.projects.models import Project
    from app.projects.problems.models import Problem


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(64), nullable=False)
    firstname: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(128), nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    projects: Mapped['Project'] = relationship(
        back_populates='profiles',
        secondary='project_profiles'
    )
    problems: Mapped['Problem'] = relationship(
        back_populates='profile'
    )


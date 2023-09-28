from sqlalchemy import String, ForeignKey
from sqlalchemy import Enum as AlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
from enum import Enum

from app.database import Base


if TYPE_CHECKING:
    from app.profiles.models import Profile


class TaskType(Enum):
    NA = 'Not Active'
    AC = 'Active'
    RW = 'In Rewiew'
    CM = 'Completed'


class Problem(Base):
    __tablename__ = 'problems'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(70), nullable=False)
    description: Mapped[str] = mapped_column()
    task_type: Mapped[TaskType] = mapped_column(default=TaskType.NA)
    hard_level: Mapped[int] = mapped_column()
    profile_id: Mapped[int] = mapped_column(ForeignKey('profiles.id'))
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), nullable=False)

    profile: Mapped['Profile'] = relationship(
        back_populates='problems'
    )
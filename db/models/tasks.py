from . import Base,Mapped,mapped_column
from datetime import datetime


class Task(Base):
    __tablename__ = "tasks"
    name:Mapped[str]
    description:Mapped[str]
    end_date:Mapped[datetime]
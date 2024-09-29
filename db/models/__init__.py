from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,sessionmaker
from sqlalchemy import create_engine



engine = create_engine("sqlite+pysqlite:///mydb.db", echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)

from .tasks import Task

def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)







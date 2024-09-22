from . import Base,Mapped


class User(Base):
    __tablename__ = "users"

    name:Mapped[int]
from . import app,UserData
from db import User,Session
from sqlalchemy import select

@app.get("/users")
async def all_users():
    with Session() as session:
        users = session.scalars(select(User)).all()
        return users
    

@app.post("/users")
async def create_user(data:UserData):
    with Session.begin() as session:
        new_user = User(**data.model_dump())
        user = session.scalar(select(User).where(User.name==new_user.name))
        if user:
            return "user already exists"
        else:
            session.add(new_user)
            return new_user
    

@app.delete("/users")
async def delete_user(name:str):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.name==name))
        if user:
            session.delete(user)
            return user
        else:
            return "user doesn't exist"
    







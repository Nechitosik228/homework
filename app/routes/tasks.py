from . import app,TaskData
from db import Task,Session
from sqlalchemy import select,update



@app.get("/tasks")
async def get_tasks():
    with Session() as session:
        tasks = session.scalars(select(Task)).all()
        return tasks


@app.post("/tasks")
async def create_task(data:TaskData):
    with Session.begin() as session:
        task = Task(**data.model_dump())
        session.add(task)
        return task
    

@app.put("/tasks/{id}")
async def update_task(id:int,data:TaskData):
    with Session() as session:
        task = session.scalar(select(Task).where(Task.id == id))
        if task:
            edit = update(Task).where(Task.id==id).values(
                name=data.name,
                description=data.description,
                end_date=data.end_date
                )
            session.execute(edit)
            return task
        else:
            return "task does not exist"
        

@app.get("/tasks/{id}")
async def get_task(id:int):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id==id))
        if task:
            data = {"id":task.id,
                    "name":task.name,
                    "description":task.description,
                    "end date":task.end_date}
            return data
        else:
            return "task does not exist"
        


@app.delete("/tasks/{id}")
async def delete_task(id:int):
    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.id==id))
        if task:
            session.delete(task)
            return task
        else:
            return "task does not exist"
    
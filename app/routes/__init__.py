from fastapi import FastAPI
from ..schemas import TaskData




app = FastAPI()


from . import tasks


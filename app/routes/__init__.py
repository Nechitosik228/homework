from fastapi import FastAPI
from ..schemas import UserData




app = FastAPI()


from . import users


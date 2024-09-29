from pydantic import BaseModel
from datetime import datetime


class TaskData(BaseModel):
    name:str
    description:str
    end_date:datetime



from app import app
from db import up,down
import uvicorn


if __name__ =="__main__":
    down()
    up()
    uvicorn.run(app,host="localhost",port=8080)
    
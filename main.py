from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel


from database import create_tables, delete_tables

from contextlib import asynccontextmanager


app = FastAPI(lifespan=lifespan)




@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Clean")
    await create_tables()
    print("Database is ready")
    yield
    print("close")


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Write this video")
#     return {"data": task}

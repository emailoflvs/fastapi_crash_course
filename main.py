from typing import Annotated, Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel

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

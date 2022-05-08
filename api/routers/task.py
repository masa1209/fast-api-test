from fastapi import APIRouter
from typing import List

import api.schemas.task as task_schema

router = APIRouter()


@router.get("/tasks")
async def list_tasks():
    pass

@router.put("/tasks/{task_id}")
async def update_task():
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    pass

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())



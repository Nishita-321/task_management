from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

tasks = []

next_id = 1


class TaskCreate(BaseModel):
    title : str
    description : str
    status : str = "pending"

 

@app.get("/")
def home():
    return{"message" : "Welcome to Task Management API",
           "status" : "success"}


@app.post("/tasks")
def create_task(task_data : TaskCreate):
    global next_id

    new_task = {
        "id" : next_id,
        "title" : task_data.title,
        "description" : task_data.description,
        "status" : task_data.status
    }

    tasks.append(new_task)
    next_id += 1

    return {
        "message" : "Task created successfully",
        "task" : new_task
    }

@app.get("/tasks")
def get_tasks():
    return {
        "total" : len(tasks),
        "tasks" : tasks
    }


@app.get("/tasks/{task_id}")
def get_task_id(task_id : int):

    for task in tasks:
        if task["id"] == task_id:
            return task


    raise HTTPException(
        status_code = 404,
        detail = " Task not found"
    )

@app.get("/tasks/title/{task_title}")
def get_task_title(task_title : str):

    for task in tasks:
        if task["title"] == task_title:
            return task


    raise HTTPException(
        status_code = 404,
        detail = "Task not found"
    )

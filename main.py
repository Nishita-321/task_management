from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Task
from schemas import TaskCreate, TaskResponse


app = FastAPI()

# tasks = []



# next_id = 1


class TaskCreate(BaseModel):
    title : str
    description : str
    status : str = "pending"

 

@app.get("/")
def home():
    return{"message" : "Welcome to Task Management API",
           "status" : "success"}


@app.post("/tasks", response_model=TaskResponse)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task



# @app.get("/tasks")
# def get_tasks():
#     return {
#         "total" : len(tasks),
#         "tasks" : tasks
#     }

# @app.get("/tasks/count")
# def count_tasks():
#     return {
#         "Task_count" : len(tasks)
#     }

# @app.get("/tasks/filter")
# def status_check(status : str):

#     filtered_tasks = []

#     for task in tasks:
#         if task["status"] == status:
#             filtered_tasks.append(task)
        
    
#     return filtered_tasks


        

# @app.get("/tasks/{task_id}")
# def get_task_id(task_id : int):

#     for task in tasks:
#         if task["id"] == task_id:
#             return task


#     raise HTTPException(
#         status_code = 404,
#         detail = " Task not found"
#     )

# @app.get("/tasks/title/{task_title}")
# def get_task_title(task_title : str):

#     for task in tasks:
#         if task["title"] == task_title:
#             return task


#     raise HTTPException(
#         status_code = 404,
#         detail = "Task not found"
#     )


# @app.get("/about")
# def about():
#     return {
#         "project_name" : "Task Management API",
#         "version" : "1.0.0"
#     }

# @app.get("/health")
# def health_check():
#     return {
#         "status" : "healthy"
#     }

# @app.get("/greet/{name}")
# def greet_person(name : str):
#     return {
#         "message" : f"Hi {name}, Welcome to FastAPI"
#     }


# @app.get("/search")
# def search(keyword : str = "python", category : str | None = None):
#     return {
#         "keyword" : f"searching for {keyword}",
#         "category" : category
#     }


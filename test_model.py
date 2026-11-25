from sqlalchemy import select
from database import SessionLocal
from models import Task

db = SessionLocal()

try:
    statement = select(Task)

    result = db.execute(statement)

    tasks = result.scalars().all()

    print("Tasks retrieved from MySQL:")

    for task in tasks:
        print(
            task.id,
            task.title,
            task.description,
            task.status
        )

finally:
    db.close()

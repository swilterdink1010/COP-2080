from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import datetime as dt

app = FastAPI(title="To-Do List API")

tasks = {}
task_count = 0
creation_log = []

class TaskCreate(BaseModel):
    title: str
    desc: Optional[str] = ""
    complete: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None
    complete: bool = None

@app.get("/")
def root():
    return {
        "message": app.title + " is running\n...better go catch it"
    }

@app.get("/tasks")
def get_all_tasks():
    return {
        "tasks": list(tasks.values()), 
        "total": len(tasks)
    }

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return tasks[task_id]

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global task_count
    task_count += 1
    now = dt.datetime.now().isoformat()
    new_task = {
        "id": task_count,
        "title": task.title,
        "desc": task.desc,
        "complete": task.complete,
        "created_at": now
    }
    tasks[task_count] = new_task
    creation_log.append(now[:10])
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    temp = tasks[task_id]
    if task.title is not None:
        temp["title"] = task.title
    if task.desc is not None:
        temp["desc"] = task.desc
    if task.complete is not None:
        temp["complete"] = task.complete
    tasks[task_id] = temp
    return temp

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    deleted = tasks.pop(task_id)
    return {"message": f"Task {task_id} deleted"}

@app.get("/stats")
def get_stats():
    total = len(tasks)
    complete = sum(1 for t in tasks.values() if t["complete"])
    pending = total - complete
    return {
        "total": total,
        "complete": complete,
        "pending": pending,
        "creation_log": creation_log
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
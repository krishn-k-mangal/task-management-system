from fastapi import FastAPI
from src.tasks.models import TaskModel
from src.utils.db import Base , engine

Base.metadata.create_all(engine)

app = FastAPI(title = "This is my Task Managema=ent Application")
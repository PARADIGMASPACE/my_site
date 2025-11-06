from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)


@app.get("/")
def read_root():
    return {"Hello": "World"}

from fastapi import FastAPI
import uvicorn

from core.config import settings
from database import Base, engine
from routers import events

# создаём таблицы
Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.app_name)

app.include_router(events.router)


@app.get("/")
def root():
    return {"message": "API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)

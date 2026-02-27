import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.utilities.logging_client import logger

from app.routers.marks import router as MarksRouter
from app.routers.students import router as StudentsRouter
from app.routers.majors import router as MajorsRouter


app = FastAPI(title="Base School")

app.include_router(MarksRouter)
app.include_router(StudentsRouter)
app.include_router(MajorsRouter)

logger.info("Server Started")


def main():
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
    )


if __name__ == "__main__":
    main()
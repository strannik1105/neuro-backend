import uvicorn
from fastapi import FastAPI
from common.config import settings
from router.api import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")


def main():
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        use_colors=True,
    )


if __name__ == "__main__":
    main()

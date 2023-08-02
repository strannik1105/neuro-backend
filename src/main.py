import uvicorn
from fastapi import FastAPI

from common.config import settings

app = FastAPI()


def main():
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        use_colors=True,
    )


if __name__ == "main":
    main()

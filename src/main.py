import uvicorn
from fastapi import FastAPI

from common.config import settings

app = FastAPI()


@app.on_event("startup")
def on_startup():
    pass


def main():
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        use_colors=True,
    )


if __name__ == 'main':
    main()

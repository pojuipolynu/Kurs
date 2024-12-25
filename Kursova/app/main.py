from fastapi import FastAPI
from core.config import settings
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from routers.healthcheck import router as healthcheck_router
from routers.song_router import router as song_router

app = FastAPI()
app.include_router(healthcheck_router)
app.include_router(song_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_main():
    return { "status_code": 200,
            "detail": "ok",
            "result": "working"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.PORT, log_level="info", reload = settings.RELOAD, host=settings.HOST)
from fastapi import FastAPI
from app.api.routes import router as api_router
from app.api.users import router as user_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, env=settings.APP_ENV)
app.include_router(api_router)
app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME}!"}
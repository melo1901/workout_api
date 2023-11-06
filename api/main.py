import uvicorn
from fastapi.applications import FastAPI
from api.endpoints.activity import router as activity_router
from api.endpoints.user import router as user_router
from api.endpoints.health import router as health_router
from api.endpoints.connection import router as connection_router


app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(activity_router, prefix="/activities", tags=["activities"])
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(connection_router, prefix="/connection", tags=["connection"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

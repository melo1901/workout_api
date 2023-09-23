from fastapi.applications import FastAPI
from api.endpoints.activity import router as activity_router
from api.endpoints.user import router as user_router

app = FastAPI()
app.include_router(activity_router, prefix="/activity", tags=["activity"])
app.include_router(user_router, prefix="/user", tags=["user"])

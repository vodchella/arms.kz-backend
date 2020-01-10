from fastapi import APIRouter
from pkg.rest.routers.v1.exercise import router as exercise_router
from pkg.rest.routers.v1.workout import router as workout_router

router = APIRouter()
router.include_router(exercise_router, prefix='/exercise')
router.include_router(workout_router, prefix='/workout')

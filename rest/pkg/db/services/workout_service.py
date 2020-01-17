from pkg.db import db
from pkg.db.models.workout import Workout
from sqlalchemy import desc


class WorkoutService:
    @staticmethod
    async def list(user_id: str):
        workouts = Workout.__table__
        query = workouts.select() \
            .where(workouts.c.user_id == user_id) \
            .order_by(desc(workouts.c.date))
        return await db.fetch_all(query)

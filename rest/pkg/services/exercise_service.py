from pkg.db import db
from pkg.db.models.exercise import Exercise
from sqlalchemy import desc


class ExerciseService:
    @staticmethod
    async def list(user_id: str):
        exercises = Exercise.__table__
        query = exercises.select() \
            .where(exercises.c.user_id == user_id) \
            .order_by(desc(exercises.c.last_workout_date))
        return await db.fetch_all(query)

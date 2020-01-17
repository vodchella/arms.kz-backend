from pkg.db import db
from pkg.db.models.exercise import Exercise, ExerciseCategory
from sqlalchemy import desc


class ExerciseService:
    @staticmethod
    async def view(exercise_id: str):
        exercises = Exercise.__table__
        query = exercises.select() \
            .where(exercises.c.id == exercise_id)
        return await db.fetch_one(query)

    @staticmethod
    async def list(user_id: str):
        exercises = Exercise.__table__
        query = exercises.select() \
            .where(exercises.c.user_id == user_id) \
            .order_by(desc(exercises.c.last_workout_date))
        return await db.fetch_all(query)

    @staticmethod
    async def list_categories(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .order_by(categories.c.name)
        return await db.fetch_all(query)

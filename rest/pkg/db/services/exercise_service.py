from pkg.db import db
from pkg.db.models.exercise import Exercise, ExerciseCategory
from pkg.db.models.workout import Workout
from sqlalchemy import desc
from sqlalchemy.sql import Select


class ExerciseService:
    @staticmethod
    async def view(exercise_id: str):
        exercises = Exercise.__table__
        query = exercises.select() \
            .where(exercises.c.id == exercise_id)
        return await db.fetch_one(query)

    @staticmethod
    async def list(user_id: str):
        e = Exercise.__table__
        w = Workout.__table__
        query = Select(columns=[*e.c, w.c.date.label('last_workout_date')]) \
            .select_from(e.join(w)) \
            .where(e.c.user_id == user_id) \
            .where(w.c.id == e.c.last_workout_id) \
            .order_by(desc(w.c.date))
        print(query)
        return await db.fetch_all(query)

    @staticmethod
    async def list_categories(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .order_by(categories.c.name)
        return await db.fetch_all(query)

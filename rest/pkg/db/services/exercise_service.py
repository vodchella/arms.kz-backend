from pkg.db import db
from pkg.db.models.exercise import Exercise
from pkg.db.models.workout import Workout
from sqlalchemy import desc, nullslast
from sqlalchemy.sql import Select
from sqlalchemy.sql.expression import false


class ExerciseService:
    @staticmethod
    async def view(exercise_id: str):
        exercises = Exercise.__table__
        query = exercises.select() \
            .where(exercises.c.is_deleted == false()) \
            .where(exercises.c.id == exercise_id)
        return await db.fetch_one(query)

    @staticmethod
    async def list(user_id: str):
        e = Exercise.__table__
        w = Workout.__table__
        query = Select(columns=[*e.c, w.c.date.label('last_workout_date')]) \
            .select_from(e.outerjoin(w)) \
            .where(e.c.user_id == user_id) \
            .where(e.c.is_deleted == false()) \
            .order_by(nullslast(desc(w.c.date)))
        return await db.fetch_all(query)

    @staticmethod
    async def move_exercises(from_category_id: str, to_category_id: str):
        exercises = Exercise.__table__
        query = exercises.update() \
            .where(exercises.c.category_id == from_category_id) \
            .values(category_id=to_category_id)
        await db.execute(query)

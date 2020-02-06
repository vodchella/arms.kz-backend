from pkg.db import db
from pkg.db.models.exercise import Exercise, ExerciseCategory
from pkg.db.models.workout import Workout
from pkg.rest.models.exercise import ExerciseCategory as ExerciseCategoryDTO
from pkg.utils.db import generate_unique_id
from sqlalchemy import desc, nullslast
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
            .select_from(e.outerjoin(w)) \
            .where(e.c.user_id == user_id) \
            .order_by(nullslast(desc(w.c.date)))
        return await db.fetch_all(query)

    @staticmethod
    async def list_categories(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .order_by(categories.c.name)
        return await db.fetch_all(query)

    @staticmethod
    async def create_category(data: ExerciseCategoryDTO, user_id: str):
        categories = ExerciseCategory.__table__
        category_id = generate_unique_id()
        query = categories.insert().values(id=category_id,
                                           user_id=user_id,
                                           name=data.name)
        await db.execute(query)
        return category_id


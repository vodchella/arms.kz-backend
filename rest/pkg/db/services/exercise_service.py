from pkg.db import db
from pkg.db.models.exercise import Exercise, ExerciseCategory
from pkg.db.models.workout import Workout
from pkg.rest.models.exercise import ExerciseCategory as ExerciseCategoryDTO
from pkg.utils.db import generate_unique_id
from sqlalchemy import desc, nullslast
from sqlalchemy.sql import Select
from sqlalchemy.sql.expression import false, true


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

    @staticmethod
    async def view_category(category_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.is_deleted == false()) \
            .where(categories.c.id == category_id)
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def find_main_category(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .where(categories.c.is_deleted == false()) \
            .where(categories.c.is_main == true())
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def list_categories(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .where(categories.c.is_deleted == false()) \
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

    @staticmethod
    async def update_category(data: ExerciseCategoryDTO):
        categories = ExerciseCategory.__table__
        query = categories.update() \
            .where(categories.c.id == data.id) \
            .where(categories.c.is_main == false()) \
            .where(categories.c.is_deleted == false()) \
            .values(name=data.name)
        await db.execute(query)

    @staticmethod
    async def delete_category(category_id: str):
        categories = ExerciseCategory.__table__
        query = categories.update() \
            .where(categories.c.id == category_id) \
            .where(categories.c.is_main == false()) \
            .values(is_deleted=True)
        await db.execute(query)

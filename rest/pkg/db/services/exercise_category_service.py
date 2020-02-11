from pkg.db import db
from pkg.db.models.exercise import ExerciseCategory
from pkg.rest.models.exercise import ExerciseCategory as ExerciseCategoryDTO
from pkg.utils.db import generate_unique_id
from sqlalchemy.sql.expression import false, true


class ExerciseCategoryService:
    @staticmethod
    async def get(category_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.is_deleted == false()) \
            .where(categories.c.id == category_id)
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def find_main(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .where(categories.c.is_deleted == false()) \
            .where(categories.c.is_main == true())
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def list(user_id: str):
        categories = ExerciseCategory.__table__
        query = categories.select() \
            .where(categories.c.user_id == user_id) \
            .where(categories.c.is_deleted == false()) \
            .order_by(categories.c.name)
        return await db.fetch_all(query)

    @staticmethod
    async def create(data: ExerciseCategoryDTO, user_id: str, is_main: bool = False):
        categories = ExerciseCategory.__table__
        category_id = generate_unique_id()
        query = categories.insert().values(id=category_id,
                                           user_id=user_id,
                                           is_main=is_main,
                                           name=data.name)
        await db.execute(query)
        return category_id

    @staticmethod
    async def create_default_category(user_id: str):
        default_category = ExerciseCategory(name='Не задана')
        await ExerciseCategoryService.create(default_category, user_id, is_main=True)

    @staticmethod
    async def update(category_id: str, data: ExerciseCategoryDTO):
        categories = ExerciseCategory.__table__
        query = categories.update() \
            .where(categories.c.id == category_id) \
            .where(categories.c.is_main == false()) \
            .where(categories.c.is_deleted == false()) \
            .values(name=data.name)
        await db.execute(query)

    @staticmethod
    async def delete(category_id: str):
        categories = ExerciseCategory.__table__
        query = categories.update() \
            .where(categories.c.id == category_id) \
            .where(categories.c.is_main == false()) \
            .values(is_deleted=True)
        await db.execute(query)

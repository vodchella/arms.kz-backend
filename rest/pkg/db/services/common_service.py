from pkg.db import db
from pkg.utils.errors import CustomException
from sqlalchemy import func, Table
from sqlalchemy.sql import Select


class CommonService:
    @staticmethod
    async def check_entity_belongs_to_user(table: Table, exercise_id: str, user_id: str):
        query = Select(columns=[func.count().label('cnt')]) \
            .select_from(table) \
            .where(table.c.user_id == user_id) \
            .where(table.c.id == exercise_id)
        row = await db.fetch_one(query)
        result = dict(row)['cnt'] != 0 if row is not None else False
        if not result:
            raise CustomException('Недостаточно прав для просмотра записи')

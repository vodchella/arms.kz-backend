from pkg.db import db
from pkg.db.models.user import User


class UserService:
    @staticmethod
    async def get_by_email(email: str):
        users = User.__table__
        query = users.select() \
            .where(users.c.email == email)
        return await db.fetch_one(query)

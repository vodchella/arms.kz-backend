from pkg.db import db
from pkg.db.models.user import User
from pkg.utils.db import generate_unique_id


class UserService:
    @staticmethod
    async def get_by_id(user_id: str):
        users = User.__table__
        query = users.select() \
            .where(users.c.id == user_id)
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def get_by_email(email: str):
        users = User.__table__
        query = users.select() \
            .where(users.c.email == email)
        result = await db.fetch_one(query)
        return dict(result) if result is not None else None

    @staticmethod
    async def create(email: str, name: str = None, picture: str = None, locale: str = None):
        users = User.__table__
        user_id = generate_unique_id()
        query = users.insert().values(id=user_id,
                                      email=email,
                                      name=name,
                                      picture=picture,
                                      locale=locale)
        await db.execute(query)
        return user_id

    @staticmethod
    async def set_token_key(user_id: str, token_key: str):
        users = User.__table__
        query = users.update() \
            .where(users.c.id == user_id) \
            .values(token_key=token_key)
        await db.execute(query)

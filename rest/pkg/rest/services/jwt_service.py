import jwt
from datetime import datetime, timedelta
from pkg.config import CONFIG
from pkg.db.services.user_service import UserService
from pkg.rest.models.token_pair import TokenPair
from pkg.rest.models.token_payload import TokenPayload
from pkg.utils.db import generate_unique_id
from typing import Union


def _create_token(user_id: str, token_key: str, token_type: str):
    if token_type == 'a':
        expires_at = datetime.utcnow() + timedelta(hours=2)
    elif token_type == 'r':
        expires_at = datetime.utcnow() + timedelta(days=7)
    else:
        raise Exception('Invalid token type')

    payload = TokenPayload(ver=1,
                           uid=user_id,
                           exp=expires_at,
                           typ=token_type,
                           key=token_key)

    return jwt.encode(payload.dict(), CONFIG['jwt']['secret'], algorithm='HS256')


class JwtService:
    @staticmethod
    async def create_token_pair(user_id: str) -> TokenPair:
        token_key = generate_unique_id()
        await UserService.set_token_key(user_id, token_key)
        auth = _create_token(user_id, token_key, 'a')
        refresh = _create_token(user_id, token_key, 'r')
        return TokenPair(auth=auth, refresh=refresh)

    @staticmethod
    def validate_token(token: str, expected_type: str) -> Union[TokenPayload, bool]:
        try:
            payload_dict = jwt.decode(token, CONFIG['jwt']['secret'], algorithm='HS256')
            payload = TokenPayload(**payload_dict)
            if payload.ver != 1:
                return False
            if payload.typ != expected_type:
                return False
            return payload
        except jwt.PyJWTError:
            return False

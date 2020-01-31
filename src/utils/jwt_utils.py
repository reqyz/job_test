from typing import Dict

import jwt

from utils.exeptions import TokenError


async def jwt_encode(data: Dict, secret: str) -> str:
    try:
        rv = jwt.encode(data, secret).decode()
    except jwt.exceptions.PyJWTError:
        raise TokenError
    return rv


async def jwt_decode(token: str, secret: str = '', validate: bool = True) -> Dict:
    try:
        rv = jwt.decode(token, secret, validate)
    except jwt.exceptions.PyJWTError:
        raise TokenError
    return rv

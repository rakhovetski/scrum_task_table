from fastapi import Depends, Request
from jose import jwt, ExpiredSignatureError, JWTError

from app.config import settings
from app.exceptions import TokenDoesnotExistException, IncorrectTokenFormatException, ProfileIsNotPresentException
from app.profiles.dao import ProfileDAO


def get_token(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise TokenDoesnotExistException
    return token


async def get_current_profile(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        raise TokenDoesnotExistException
    except JWTError:
        raise IncorrectTokenFormatException
    profile_id = payload.get('sub')
    if not profile_id:
        raise ProfileIsNotPresentException
    profile = await ProfileDAO.find_by_id(id=int(profile_id))
    if not profile:
        raise ProfileIsNotPresentException
    return profile
    
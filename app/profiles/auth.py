from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.profiles.dao import ProfileDAO
from app.exceptions import IncorrectEmailOrPasswordException


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(input_password, hashed_password) -> bool:
    return pwd_context.verify(input_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_profile(email: EmailStr, password: str):
    profile = await ProfileDAO.find_by_email(email=email)
    if not (profile and verify_password(password, profile.hashed_password)):
        raise IncorrectEmailOrPasswordException
    return profile
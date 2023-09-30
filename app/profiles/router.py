from fastapi import APIRouter, Depends, Response

from app.profiles.dao import ProfileDAO
from app.profiles.models import Profile
from app.profiles.schemas import SProfileLoginInfo, SProfileRegisterInfo, SProfileMinReturn, SProfileDetailReturn
from app.exceptions import ProfileAlreadyRegisteredException
from app.profiles.auth import authenticate_profile, create_access_token, create_password_hash
from app.profiles.dependencies import get_current_profile


router_profiles = APIRouter(
    prefix='/profiles',
    tags=['Profiles']
)


auth_router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router_profiles.get('')
async def get_all_profiles() -> list[SProfileMinReturn]:
    return await ProfileDAO.find_all()


@router_profiles.get('/{profile_id}')
async def get_profile_by_id(profile_id: int) -> SProfileDetailReturn:
    return await ProfileDAO.find_by_id(profile_id)


@router_profiles.get('/me')
async def get_my_profile(my_profile: Profile = Depends(get_current_profile)) -> SProfileDetailReturn:
    return my_profile


@auth_router.post('/register')
async def register_profile(profile_info: SProfileRegisterInfo) -> SProfileDetailReturn:
    profile_exists = await ProfileDAO.find_by_email(profile_info.email)
    if profile_exists:
        raise ProfileAlreadyRegisteredException
    hashed_password = create_password_hash(profile_info.password)
    new_profile = await ProfileDAO.insert(
        firstname=profile_info.firstname,
        lastname=profile_info.lastname,
        email=profile_info.email,
        hashed_password=hashed_password
    )
    return new_profile


@auth_router.post('/login')
async def login_profile(response: Response,
                        profile_info: SProfileLoginInfo) -> dict:
    profile = await authenticate_profile(profile_info.email, profile_info.password)

    access_token = create_access_token({'sub': str(profile.id)})
    response.set_cookie('access_token', access_token, httponly=True)
    return {'access_token': access_token}


@auth_router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('access_token')

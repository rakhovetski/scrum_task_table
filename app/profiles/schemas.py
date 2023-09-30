from pydantic import BaseModel, Field, EmailStr


class SProfileMinReturn(BaseModel):
    id: int
    email: EmailStr


class SProfileDetailReturn(BaseModel):
    id: int
    email: EmailStr
    lastname: str
    firstname: str


class SProfileRegisterInfo(BaseModel):
    lastname: str = Field(..., max_length=64)
    firstname: str = Field(..., max_length=64)
    email: EmailStr = Field(..., max_length=128)
    password: str


class SProfileLoginInfo(BaseModel):
    email: EmailStr = Field(..., max_length=128)
    password: str
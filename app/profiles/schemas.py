from pydantic import BaseModel, Field, EmailStr


class SProfileRegisterInfo(BaseModel):
    lastname: str = Field(..., max_length=64)
    firstname: str = Field(..., max_length=64)
    email: EmailStr = Field(..., max_length=128)
    password: str


class SProfileLoginInfo(BaseModel):
    email: EmailStr = Field(..., max_length=128)
    password: str
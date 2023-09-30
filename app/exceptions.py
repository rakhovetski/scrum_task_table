from fastapi import HTTPException, status


class MyException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidProjectParamsException(MyException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid project params"


class ProfileAlreadyRegisteredException(MyException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Profile with this email aleady exists"


class IncorrectEmailOrPasswordException(MyException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Incorrect email or password"


class TokenDoesnotExistException(MyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token does not exist'


class IncorrectTokenFormatException(MyException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect token format'


class ProfileIsNotPresentException(MyException):
    status_code = status.HTTP_401_UNAUTHORIZED
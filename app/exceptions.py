from fastapi import HTTPException, status


class MyException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidProjectParamsException(HTTPException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    detail = "Invalid project params"
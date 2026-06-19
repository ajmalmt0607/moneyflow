from pydantic import BaseModel
from pydantic import EmailStr


class RegisterRequest(BaseModel):

    email: EmailStr
    password: str


class VerifyOTPRequest(BaseModel):

    email: EmailStr
    otp: str


class LoginRequest(BaseModel):

    email: EmailStr
    password: str
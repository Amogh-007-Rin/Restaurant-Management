from pydantic import BaseModel, Field, EmailStr, field_validator
import re
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Annotated

class Admin(BaseModel):
    username: Annotated[str,Field(pattern=r"^(?=.*[@#])[a-zA-Z0-9@#]+$", description="The admin field must contain one special character(@ or #) and space is not allowed", examples="Admin@123, User#123")]

    email: Annotated[EmailStr, Field(description="Enter your admin email", examples="admin123@gmail.com")]

    phone: Annotated[PhoneNumber, Field(description="Enter Admin Phone number", examples="+44 737263****")]

    password: Annotated[str, Field(description="Enter Admin Password", examples="Admin@123")]


    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one number')
        if not re.search(r'[@$!%*?&]', v):
            raise ValueError('Password must contain at least one special character (@$!%*?&)')
        return v
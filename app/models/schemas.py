from pydantic import BaseModel, Field

class HealthCheckResponse(BaseModel):
    status: str = Field(..., description="The health status of the application")
    uptime: int = Field(..., description="The uptime of the application in seconds")
    version: str = Field(..., description="The current version of the application")


class UserSchema(BaseModel):
    id: int = Field(..., description="The unique identifier of the user")
    username: str = Field(..., description="The username of the user")
    email: str = Field(..., description="The email address of the user")

    class Config:
        orm_mode = True

class UserCreateSchema(BaseModel):
    username: str = Field(..., description="The username of the user")
    email: str = Field(..., description="The email address of the user")

class UserUpdateSchema(BaseModel):
    username: str = Field(None, description="The username of the user")

class UserResponseSchema(BaseModel):
    id: int = Field(..., description="The unique identifier of the user")
    username: str = Field(..., description="The username of the user")
    email: str = Field(..., description="The email address of the user")

    class Config:
        orm_mode = True
"""
Models
O que é: Objetos mapeados da aplicação
O que faz: mapear todos os objetivos que serão tramitados entre as camadas
"""
from pydantic import BaseModel
from typing import Optional

class CreateUserRequest(BaseModel):
    name: str
    password: str
    occupation: int
    area: Optional[str] = None

class UpdateUserRequest(BaseModel):
    name: str
    password: str
    area: str

class UserResponse(BaseModel):
    id: int
    name: str
    occupation: int
    area: str

class UserId(BaseModel):
    id: int
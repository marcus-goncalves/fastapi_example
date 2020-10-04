"""
Routes
O que é: Porta de entrada do sistema, única camada de interação
O que faz: tomada/plugin da aplicação
"""

from fastapi import APIRouter
from users import models

user_routes = APIRouter()

@user_routes.get('/')
async def get_all_users():
    return {'msg': 'Return all users.'}

@user_routes.get('/{id_user}')
async def get_user(id_user: int):
    return {'msg': 'Return userID: {}'.format(id_user)}

@user_routes.post('/')
async def create_user(body: models.CreateUserRequest):
    return {'msg': 'Create user with payload'}

@user_routes.delete('/{id_user}')
async def delete_user(id_user: int):
    return {'msg': 'Delete userID: {}'.format(id_user)}

@user_routes.put('/{id_user}')
async def update_user(id_user: int, body: models.UpdateUserRequest):
    return {'msg': 'Update userID: {}'.format(id_user)}

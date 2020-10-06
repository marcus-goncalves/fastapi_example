"""
Routes
O que é: Porta de entrada do sistema, única camada de interação
O que faz: tomada/plugin da aplicação
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from users import models
from users import services


user_routes = APIRouter()

@user_routes.get('/', response_model=models.UserResponse)
async def get_all_users():
    res = await services.find_all()
    return JSONResponse(content=res)

@user_routes.get('/{id_user}', response_model=models.UserResponse)
async def get_user(id_user: int):
    res = await services.find_one(id_user)
    return JSONResponse(content=res)

@user_routes.post('/', response_model=models.UserId)
async def create_user(body: models.CreateUserRequest):
    res = await services.create_user(body)

    return JSONResponse(content=res, status_code=201)

@user_routes.delete('/{id_user}')
async def delete_user(id_user: int):
    await services.delete_user(id_user)

    return JSONResponse(status_code=202)

@user_routes.put('/{id_user}')
async def update_user(id_user: int, payload: models.UpdateUserRequest):
    await services.update_user(id_user, payload)

    return JSONResponse(status_code=200)

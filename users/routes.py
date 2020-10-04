from fastapi import APIRouter

user_routes = APIRouter()

@user_routes.get('/')
async def get_all_users():
    return {'msg': 'Return all users.'}

@user_routes.get('/{id_user}')
async def get_user(id_user: int):
    return {'msg': 'Return userID: {}'.format(id_user)}

@user_routes.post('/')
async def create_user():
    return {'msg': 'Create user with payload'}

@user_routes.delete('/{id_user}')
async def delete_user(id_user: int):
    return {'msg': 'Delete userID: {}'.format(id_user)}

@user_routes.put('/{id_user}')
async def update_user(id_user: int):
    return {'msg': 'Update userID: {}'.format(id_user)}
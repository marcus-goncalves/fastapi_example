from fastapi import FastAPI
from users import routes as users

app = FastAPI(
    title='FastAPI - Example API',
    description='This API was created to provide an example built in fastapi.',
    version='1.0.0'
)

app.include_router(
    users.user_routes,
    prefix='/users',
    tags=['Users'],
    responses={
        404: {'description': 'Não encontrado'},
        403: {'description': 'Acesso Negado'}
    }
)


@app.get('/', include_in_schema=False)
def root():
    return {'msg': 'Hello World!'}


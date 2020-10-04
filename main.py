import uvicorn

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
        200: {'description': 'OK'},
        201: {'description': 'Created'},
        202: {'description': 'Accepted'},
        204: {'description': 'No Content'},
        403: {'description': 'Forbidden'},
        404: {'description': 'Not found'}
    }
)


@app.get('/', include_in_schema=False)
def root():
    return {'msg': 'Hello World!'}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='info')
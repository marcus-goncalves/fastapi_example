"""
Services
O que é: Camada de validação e regras de negócio
O que faz: integra routes e entities | aplicação de regras de negócio
"""
from users import entities
from fastapi import HTTPException

async def find_all():
    try:
        res = await entities.find_all()
        return res
    except:
        raise HTTPException(status_code=404, detail={'msg': 'Sem Dados'})
    

async def find_one(id_user):
    try:
        res = await entities.find_one(id_user)
        return res
    except:
        raise HTTPException(status_code=404)
    

async def create_user(payload):
    res = await entities.create(payload)
    return res

async def delete_user(id_user):
    res = await entities.delete(id_user)
    return res

async def update_user(id_user, payload):
    new_values = list(dict(payload).values())
    new_values.append(id_user)

    await entities.update(new_values)
    return 'ok'
"""
Entities
O que é: Camada de relacionamento com DB
O que faz: integra com db
"""
import sqlite3
import json
from fastapi import HTTPException

def get_connection():
    conn = sqlite3.connect('db/example.db')
    conn.row_factory = sqlite3.Row
    
    return conn


async def find_all():
    conn = get_connection()
    cur = conn.cursor()

    query = 'SELECT id, name, occupation, area FROM users'
    res = [dict(row) for row in cur.execute(query).fetchall()]

    conn.close()
    return res

async def find_one(id_user):
    conn = get_connection()
    cur = conn.cursor()
    
    query = 'SELECT id, name, occupation, area FROM users WHERE id = {}'.format(id_user)
    res = dict(cur.execute(query).fetchone())

    conn.close()
    return res

async def create(payload):
    conn = get_connection()
    cur = conn.cursor()

    data = list(dict(payload).values())
    query = 'INSERT INTO users (name, password, occupation, area) VALUES (?, ?, ?, ?)'
    res = cur.execute(query, data).lastrowid
    conn.commit()

    conn.close()

    return {'id': res}

async def delete(id_user):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = 'DELETE FROM users WHERE id = {}'.format(id_user)
        res = cur.execute(query).lastrowid
        conn.commit()
        return {'id': res}
    except:
        HTTPException(status_code=404)

async def update(new_values):
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """UPDATE users SET name = ?, password = ?, area = ? WHERE id = ?"""
        cur.execute(query, new_values)
        conn.commit()

        return 'ok'
    except:
        print('deu ruim')
        HTTPException(status_code=403)
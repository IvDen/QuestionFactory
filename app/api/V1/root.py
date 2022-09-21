import asyncio
import datetime

from fastapi import APIRouter, Depends, Request

router = APIRouter(
    responses={404: {'description': 'Not found'}}
)


def my_inj(request: Request):
    return request.state.test


def get_db():
    print('db before yield')
    try:
        yield 'db yield'
    finally:
        print('db after yield')


async def my_coro(time: int, depends=Depends(get_db)):
    await asyncio.sleep(time)


async def first_fx():
    await my_coro(2)
    return


async def second_fx():
    await my_coro(1)
    return


@router.get('/', tags=['root'])
async def root_handler():
    start = datetime.datetime.now()
    done, pending = await asyncio.wait([first_fx(), second_fx()])
    # my_gather = await asyncio.gather(first_fx(), second_fx())
    stop = datetime.datetime.now()
    result = stop - start
    return {'root_handler': [result, pending]}


@router.get('/1', tags=['test_middleware'])
async def root_handler():
    print('im here')
    return {'root_handler': 1}


@router.get('/2', tags=['test_middleware'])
async def root_handler():
    return {'root_handler': 2}
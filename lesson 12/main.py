from tortoise import run_async
import mydb
from aiohttp import ClientSession

API_URL = 'https://randomuser.me/api/'


async def get_json(session, url):
    async with session.get(url) as response:
        return await response.json() if response.status == 200 else None


async def get_users(session, number_of_tries):
    for index in range(1, number_of_tries + 1):
        data = await get_json(session, "https://jsonplaceholder.typicode.com/users/" + str(index))
        print(data)
        if data is None:
            continue
        created_user = mydb.User(
            id=data['id'],
            name=data['name'],
            username=data['username'],
            phone=data['phone'],
            email=data['email'])
        await created_user.save()


async def get_data():
    await mydb.init()
    async with ClientSession() as session:
        await get_users(session, 10)


if __name__ == '__main__':
    run_async(get_data())

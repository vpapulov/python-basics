from tortoise import run_async
import mydb
from aiohttp import ClientSession

API_URL = 'https://randomuser.me/api/'


async def get_json(session, url):
    async with session.get(url) as response:
        return await response.json() if response.status == 200 else None


async def get_data(number_of_tries):
    await mydb.init()
    async with ClientSession() as session:
        for index in range(number_of_tries):
            data_raw = await get_json(session, API_URL)
            if data_raw is None:
                continue
            data = data_raw['results'][0]
            created_user = mydb.User(
                name=(data['name']['first'] + ' ' + data['name']['last']),
                gender=data['gender'],
                age=data['dob']['age'])
            await created_user.save()


if __name__ == '__main__':
    run_async(get_data(10))

    # # 'https://jsonplaceholder.typicode.com/posts/1'
    # # 'https://randomuser.me/api/'
    # done_tasks, pending_tasks = await asyncio.wait([
    #     get_json('https://randomuser.me/api/'),
    #     get_json('https://jsonplaceholder.typicode.com/posts/1'),
    # ])
    #
    # for task in done_tasks:
    #     data = task.result()
    #     break
    # else:
    #     data = None

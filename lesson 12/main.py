from tortoise import run_async
import mydb
from aiohttp import ClientSession

API_URL = 'https://randomuser.me/api/'


async def get_json(session, url):
    async with session.get(url) as response:
        return await response.json() if response.status == 200 else None


async def get_data(numberOfTries):
    await mydb.init()
    async with ClientSession() as session:
        for index in range(numberOfTries):
            dataRaw = await get_json(session, API_URL)
            if dataRaw is None:
                continue
            data = dataRaw['results'][0]
            createdUser = mydb.User(
                name=(data['name']['first'] + ' ' + data['name']['last']),
                gender=data['gender'],
                age=data['dob']['age'])
            await createdUser.save()


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

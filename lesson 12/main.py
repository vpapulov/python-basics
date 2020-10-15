import asyncio
import mydb
from aiohttp import ClientSession

async def get_json(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_data():
    await mydb.init()
    u1 = mydb.User(id=1333, name='Вася', gender='male', age=25)
    await u1.save()

#    data = await get_json('https://randomuser.me/api/')
#    return data


if __name__ == '__main__':
    res = asyncio.run(get_data())
    print(res)



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

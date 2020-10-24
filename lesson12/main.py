from tortoise import run_async
import mydb
from aiohttp import ClientSession


async def get_json(session, url):
    async with session.get(url) as response:
        return await response.json() if response.status == 200 else None


async def get_users(session, number_of_entities):
    for index in range(1, number_of_entities + 1):
        data = await get_json(session, "https://jsonplaceholder.typicode.com/users/" + str(index))
        if data is None:
            continue
        exists = await mydb.User.filter(id=data['id']).exists()
        if not exists:
            user = mydb.User(
                id=data['id'],
                name=data['name'],
                username=data['username'],
                phone=data['phone'],
                email=data['email']
            )
            await user.save()
        else:
            await mydb.User.filter(id=data['id']).update(
                name=data['name'],
                username=data['username'],
                phone=data['phone'],
                email=data['email']
            )


async def get_posts(session, number_of_entities):
    for index in range(1, number_of_entities + 1):
        data = await get_json(session, "https://jsonplaceholder.typicode.com/posts/" + str(index))
        if data is None:
            continue
        exists = await mydb.Post.filter(id=data['id']).exists()
        if not exists:
            post = mydb.Post(
                id=data['id'],
                userId=data['userId'],
                title=data['title'],
                body=data['body']
            )
            await post.save()
        else:
            await mydb.Post.filter(id=data['id']).update(
                userId=data['userId'],
                title=data['title'],
                body=data['body']
            )


async def get_comments(session, number_of_entities):
    for index in range(1, number_of_entities + 1):
        data = await get_json(session, "https://jsonplaceholder.typicode.com/comments/" + str(index))
        if data is None:
            continue
        exists = await mydb.Comment.filter(id=data['id']).exists()
        if not exists:
            comment = mydb.Comment(
                id=data['id'],
                postId=data['postId'],
                name=data['name'],
                email=data['email'],
                body=data['body']
            )
            await comment.save()
        else:
            await mydb.Comment.filter(id=data['id']).update(
                postId=data['postId'],
                name=data['name'],
                email=data['email'],
                body=data['body']
            )


async def get_data():
    await mydb.init()
    async with ClientSession() as session:
        await get_users(session, 10)
        await get_posts(session, 100)
        await get_comments(session, 500)


if __name__ == '__main__':
    run_async(get_data())

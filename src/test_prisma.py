import asyncio
from prisma import Prisma


async def main() -> None:
    db = Prisma(use_dotenv=True)
    await db.connect()

    post = await db.post.create(
        {
            'title': 'Hello from prisma!',
            'desc': 'Prisma is a database toolkit and makes databases easy.',
            'published': True,
        }
    )
    
    print(f'created post: {post.model_dump_json(indent=2)}')
    
    found = await db.post.find_unique(where={'id': post.id})
    if found is None: 
        raise Exception()
    print(f'found post: {found.model_dump_json(indent=2)}')
    
    await db.user.create({
        'username': 'bingo',
        'posts': {
            'create': {
                'title': 'New User',
                'desc': 'I just joined',
                'published': True
            }
        }
    })
    count = await db.post.count();
    assert count is not None
    print(f'found {count} posts')

    result = await db.query_raw('SELECT * FROM post')
    print(result)

    
    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())

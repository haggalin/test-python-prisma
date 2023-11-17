#import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from app.db import connect_db, disconnect_db, db


app = FastAPI()
app.add_event_handler('startup', connect_db)
app.add_event_handler('shutdown', disconnect_db)

@app.get("/")
async def root():
    return {"message": "Hello World"}

class User(BaseModel):
    username: str


@app.post('/user')
async def create_user(req: User):
    await db.post.create({
        "published": True,
        "title": "My title",
        
    })
    user = await db.user.create({
        "username": req.username
    })
    return {"id": user.id}

"""
async def main() -> None:


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

    db.
    
    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())
"""
from prisma import Prisma

db = Prisma(use_dotenv=True)

async def connect_db() -> None:
    await db.connect()

async def disconnect_db() -> None:
    await db.disconnect()
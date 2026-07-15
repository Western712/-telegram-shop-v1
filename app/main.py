import asyncio

from app.bot.loader import bot, dp
from app.handlers.register import register_routers


async def main() -> None:
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

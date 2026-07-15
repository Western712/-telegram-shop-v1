from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("products"))
async def products_handler(message: Message) -> None:
    await message.answer("📦 Список товаров пока пуст")

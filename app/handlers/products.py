from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.connection import async_session
from app.keyboards.products import product_list_keyboard
from app.services.product_service import ProductService

router = Router()


@router.message(Command("products"))
async def products_handler(message: Message) -> None:
    async with async_session() as session:
        service = ProductService(session)
        products = await service.get_products()

    if not products:
        await message.answer("📦 Список товаров пуст")
        return

    await message.answer(
        "📦 Товары магазина:",
        reply_markup=product_list_keyboard(products),
    )

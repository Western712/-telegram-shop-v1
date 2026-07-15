from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import Message

from app.database.connection import async_session
from app.services.product_service import ProductService
from app.states.search import ProductSearch

router = Router()


@router.message(Command("search"))
async def start_search(message: Message, state: FSMContext):
    await state.set_state(ProductSearch.query)
    await message.answer("🔎 Введите название, бренд, артикул или категорию:")


@router.message(ProductSearch.query)
async def search_products(message: Message, state: FSMContext):
    async with async_session() as session:
        products = await ProductService(session).search(message.text)

    if not products:
        await message.answer("❌ Ничего не найдено")
    else:
        result = "\n".join(
            [f"📦 {p.name} | {p.article}" for p in products]
        )
        await message.answer(result)

    await state.clear()

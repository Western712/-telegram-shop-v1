from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.database.connection import async_session
from app.services.product_service import ProductService

router = Router()


@router.callback_query(lambda c: c.data == "cancel_product")
async def cancel_product(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.answer("❌ Создание товара отменено")
    await callback.answer()


@router.callback_query(lambda c: c.data == "save_product")
async def save_product(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()

    async with async_session() as session:
        service = ProductService(session)
        await service.create_product(**data)

    await state.clear()
    await callback.message.answer("✅ Товар успешно добавлен в базу")
    await callback.answer()

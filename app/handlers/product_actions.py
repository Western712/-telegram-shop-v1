from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.states.product import ProductCreation

router = Router()


@router.callback_query(lambda c: c.data == "cancel_product")
async def cancel_product(callback: CallbackQuery, state: FSMContext) -> None:
    await state.clear()
    await callback.message.answer("❌ Создание товара отменено")
    await callback.answer()


@router.callback_query(lambda c: c.data == "save_product")
async def save_product(callback: CallbackQuery, state: FSMContext) -> None:
    data = await state.get_data()
    await state.clear()
    await callback.message.answer(
        "✅ Товар подготовлен к сохранению:\n"
        f"{data}"
    )
    await callback.answer()

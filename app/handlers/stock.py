from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.database.connection import async_session
from app.services.product_service import ProductService
from app.services.stock_service import StockService
from app.states.stock import StockChange

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("stock_in_"))
async def stock_in(callback: CallbackQuery, state: FSMContext):
    await state.update_data(product_id=int(callback.data.split("_")[-1]), operation=1)
    await state.set_state(StockChange.quantity)
    await callback.message.answer("Введите количество прихода:")
    await callback.answer()


@router.callback_query(lambda c: c.data and c.data.startswith("stock_out_"))
async def stock_out(callback: CallbackQuery, state: FSMContext):
    await state.update_data(product_id=int(callback.data.split("_")[-1]), operation=-1)
    await state.set_state(StockChange.quantity)
    await callback.message.answer("Введите количество списания:")
    await callback.answer()


@router.message(StockChange.quantity)
async def change_stock(message: Message, state: FSMContext):
    data = await state.get_data()
    quantity = int(message.text) * data["operation"]

    async with async_session() as session:
        product_service = ProductService(session)
        product = await product_service.get_product(data["product_id"])
        if product:
            await StockService(session).change_stock(product, quantity)

    await state.clear()
    await message.answer("✅ Остаток обновлён")

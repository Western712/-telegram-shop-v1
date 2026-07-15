from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.database.connection import async_session
from app.models.change_log import ChangeLog
from app.services.product_service import ProductService
from app.states.edit_product import ProductEdit

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("edit_"))
async def edit_product(callback: CallbackQuery, state: FSMContext):
    product_id = int(callback.data.split("_")[1])
    await state.update_data(product_id=product_id)
    await state.set_state(ProductEdit.value)
    await callback.message.answer("Введите новое название товара:")
    await callback.answer()


@router.message(ProductEdit.value)
async def save_edit(message: Message, state: FSMContext):
    data = await state.get_data()

    async with async_session() as session:
        product = await ProductService(session).get_product(data["product_id"])

        if product:
            old_name = product.name
            product.name = message.text

            session.add(ChangeLog(
                admin_id=message.from_user.id,
                action="update",
                entity="product",
                details=f"name: {old_name} -> {message.text}",
            ))

            await session.commit()

    await state.clear()
    await message.answer("✅ Товар обновлён")

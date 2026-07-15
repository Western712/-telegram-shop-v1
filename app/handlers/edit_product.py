from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.database.connection import async_session
from app.keyboards.edit_product import edit_fields
from app.models.change_log import ChangeLog
from app.services.product_service import ProductService
from app.states.edit_product import ProductEdit

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("edit_"))
async def edit_product(callback: CallbackQuery, state: FSMContext):
    parts = callback.data.split("_")

    if len(parts) == 2:
        await state.update_data(product_id=int(parts[1]))
        await callback.message.answer(
            "Выберите поле для изменения:",
            reply_markup=edit_fields(int(parts[1])),
        )
    else:
        await state.update_data(
            product_id=int(parts[2]),
            field=parts[1],
        )
        await state.set_state(ProductEdit.value)
        await callback.message.answer("Введите новое значение:")

    await callback.answer()


@router.message(ProductEdit.value)
async def save_edit(message: Message, state: FSMContext):
    data = await state.get_data()

    async with async_session() as session:
        product = await ProductService(session).get_product(data["product_id"])

        if not product:
            await message.answer("❌ Товар не найден")
            return

        field = data["field"]
        old_value = str(getattr(product, field))

        if field == "price":
            product.price = message.text
        elif field in {"name", "brand", "category", "article"}:
            setattr(product, field, message.text)

        session.add(ChangeLog(
            admin_id=message.from_user.id,
            action="update",
            entity="product",
            details=f"{field}: {old_value} -> {message.text}",
        ))

        await session.commit()

    await state.clear()
    await message.answer("✅ Товар обновлён")

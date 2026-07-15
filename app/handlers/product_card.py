from aiogram import Router
from aiogram.types import CallbackQuery

from app.database.connection import async_session
from app.keyboards.product_actions import product_actions
from app.services.product_service import ProductService

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("product_"))
async def product_card(callback: CallbackQuery) -> None:
    product_id = int(callback.data.split("_")[1])

    async with async_session() as session:
        service = ProductService(session)
        product = await service.get_product(product_id)

    if not product:
        await callback.answer("Товар не найден")
        return

    text = (
        f"📦 {product.name}\n\n"
        f"Артикул: {product.article}\n"
        f"Бренд: {product.brand or '-'}\n"
        f"Категория: {product.category or '-'}\n\n"
        f"💰 Цена: {product.price}\n"
        f"📊 Остаток: {product.stock}\n"
        f"Статус: {product.status}"
    )

    await callback.message.answer(
        text,
        reply_markup=product_actions(product.id),
    )
    await callback.answer()

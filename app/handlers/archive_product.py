from aiogram import Router
from aiogram.types import CallbackQuery

from app.database.connection import async_session
from app.services.product_service import ProductService

router = Router()


@router.callback_query(lambda c: c.data and c.data.startswith("archive_"))
async def archive_product(callback: CallbackQuery):
    product_id = int(callback.data.split("_")[1])

    async with async_session() as session:
        product = await ProductService(session).get_product(product_id)

        if not product:
            await callback.answer("Товар не найден")
            return

        product.status = "archived"
        await session.commit()

    await callback.message.answer("🗑 Товар отправлен в архив")
    await callback.answer()

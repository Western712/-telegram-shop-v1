from aiogram import Dispatcher

from app.handlers.start import router as start_router
from app.handlers.products import router as products_router
from app.handlers.add_product import router as add_product_router
from app.handlers.product_actions import router as product_actions_router
from app.handlers.product_card import router as product_card_router


def register_routers(dp: Dispatcher) -> None:
    dp.include_router(start_router)
    dp.include_router(products_router)
    dp.include_router(add_product_router)
    dp.include_router(product_actions_router)
    dp.include_router(product_card_router)

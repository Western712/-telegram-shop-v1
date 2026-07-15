from aiogram import Dispatcher

from app.handlers.start import router as start_router
from app.handlers.products import router as products_router


def register_routers(dp: Dispatcher) -> None:
    dp.include_router(start_router)
    dp.include_router(products_router)

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.states.product import ProductCreation

router = Router()


@router.message(Command("add_product"))
async def add_product_start(message: Message, state: FSMContext) -> None:
    await state.set_state(ProductCreation.name)
    await message.answer("Введите название товара:")


@router.message(ProductCreation.name)
async def product_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(ProductCreation.article)
    await message.answer("Введите артикул:")


@router.message(ProductCreation.article)
async def product_article(message: Message, state: FSMContext) -> None:
    await state.update_data(article=message.text)
    await state.set_state(ProductCreation.brand)
    await message.answer("Введите бренд:")

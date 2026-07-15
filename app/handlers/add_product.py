from decimal import Decimal

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.keyboards.product import product_confirmation
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


@router.message(ProductCreation.brand)
async def product_brand(message: Message, state: FSMContext) -> None:
    await state.update_data(brand=message.text)
    await state.set_state(ProductCreation.category)
    await message.answer("Введите категорию:")


@router.message(ProductCreation.category)
async def product_category(message: Message, state: FSMContext) -> None:
    await state.update_data(category=message.text)
    await state.set_state(ProductCreation.price)
    await message.answer("Введите цену:")


@router.message(ProductCreation.price)
async def product_price(message: Message, state: FSMContext) -> None:
    await state.update_data(price=Decimal(message.text))
    await state.set_state(ProductCreation.stock)
    await message.answer("Введите количество:")


@router.message(ProductCreation.stock)
async def product_stock(message: Message, state: FSMContext) -> None:
    await state.update_data(stock=int(message.text))
    data = await state.get_data()
    await state.set_state(ProductCreation.confirmation)
    await message.answer(
        f"Проверьте товар:\n\n{data}",
        reply_markup=product_confirmation(),
    )

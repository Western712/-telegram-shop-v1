from aiogram.fsm.state import State, StatesGroup


class ProductCreation(StatesGroup):
    name = State()
    article = State()
    brand = State()
    category = State()
    price = State()
    stock = State()
    confirmation = State()

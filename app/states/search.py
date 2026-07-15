from aiogram.fsm.state import State, StatesGroup


class ProductSearch(StatesGroup):
    query = State()

from aiogram.fsm.state import State, StatesGroup


class ProductEdit(StatesGroup):
    value = State()

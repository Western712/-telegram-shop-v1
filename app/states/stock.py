from aiogram.fsm.state import State, StatesGroup


class StockChange(StatesGroup):
    quantity = State()
    comment = State()

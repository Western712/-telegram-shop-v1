from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def admin_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📦 Все товары", callback_data="products")],
            [InlineKeyboardButton(text="➕ Добавить товар", callback_data="add_product")],
            [InlineKeyboardButton(text="📊 Остатки", callback_data="stock")],
            [InlineKeyboardButton(text="🔎 Поиск", callback_data="search")],
        ]
    )

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def edit_fields(product_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝 Название", callback_data=f"edit_name_{product_id}")],
            [InlineKeyboardButton(text="💰 Цена", callback_data=f"edit_price_{product_id}")],
            [InlineKeyboardButton(text="🏷 Бренд", callback_data=f"edit_brand_{product_id}")],
            [InlineKeyboardButton(text="📁 Категория", callback_data=f"edit_category_{product_id}")],
            [InlineKeyboardButton(text="📦 Артикул", callback_data=f"edit_article_{product_id}")],
        ]
    )

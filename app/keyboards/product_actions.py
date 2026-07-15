from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def product_actions(product_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✏️ Редактировать", callback_data=f"edit_{product_id}")],
            [InlineKeyboardButton(text="📊 Изменить остаток", callback_data=f"stock_{product_id}")],
            [InlineKeyboardButton(text="💰 Изменить цену", callback_data=f"price_{product_id}")],
            [InlineKeyboardButton(text="🗑 Архивировать", callback_data=f"archive_{product_id}")],
        ]
    )

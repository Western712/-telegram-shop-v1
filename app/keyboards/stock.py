from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def stock_keyboard(product_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📥 Приход", callback_data=f"stock_in_{product_id}")],
            [InlineKeyboardButton(text="📤 Списание", callback_data=f"stock_out_{product_id}")],
        ]
    )

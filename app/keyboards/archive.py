from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def archive_keyboard(product_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="♻️ Восстановить", callback_data=f"restore_{product_id}")]
        ]
    )

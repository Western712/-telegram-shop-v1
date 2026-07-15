from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def product_confirmation() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ Сохранить", callback_data="save_product")],
            [InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_product")],
        ]
    )

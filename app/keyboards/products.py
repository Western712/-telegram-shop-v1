from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def product_list_keyboard(products) -> InlineKeyboardMarkup:
    buttons = []
    for product in products:
        buttons.append([
            InlineKeyboardButton(
                text=f"{product.name} ({product.stock} шт.)",
                callback_data=f"product_{product.id}",
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)

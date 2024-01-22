from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

proxy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="П", callback_data="0")
        ],
        [
            InlineKeyboardButton(text="Нужна другая локация", callback_data="0"),
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="FAQ", callback_data="0"),
            InlineKeyboardButton(text="Связаться с нами", callback_data="0")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)

top_up_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Криптовалюта 💲", callback_data="0"),
            InlineKeyboardButton(text="Карточка 💳", callback_data="0")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="back")
        ]
    ]
)
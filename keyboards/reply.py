from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прокси")
        ],
        [
            KeyboardButton(text="Помощь")
        ],
        [
            KeyboardButton(text="Пополнить баланс")
        ],
        [
            KeyboardButton(text="Партнёрка")
        ],
        [
            KeyboardButton(text="Мои прокси")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Меню выбора",
    selective=True
)
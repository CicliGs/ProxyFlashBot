from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

proxy_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='П', callback_data="buy_poland")
            ],
            [
                InlineKeyboardButton(text='Нужна другая локация', callback_data="0"),
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Poland', callback_data="buy_poland")
            ],
            [
                InlineKeyboardButton(text='We need another location', callback_data="0"),
                InlineKeyboardButton(text='Back', callback_data="back")
            ]
        ]
    )
}

help_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='FAQ', callback_data="0"),
                InlineKeyboardButton(text='Связаться с нами', url="https://t.me/iproxy_pl")
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='FAQ', callback_data="0"),
                InlineKeyboardButton(text='Contact us', url="https://t.me/iproxy_pl")
            ],
            [
                InlineKeyboardButton(text='Back', callback_data="back")
            ]
        ]
    )
}

top_up_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Криптовалюта 💲', callback_data="cryptocurrency"),
                InlineKeyboardButton(text='Карточка 💳', callback_data="bank_card")
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Cryptocurrency 💲', callback_data="cryptocurrency"),
                InlineKeyboardButton(text='Debit card 💳', callback_data="bank_card")
            ],
            [
                InlineKeyboardButton(text='Back', callback_data="back")
            ]
        ]
    )
}

selecting_proxy_duration_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='1 день (5$)', callback_data="buy_duration_day"),
                InlineKeyboardButton(text='1 неделя (15$)', callback_data="buy_duration_week"),
                InlineKeyboardButton(text='1 месяц (40$)', callback_data="buy_duration_month"),
            ],
            [
                InlineKeyboardButton(text='1 год (??$)', callback_data="buy_duration_year")
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='1 day (5$)', callback_data="buy_duration_day"),
                InlineKeyboardButton(text='1 week (15$)', callback_data="buy_duration_week"),
                InlineKeyboardButton(text='1 month (40$)', callback_data="buy_duration_month"),
            ],
            [
                InlineKeyboardButton(text='1 year (??$)', callback_data="buy_duration_year")
            ],
            [
                InlineKeyboardButton(text='Back', callback_data="back")
            ]
        ]
    )
}
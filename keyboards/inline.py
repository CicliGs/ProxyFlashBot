from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from localization.translations import choose_language, lan

proxy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=choose_language('Польша', lan.getLanguage()), callback_data="buy_poland")
        ],
        [
            InlineKeyboardButton(text=choose_language('Нужна другая локация', lan.getLanguage()), callback_data="0"),
            InlineKeyboardButton(text=choose_language('Назад', lan.getLanguage()), callback_data="back")
        ]
    ]
)

help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=choose_language('FAQ', lan.getLanguage()), callback_data="0"),
            InlineKeyboardButton(text=choose_language('Связаться с нами', lan.getLanguage()), url="https://t.me/iproxy_pl")
        ],
        [
            InlineKeyboardButton(text=choose_language('Назад', lan.getLanguage()), callback_data="back")
        ]
    ]
)

top_up_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=choose_language('Криптовалюта 💲', lan.getLanguage()), callback_data="cryptocurrency"),
            InlineKeyboardButton(text=choose_language('Карточка 💳', lan.getLanguage()), callback_data="bank_card")
        ],
        [
            InlineKeyboardButton(text=choose_language('Назад', lan.getLanguage()), callback_data="back")
        ]
    ]
)

selecting_proxy_duration_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=choose_language('1 день (5$)', lan.getLanguage()), callback_data="buy_duration_day"),
            InlineKeyboardButton(text=choose_language('1 неделя (15$)', lan.getLanguage()), callback_data="buy_duration_week"),
            InlineKeyboardButton(text=choose_language('1 месяц (40$)', lan.getLanguage()), callback_data="buy_duration_month"),
        ],
        [
            InlineKeyboardButton(text=choose_language('1 год (??$)', lan.getLanguage()), callback_data="buy_duration_year")
        ],
        [
            InlineKeyboardButton(text=choose_language('Назад', lan.getLanguage()), callback_data="back")
        ]
    ]
)
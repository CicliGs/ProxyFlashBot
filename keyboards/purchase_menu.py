from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.load_json_config import load_json_config


data = load_json_config()
order = data['order']


selecting_proxy_duration_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{order['order_1']['price']} USDT / {order['order_1']['term_ru']}",
                    callback_data="order_1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_2']['price']} USDT / {order['order_2']['term_ru']}",
                    callback_data="0"
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_3']['price']} USDT / {order['order_3']['term_ru']}",
                    callback_data='0'
                ),
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{order['order_1']['price']} USDT / {order['order_1']['term_en']}",
                    callback_data='order_1'
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_2']['price']} USDT / {order['order_2']['term_en']}",
                    callback_data='order_2'
                )
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_3']['price']} USDT / {order['order_3']['term_en']}",
                    callback_data='order_3'
                )
            ],
            [
                InlineKeyboardButton(text='Back', callback_data="back")
            ],
        ]
    )
}

payment_method_selection = {
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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.load_json_config import load_json_config


data = load_json_config()
order = data['order']

proxy_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Польша', callback_data="buy_country_poland")
            ],
            [
                InlineKeyboardButton(text='Нужна другая локация', url="https://t.me/iproxy_pl"),
                InlineKeyboardButton(text='Назад', callback_data="back")
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Poland', callback_data="buy_country_poland")
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

selecting_proxy_duration_kb = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=f"{order['order_1']['price']} USDT / {order['order_1']['term_ru']}",
                    callback_data='order_1'
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_2']['price']} USDT / {order['order_2']['term_ru']}",
                    callback_data='order_2'
                ),
            ],
            [
                InlineKeyboardButton(
                    text=f"{order['order_3']['price']} USDT / {order['order_3']['term_ru']}",
                    callback_data='order_3'
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

balance_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='5 USDT', callback_data='top_up_5')
        ],
        [
            InlineKeyboardButton(text='10 USDT', callback_data='top_up_10')
        ],
        [
            InlineKeyboardButton(text='20 USDT', callback_data='top_up_20')
        ],
    ]
)

balance = {
    'ru': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Да', callback_data='yes_top_up')
            ],
            [
                InlineKeyboardButton(text='Нет', callback_data='no_top_up')
            ]
        ]
    ),
    'en': InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Yes', callback_data='yes_top_up')
            ],
            [
                InlineKeyboardButton(text='No', callback_data='no_top_up')
            ]
        ]
    )
}
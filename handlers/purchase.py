from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, LabeledPrice, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import purchase_menu
from localization.translations import payment_method_selection, proxy_duration_selection, available_language

from utils.load_json_config import load_json_config
from utils.payment_request import payment_request
from utils.payment_details import payment_details
from config_reader import config

data = load_json_config()
order = data['order']


PRICES = {
    'day': LabeledPrice(label="Подписка на 1 день", amount=100 * 100),
    'week': LabeledPrice(label="Подписка на 1 неделю", amount=1400 * 100),
    'month': LabeledPrice(label="Подписка на 1 месяц", amount=3600 * 100),
    'year': LabeledPrice(label="Подписка на 1 год", amount=38000 * 100)
}

router = Router()


class OrderState(StatesGroup):
    pay_crypto = State()


@router.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    await call.message.delete()


@router.callback_query(F.data == "buy_country_poland")
async def buy_poland(call: CallbackQuery, state: FSMContext):
    await state.update_data(country_proxy='Poland')

    language = available_language(call.from_user.language_code)
    await call.message.edit_text(
        text=proxy_duration_selection[language],
        reply_markup=purchase_menu.selecting_proxy_duration_kb[language]
    )


@router.callback_query(F.data.startswith('order_'))
async def buy_duration(call: CallbackQuery, state: FSMContext):
    language = available_language(call.from_user.language_code)

    await state.update_data(order=call.data)

    await call.message.edit_text(
        text=payment_method_selection[language],
        reply_markup=purchase_menu.payment_method_selection[language]
    )
    await call.answer()


@router.callback_query(F.data == "cryptocurrency")
async def pay_order(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(OrderState.pay_crypto)

    data = await state.get_data()
    lang = available_language(call.from_user.language_code)
    price = order[data['order']]['price']
    await state.update_data(price=price)

    payment_data = payment_request(price, lang)

    await state.update_data(track_id=payment_data['trackId'])

    pay_keyboard = {
        "ru": InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Оплатить", url=payment_data["payLink"]),
                    InlineKeyboardButton(text="Проверить", callback_data="check"),
                ],
            ]
        ),
        "en": InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Pay", url=payment_data["payLink"]),
                    InlineKeyboardButton(text="Check", callback_data="check"),
                ],
            ]
        ),
    }

    pay_text = {
        "ru": "Отлично, теперь оплатите криптовалютой нажав на кнопку, а затем нажмите <b>Проверить</b>. Не подтверждайте оплату пока не оплатите всю сумму указанную на данной странице!",
        "en": "That's excellent, now pay with crypto-currency clicking on button, and then click <b>Check</b>. Don't confirm payment until you pay all the count specified on following page!"
    }

    await call.message.edit_text(
        text=pay_text[lang],
        reply_markup=pay_keyboard[lang],
    )


@router.callback_query(OrderState.pay_crypto, F.data == "check")
async def check_payment(call: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()

    lang = available_language(call.from_user.language_code)

    order = payment_details(data["track_id"], lang)

    price = data['price']

    thanks_text = {
        "ru": "Спасибо за покупку, мы отправили ваш запрос!",
        "en": "Thank for purchase, we sent your request!"
    }

    if order["status"] == "Paid":
        await call.message.edit_text(
            text=thanks_text[lang],
            reply_markup=purchase_menu.pay_keyboard[lang],
        )

        await bot.send_message(
            config.admin_id.get_secret_value(),
            f"Пользователь @{call.from_user.username} с id {call.from_user.id} оплатил {price} USDT за прокси {data['country_proxy']}"
        )
        await state.clear()
    else:
        sorry_text = {
            "ru": "Извините, вы не оплатили покупку :(",
            "en": "Sorry, you haven't pay :("
        }
        await call.answer(text=sorry_text[lang], show_alert=True)
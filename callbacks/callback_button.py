from aiogram import Router, F, Bot, types
from aiogram.types import CallbackQuery, LabeledPrice
from keyboards import inline
from config_reader import config
from localization.translations import choose_language

router = Router()
PRICES = {
    'day': LabeledPrice(label="Подписка на 1 день", amount=100*100),
    'week': LabeledPrice(label="Подписка на 1 неделю", amount=1400*100),
    'month': LabeledPrice(label="Подписка на 1 месяц", amount=3600*100),
    'year': LabeledPrice(label="Подписка на 1 год", amount=38000*100)
}


class Constants:
    country_proxy: str = 'None'
    duration_proxy: int = 0
    payment_method: str = 'None'
    language: str = 'en'


@router.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    await call.message.delete()


@router.callback_query(F.data == "buy_poland")
async def buy_poland(call: CallbackQuery):
    Constants.country_proxy = 'Poland'
    Constants.language = call.from_user.language_code
    await call.message.edit_text(
        choose_language('Выберите длительность работы прокси:', Constants.language),
        reply_markup=inline.selecting_proxy_duration_kb[Constants.language]
    )


@router.callback_query(F.data == "buy_duration_day") #Покупка на определённый срок
async def buy_day_answer(call: CallbackQuery):
    call.message.from_user.language_code
    Constants.duration_proxy = 1
    await call.message.edit_text(
        choose_language('Выберите способ оплаты:', Constants.language),
        reply_markup=inline.top_up_kb[Constants.language]
    )
    await call.answer()


@router.callback_query(F.data == "buy_duration_week")
async def buy_week_answer(call: CallbackQuery):
    Constants.duration_proxy = 7
    await call.message.edit_text(
        choose_language('Выберите способ оплаты:', Constants.language),
        reply_markup=inline.top_up_kb[Constants.language]
    )
    await call.answer()


@router.callback_query(F.data == "buy_duration_month")
async def buy_week_answer(call: CallbackQuery):
    Constants.duration_proxy = 30
    await call.message.edit_text(
        choose_language('Выберите способ оплаты:', Constants.language),
        reply_markup=inline.top_up_kb[Constants.language]
    )
    await call.answer()


@router.callback_query(F.data == "buy_duration_year")
async def buy_week_answer(call: CallbackQuery):
    Constants.duration_proxy = 365
    await call.message.edit_text(
        choose_language('Выберите способ оплаты:', Constants.language),
        reply_markup=inline.top_up_kb[Constants.language]
    )
    await call.answer()


@router.callback_query(F.data == "bank_card")
async def buy(call: CallbackQuery, bot: Bot):
    await buy_proxy(Constants.country_proxy, Constants.duration_proxy, bot, call)


@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: types.Message, bot: Bot):
    if Constants.country_proxy == "Poland":
        if Constants.duration_proxy == 1:
            print("Some")
            # Выдача ключа будет происходить здесь
            # формат Ip:port:login:password
        elif Constants.duration_proxy == 30:
            ...
    print("SUCCESSFUL PAYMENT")
    await bot.send_message(
        message.chat.id,
        f"Платёж на сумму {message.successful_payment.total_amount // 100}{message.successful_payment.currency} прошел успешно!"
    )

async def buy_proxy(country: str, duration: int, bot: Bot, call: CallbackQuery):
    if config.payment_token_test.get_secret_value().split(":")[1] == 'TEST':
        await bot.send_message(call.message.chat.id, "Тестовый платёж!!!")
    if duration == 1:
        prices_ = PRICES.get('day')
        start_parameter_ = 'one-day-subscription'
        photo_url_ = 'https://raw.githubusercontent.com/CicliGs/Multiuser_chat/main/images/%D0%9E%D0%B4%D0%B8%D0%BD%20%D0%B3%D0%BE%D0%B4.png'
    elif duration == 7:
        prices_ = PRICES.get('week')
        start_parameter_ = 'one-week-subscription'
    elif duration == 30:
        prices_ = PRICES.get('month')
        start_parameter_ = 'one-month-subscription'

    await bot.send_invoice(call.message.chat.id,
                           title="Покупка прокси сервера",
                           description="Аренда прокси сервера с регионом " + country + " на " + str(duration) + " дней",
                           provider_token=config.payment_token_test.get_secret_value(),
                           currency="RUB",
                           #photo_url="https://telegram.org/file/400780400534/4/4SMmJ6f4F1E.573667/b64e65fb46f54267aa",
                           photo_url=photo_url_,
                           photo_width=416,
                           photo_height=234,
                           is_flexible=False,
                           prices=[prices_],
                           start_parameter=start_parameter_,
                           payload="test-invoice-payload"
                           )
    await call.message.delete()
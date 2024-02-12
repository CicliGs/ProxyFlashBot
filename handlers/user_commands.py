from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold
from localization.translations import choose_language, welcome_message_1, welcome_message_2, available_language
from config_reader import config
from database.models import User, Proxy
from database.methods.create import add_new_user, add_new_proxy
from database.methods.get import get_user_by_id, get_proxy_by_user_id
from database.methods.delete import check_subscription_proxy
import datetime
import time
import threading

from keyboards import inline

router = Router()
language: str


def get_current_time() -> datetime:
    delta = datetime.timedelta(hours=3, minutes=0)
    return datetime.datetime.now(datetime.timezone.utc) + delta


def syb(id):
    while True:
        check_subscription_proxy(id)
        time.sleep(3600)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")
    global language
    language = available_language(message.from_user.language_code)

    user = User(message.from_user.id, None, message.from_user.language_code)
    add_new_user(user)

    new_thread = threading.Thread(target=syb(message.from_user.id))
    new_thread.start()

    await message.answer(welcome_message_1[language])
    await message.answer(welcome_message_2[language])


@router.message(Command("proxy"))
async def proxy(message: Message) -> None:
    global language
    language = message.from_user.language_code
    await message.answer(
        choose_language('Выберите регион:', language),
        reply_markup=inline.proxy_kb[language]
    )


@router.message(Command("help"))
async def help(message: Message) -> None:
    global language
    language = message.from_user.language_code
    await message.answer(
        choose_language('Выберите необходимый вариант:', language),
        reply_markup=inline.help_kb[language]
    )


@router.message(Command("affiliate"))
async def affiliate(message: Message) -> None:
    global language
    language = message.from_user.language_code
    await message.answer(
        choose_language('Данная функция пока в разработке...', language)
    )


@router.message(Command("my_proxy"))
async def my_proxy(message: Message) -> None:
    global language
    language = message.from_user.language_code

    proxy = get_proxy_by_user_id(message.from_user.id)
    text: str = None
    if isinstance(proxy, Proxy):
        print(proxy)
        text = f"{proxy.country}: {proxy.proxy}"
    else:
        text = ',\n'.join('{}: {}'.format(x.country, y.proxy) for x, y in zip(proxy, proxy))

    if text is not None:
        await message.answer(
            text=choose_language('Ваши прокси:\n', language)+text
        )
    else:
        await message.answer(choose_language('У вас нет прокси :(', language))


@router.message(Command("send_message"))
async def send_command(message: Message, bot: Bot) -> None:
    if str(message.from_user.id) == str(config.admin_id.get_secret_value()):
        args = message.text.split()
        print(args)

        target_id = args[1]
        country_proxy = args[2]
        target_proxy = args[3]
        duration_proxy = args[4]

        await bot.send_message(target_id, f"Ваш прокси с регионом {country_proxy}: {target_proxy} на {duration_proxy} дней")

        current_date = datetime.datetime.now().strftime("%d.%m.%y")
        end_date = datetime.datetime.now() + datetime.timedelta(days=duration_proxy)
        formatted_tomorrow = end_date.strftime("%d.%m.%y")

        proxy = Proxy(target_id, country_proxy, target_proxy, current_date, end_date, get_current_time())
        add_new_proxy(proxy)

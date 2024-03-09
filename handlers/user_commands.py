from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold
from localization.translations import choose_language, welcome_message_1, welcome_message_2, welcome_message_3, available_language
from config_reader import config
from database.models import User, Proxy
from database.methods.create import add_new_user, add_new_proxy
from database.methods.get import get_user_by_id, get_proxy_by_user_id
from database.methods.delete import check_subscription_proxy
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
from utils import apsched

from keyboards import inline

router = Router()
language: str


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")
    global language
    language = available_language(message.from_user.language_code)
    if language != 'ru' and language != 'en':
        language = 'en'

    user = get_user_by_id(message.from_user.id)
    if user is None:
        user = User(message.from_user.id, None, language, 0.0)
        add_new_user(user)

    await message.answer(welcome_message_1[language])
    await message.answer(welcome_message_2[language])
    await message.answer(welcome_message_3[language])


@router.message(Command("proxy"))
async def proxy(message: Message) -> None:
    user = get_user_by_id(message.from_user.id)
    language = user.language
    await message.answer(
        choose_language('Выберите регион:', language),
        reply_markup=inline.proxy_kb[language]
    )


@router.message(Command("help"))
async def help(message: Message) -> None:
    user = get_user_by_id(message.from_user.id)
    language = user.language
    await message.answer(
        choose_language('Выберите необходимый вариант:', language),
        reply_markup=inline.help_kb[language]
    )


@router.message(Command("affiliate"))
async def affiliate(message: Message) -> None:
    await message.answer(
        choose_language('Данная функция пока в разработке...', language)
    )


@router.message(Command("profile"))
async def my_profile(message: Message) -> None:
    user = get_user_by_id(message.from_user.id)
    language = ''
    answer = ''
    if user.language == 'ru':
        language = 'ru🇷🇺'
        answer = f'Мой профиль👤🪪:\n' + f'🆔: {user.user_id}\n' + f'🌐Язык: {language}\n\n' + f'💵Баланс: {user.balance} USDT'
    else:
        language = 'en🇬🇧'
        answer = f'My profile👤🪪:\n' + f'🆔: {user.user_id}\n' + f'🌐Language: {language}\n\n' + f'💵Balance: {user.balance} USDT'

    await message.answer(
        answer
    )


@router.message(Command("my_proxy"))
async def my_proxy(message: Message, bot: Bot) -> None:
    result = check_subscription_proxy(message.from_user.id)
    user = get_user_by_id(message.from_user.id)
    language = user.language

    for i in result:
        await bot.send_message(
            config.admin_id.get_secret_value(),
            f"Необходимо удалить прокси {i.proxy}"
        )

    proxy = get_proxy_by_user_id(message.from_user.id)
    if not proxy:
        await message.answer(choose_language('У вас нет прокси :(', language))
    else:
        text: str = None
        if isinstance(proxy, Proxy):
            text = f"{proxy.country}: {proxy.proxy}"
        else:
            text = ',\n'.join('{}: {}'.format(x.country, y.proxy) for x, y in zip(proxy, proxy))

        if text is not None:
            await message.answer(
                text=choose_language('Ваши прокси:\n', language) + text
            )
        else:
            await message.answer(choose_language('У вас нет прокси :(', language))


@router.message(Command("send_message"))
async def send_command(message: Message, bot: Bot, apscheduler: AsyncIOScheduler) -> None:
    if str(message.from_user.id) == str(config.admin_id.get_secret_value()):
        language = message.from_user.language_code
        args = message.text.split()

        target_id = args[1]
        country_proxy = args[2]
        target_proxy = args[3]
        duration_proxy = args[4]

        await bot.send_message(target_id,
                               f"Ваш прокси с регионом {country_proxy}: {target_proxy} на {duration_proxy} дней")

        current_date = datetime.datetime.now().strftime("%d.%m.%y")
        end_date = datetime.datetime.now() + datetime.timedelta(hours=3)
        formatted_end_date = end_date.strftime("%d.%m.%y")
        time = (datetime.datetime.fromisoformat(str(message.date)) + datetime.timedelta(hours=3)).time()

        proxy = Proxy(target_id, country_proxy, target_proxy, current_date, formatted_end_date, time)
        add_new_proxy(proxy)

        apscheduler.add_job(apsched.send_message_time, trigger='date',
                            run_date=datetime.datetime.now()
                                     + datetime.timedelta(hours=(int(duration_proxy) * 24))
                                     + datetime.timedelta(minutes=3),
                            kwargs={'bot': bot, 'target_proxy': target_proxy,
                                    'country_proxy': country_proxy, 'language': language})

        apscheduler.add_job(apsched.send_message_end, trigger='date',
                            run_date=datetime.datetime.now()
                                     + datetime.timedelta(hours=(int(duration_proxy) * 24))
                                     + datetime.timedelta(minutes=3),
                            kwargs={'bot': bot, 'target_id': target_id, 'target_proxy': target_proxy,
                                    'country_proxy': country_proxy, 'language': language})

        apscheduler.add_job(apsched.delete_proxy, trigger='date',
                            run_date=datetime.datetime.now()
                                     + datetime.timedelta(hours=(int(duration_proxy) * 24))
                                     + datetime.timedelta(minutes=3),
                            kwargs={'target_id': target_id})

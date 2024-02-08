from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold
from localization.translations import choose_language, welcome_message_1, welcome_message_2, available_language
from config_reader import config

from keyboards import inline

router = Router()
language: str


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")
    global language
    language = available_language(message.from_user.language_code)
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
    await message.answer(
        choose_language('Данная функция пока в разработке...', language)
    )


@router.message(Command("send_message"))
async def send_command(message: Message, bot: Bot) -> None:
    if str(message.from_user.id) == str(config.admin_id.get_secret_value()):
        args = message.text.split()
        print(args)

        target_id = args[1]
        country_proxy = args[2]
        target_proxy = args[3]

        await bot.send_message(target_id, f"Ваш прокси с регионом {country_proxy}: {target_proxy}")

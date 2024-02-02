from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import hbold
from localization.translations import choose_language

from keyboards import inline

router = Router()
language: str


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")
    global language
    language = message.from_user.language_code


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
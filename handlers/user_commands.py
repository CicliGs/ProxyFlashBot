from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.utils.markdown import hbold
from localization.translations import choose_language, lan

from keyboards import reply, inline

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")
    print(message.from_user.language_code)
    lan.setLanguage(message.from_user.language_code)


@router.message(Command("proxy"))
async def proxy(message: Message) -> None:
    print(lan.getLanguage())
    lan.setLanguage(message.from_user.language_code)
    await message.answer(
        choose_language('Выберите регион:', lan.getLanguage()),
        reply_markup=inline.proxy_kb
    )


@router.message(Command("help"))
async def help(message: Message) -> None:
    await message.answer(
        choose_language('Выберите необходимый вариант:', lan.getLanguage()),
        reply_markup=inline.help_kb
    )


@router.message(Command("affiliate"))
async def affiliate(message: Message) -> None:
    await message.answer(
        choose_language('Данная функция пока в разработке...', lan.getLanguage())
    )


@router.message(Command("my_proxy"))
async def my_proxy(message: Message) -> None:
    await message.answer(
        choose_language('Данная функция пока в разработке...', lan.getLanguage())
    )
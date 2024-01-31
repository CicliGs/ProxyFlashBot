from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.utils.markdown import hbold

from keyboards import reply, inline

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.username)}!")


@router.message(Command("proxy"))
async def proxy(message: Message) -> None:
    await message.answer("Выберите регион:", reply_markup=inline.proxy_kb)


@router.message(Command("help"))
async def help(message: Message) -> None:
    await message.answer("Выберите необходимый вариант:", reply_markup=inline.help_kb)


@router.message(Command("affiliate"))
async def affiliate(message: Message) -> None:
    await message.answer("Данная функция пока в разработке...")


@router.message(Command("my_proxy"))
async def my_proxy(message: Message) -> None:
    await message.answer("Данная функция пока в разработке...")
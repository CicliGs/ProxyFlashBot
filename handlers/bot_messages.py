from aiogram import Router, F
from aiogram.types import Message

from keyboards import inline

router = Router()

@router.message()
async def echo(message: Message) -> None:
    msg = message.text.lower()

    if msg == "прокси":
        await message.answer("Выберите регион:", reply_markup=inline.proxy_kb)
        await message.delete()
    elif msg == "помощь":
        await message.answer("Выберите необходимый вариант:", reply_markup=inline.help_kb)
        await message.delete()
    elif msg == "пополнить баланс":
        await message.answer("Выберите спрособ оплаты:", reply_markup=inline.top_up_kb)
        await message.delete()
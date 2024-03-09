from aiogram import Router, F
from aiogram.types import Message

from database.methods.get import get_user_by_id
from keyboards import inline
from keyboards.inline import balance
from utils import const
from aiogram.fsm.context import FSMContext

router = Router()


@router.message()
async def echo(message: Message, state: FSMContext) -> None:
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
    elif float(msg):
        user = get_user_by_id(message.from_user.id)
        const.temp = float(msg)
        await state.update_data(price=const.temp)

        answer = ''
        if user.language == 'ru':
            answer = f'Ваш текущий баланс {user.balance} USDT. Желаете ли вы пополнить его на {float(msg)} USDT?'
        else:
            answer = f'Your current balance is {user.balance} USDT. Would you like to replenish it by {float(msg)} USDT?'

        await message.answer(answer, reply_markup=balance[user.language])

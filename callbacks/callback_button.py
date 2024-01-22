from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import reply

router = Router()

@router.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("", reply_markup=reply.main_kb)
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import bot_messages, user_commands, purchase
from localization.translations import bot_commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import apsched
from datetime import datetime, timedelta
from utils.apschedulermiddleware import SchedulerMiddleware

from config_reader import config


async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.start()
    dp.update.middleware.register(SchedulerMiddleware(scheduler))

    # await bot.set_my_commands(commands=bot_commands['ru'], language_code='ru')
    # await bot.set_my_commands(commands=bot_commands['en'], language_code='en')
    dp.include_routers(
        purchase.router,
        user_commands.router,
        bot_messages.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

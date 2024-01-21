import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import bot_messages, user_commands
from callbacks import callback_button

from config_reader import config

async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        callback_button.router,
        bot_messages.router
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
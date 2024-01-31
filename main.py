import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from handlers import bot_messages, user_commands
from callbacks import callback_button

from config_reader import config

bot_commands = [
    BotCommand(command="/proxy", description="Купить прокси"),
    BotCommand(command="/help", description="Помощь"),
    BotCommand(command="/affiliate", description="Партнёрская программа"),
    BotCommand(command="/my_proxy", description="Мои прокси")
]


async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await bot.set_my_commands(bot_commands)
    dp.include_routers(
        user_commands.router,
        callback_button.router,
        bot_messages.router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
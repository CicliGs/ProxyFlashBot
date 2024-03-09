from aiogram import Bot
from config_reader import config
from database.methods.delete import check_subscription_proxy


async def send_message_time(bot: Bot, target_proxy: str, country_proxy: str, language):
    answer = f'Необходимо отключить прокси {target_proxy} ({country_proxy})'
    # if language == 'ru':
    #     answer = f'Необходимо отключить прокси {target_proxy} ({country_proxy})'
    # else:
    #     answer = f'Proxy {target_proxy} ({country_proxy}) must be disabled'
    await bot.send_message(config.admin_id.get_secret_value(), answer)


async def send_message_end(bot: Bot, target_id, target_proxy, country_proxy, language):
    answer = ''
    if language == 'ru':
        answer = f'Ваш прокси {target_proxy} с регионом {country_proxy} закончился'
    else:
        answer = f'Your proxy {target_proxy} with region {country_proxy} has expired'

    await bot.send_message(target_id, answer)


async def delete_proxy(target_id):
    check_subscription_proxy(target_id)


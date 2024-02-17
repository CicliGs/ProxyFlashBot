import mysql.connector

from aiogram import Bot
from database.models import User, Transaction, Proxy
from database.methods.get import get_proxy_by_user_id
import datetime
from config_reader import config


def get_current_time() -> datetime:
    delta = datetime.timedelta(hours=3, minutes=0)
    return datetime.datetime.now(datetime.timezone.utc) + delta


def check_subscription_proxy(id):  # Проверка подписки прокси, передеётся id пользователя
    proxy = get_proxy_by_user_id(id)

    current_date = datetime.datetime.now() + datetime.timedelta(hours=3)

    delete_proxy_id = []  # id удаляемых прокси
    delete_proxy = []

    if isinstance(proxy, Proxy):
        end_proxy_date = datetime.datetime.strptime(proxy.end_proxy_date + ' ' + proxy.time, '%d.%m.%y %H:%M:%S')
        if current_date >= end_proxy_date:
            delete_proxy.append(proxy)
            delete_proxy_id.append(proxy.id)
            # Отправить сообщение о удалении админу

    else:
        for x in proxy:
            end_proxy_date = datetime.datetime.strptime(x.end_proxy_date + ' ' + x.time, '%d.%m.%y %H:%M:%S')
            if current_date > end_proxy_date:
                delete_proxy.append(x)
                delete_proxy_id.append(x.id)

    return delete_proxy

    for i in delete_proxy_id:
        delete_proxy_by_user_id(i)


def delete_proxy_by_user_id(id):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    delete_query = "DELETE FROM proxy WHERE id = %s"

    cursor.execute(delete_query, (id,))

    connection.commit()
    connection.close()

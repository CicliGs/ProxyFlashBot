import mysql.connector

from database.models import User, Proxy, Transaction
from config_reader import config


def add_new_user(user: User):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO users (id, referrer_id, language, balance) VALUES (%s, %s, %s, %s);
    """

    cursor.execute(insert_query, (user.user_id, user.referrer_id, user.language, user.balance))

    connection.commit()
    connection.close()


def add_new_proxy(proxy: Proxy):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO proxy (user_id, country, proxy, start_proxy_date, end_proxy_date, time) 
        VALUES (%s, %s, %s, %s, %s, %s);
    """

    cursor.execute(
        insert_query,
        (proxy.user_id, proxy.country, proxy.proxy, proxy.start_proxy_date, proxy.end_proxy_date, proxy.time)
    )

    connection.commit()
    connection.close()


def add_new_transaction(tr: Transaction):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    insert_query = """
        INSERT INTO transactions (user_id, payment_amount, track_id, transaction_date, transaction_time)
        VALUES (%s, %s, %s, %s, %s);
    """

    cursor.execute(
        insert_query,
        (tr.user_id, tr.payment_amount, tr.track_id, tr.transaction_date, tr.transaction_time)
    )

    connection.commit()
    connection.close()

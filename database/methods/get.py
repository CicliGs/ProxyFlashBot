import mysql.connector

from database.models import User, Transaction, Proxy
from config_reader import config


def get_user_by_id(id) -> User:
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    query = """
        SELECT * FROM users WHERE id = %s
    """
    cursor.execute(query, (id,))
    res = cursor.fetchall()

    connection.commit()
    connection.close()

    user = User(res[0][0], res[0][1], res[0][2])

    return user


def get_transactions_by_user_id(id):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    query = """
        SELECT * FROM transactions WHERE user_id = %s
    """
    cursor.execute(query, (id,))
    res = cursor.fetchall()

    connection.commit()
    connection.close()

    tmp = []
    for x in res:
        transaction = Transaction(res[1], res[2], res[3], res[4], res[5])
        transaction.id = res[0]
        tmp.append(transaction)

    return tmp


def get_proxy_by_user_id(id):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    query = """
        SELECT * FROM proxy WHERE user_id = %s
    """
    cursor.execute(query, (id,))
    res = cursor.fetchall()

    connection.commit()
    connection.close()

    tmp = []
    for x in res:
        proxy = Proxy(res[1], res[2], res[3], res[4], res[5], res[6])
        proxy.id = res[0]
        tmp.append(proxy)

    return tmp

import mysql.connector

from database.models import User
from config_reader import config


def update_user_by_user_id(user: User):
    connection = mysql.connector.connect(
        user=config.db_user_name.get_secret_value(),
        password=config.db_password.get_secret_value(),
        host=config.db_host.get_secret_value(),
        database=config.db_database.get_secret_value()
    )
    cursor = connection.cursor()

    query = """
        UPDATE users SET balance = %s WHERE id = %s
    """

    cursor.execute(query, (user.balance, user.user_id))
    res = cursor.fetchall()

    connection.commit()
    connection.close()

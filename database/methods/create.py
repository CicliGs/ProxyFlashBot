import mysql.connector

from database.models import User
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
        INSERT INTO users (id, referrer_id, language) VALUES (%s, %s, %s);
    """

    cursor.execute(insert_query, (user.user_id, user.referrer_id, user.language))

    connection.commit()
    connection.close()

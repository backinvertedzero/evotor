import pymysql
from connect import get_connection



def get_user_credentials(user_id: int, connection) -> dict:
    #connection = get_connection()

    with connection.cursor() as cursor:
        select_all_rows = f"SELECT * FROM `users` WHERE id = '{user_id}'"
        cursor.execute(select_all_rows)

        row = cursor.fetchone()
        return {'id': row['evator_token'], 'store_id': row['evator_store_id']}

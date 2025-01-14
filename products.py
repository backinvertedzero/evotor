
def get_evotor_products_data(evator_product_id: str, connection) -> dict:
    with connection.cursor() as cursor:
        select_all_rows = f"SELECT * FROM `evator_products` WHERE evator_product_id = '{evator_product_id}'"
        cursor.execute(select_all_rows)

        row = cursor.fetchone()
        if row is not None:
            return {'id': row['id'], 'user_id': row['user_id'], 'product_id': row['product_id']}
        else:
            return {}

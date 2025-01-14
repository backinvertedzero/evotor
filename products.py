
def get_evotor_products_data(evator_product_id: str, connection) -> dict:
    with connection.cursor() as cursor:
        select_all_rows = f"SELECT * FROM `evator_products` WHERE evator_product_id = '{evator_product_id}'"
        cursor.execute(select_all_rows)

        row = cursor.fetchone()
        if row is not None:
            return {'id': row['id'], 'user_id': row['user_id'], 'product_id': row['product_id']}
        else:
            return {}

def get_evotor_products_data_by_list(evator_products: list, connection) -> list:
    data = []

    for product in evator_products:
        x = get_evotor_products_data(product['id'], connection)
        id = x['id'] if 'id' in x else None
        data.append({'pid': product['id'], 'id': id, 'pname': product['name']})

    return sorted(data,  key=lambda k:  (k['id'] is None, k['id'] == 0, k['id']), reverse=False)


def delete_product_from_db(id: int, connection):
    with connection.cursor() as cursor:
        sql = f"DELETE FROM `evator_products` WHERE id = '{id}'"
        cursor.execute(sql)
    connection.commit()
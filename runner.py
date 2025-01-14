from users import get_user_credentials
from evotor_requests import get_all_products, delete_product
from service import get_duplicates, get_by_title
from connect import get_connection
from products import delete_product_from_db, get_evotor_products_data_by_list
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    connection = get_connection()
    creds = get_user_credentials(user_id=user_id, connection=connection)

    products = get_all_products(creds['id'], creds['store_id'])
    duplicates = get_duplicates(products)

    for item in duplicates:
        x = get_by_title(item, products)
        y = get_evotor_products_data_by_list(x, connection)
        z = y[1:]
        for q in z:
            pid = q['pid']
            id = q['id']
            # delete_product(creds['id'], creds['store_id'], pid)
            if id is not None:
                # delete_product_from_db(id, connection)
                pass
            print(f"{pid}: {id}")
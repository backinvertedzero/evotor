from users import get_user_credentials
from evotor_requests import get_all_products
from service import get_duplicates, get_by_title
from connect import get_connection
from products import get_evotor_products_data
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    connection = get_connection()
    creds = get_user_credentials(user_id=user_id, connection=connection)

    products = get_all_products(creds['id'], creds['store_id'])
    duplicates = get_duplicates(products)

    for item in duplicates:
        x = get_by_title(item, products)

        for it in x:
            z = get_evotor_products_data(it['id'], connection)
            print(f"{it['name']}, {it['id']}")
            if z is not None:
                #print(z)
                pass

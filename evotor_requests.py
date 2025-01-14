import httpx

API_URL = 'https://api.evotor.ru/stores/'


def get_all_products(id: str, store_id: str) -> list:
    products_url = API_URL + store_id + '/products'

    headers = {'X-Authorization': id}

    r = httpx.get(products_url, headers=headers)

    data = r.json()

    if not data['items']:
        raise Exception("Can not items")


    return data['items']

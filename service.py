from collections import defaultdict, Counter

def get_duplicates(products: list) -> dict:
    counter = {}

    for elem in products:
        counter[elem['name']] = counter.get(elem['name'], 0) + 1

    doubles = {element: count for element, count in counter.items() if count > 1}

    return doubles



def get_by_title(title: str, products: list) -> list:
    data = []

    for elem in products:
        if elem['name'] == title:
            data.append(elem)

    return data
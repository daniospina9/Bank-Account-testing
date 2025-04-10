def calculate_total(products, discount):
    total = 0
    for product in products:
        total += product["price"]
    return total - discount

def test_calculate_total_with_empty_list():
    assert calculate_total([], 0) == 0

def test_calculate_total_with_single_product():
    products = [
        {
            "name": "Notebooks", "price": 5
        }
    ]
    assert calculate_total(products, 0) == 5

def test_calculate_total_with_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products, 0) == 12

def test_calculate_total_with_descount_zero_and_empty_list():
    assert calculate_total([], 0) == 0

def test_calculate_total_with_descount_greater_zero_and_empty_list():
    assert calculate_total([], 1) == -1

def test_calculate_total_with_descount_zero_and_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products, 0) == 12

def test_calculate_total_with_descount_greater_zero_and_multiple_product():
    products = [
        {
            "name": "Book", "price": 10
        },
        {
            "name": "Pen", "price": 2
        }
    ]
    assert calculate_total(products, 1) == 11
    


if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
    test_calculate_total_with_descount_zero_and_empty_list()
    test_calculate_total_with_descount_greater_zero_and_empty_list()
    test_calculate_total_with_descount_zero_and_multiple_product()
    test_calculate_total_with_descount_greater_zero_and_multiple_product()
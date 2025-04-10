lista = [1,2,3,4,5]

new_dict = [
    {
        "name": "pet", "price": 12, "discount": 30
    },
    {
        "name": "pencil", "price": 8, "discount": 0
    },
    {
        "name": "book", "price": 15, "discount": 45
    }
]
people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

def print_values():
    for person in new_dict:
        print('discount =>', person['discount'])




def filter_numbers():
    new_numbers = list(filter(lambda x: x % 2 == 0, lista))
    print(new_numbers)


if __name__ == "__main__":
    filter_numbers()
    print_values()
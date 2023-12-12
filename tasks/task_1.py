data_types = [
    1852, 12.43, True, 4 + 3j, "Bravo!",
    (13, -5), 3.5e10, 100.95, "abcdef",
    [21, 49], {"name": 'Micky', "age": 17}
]

for items in data_types:
    if not isinstance(items, (float, str)):
        print("Элемент: ", items, "Тип:", type(items))

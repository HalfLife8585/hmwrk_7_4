def common_elements():
    # Генеруємо список чисел, кратних 3
    multiples_of_3 = set(i for i in range(100) if i % 3 == 0)

    # Генеруємо список чисел, кратних 5
    multiples_of_5 = set(i for i in range(100) if i % 5 == 0)

    # Знаходимо перетин двох множин
    common = multiples_of_3.intersection(multiples_of_5)

    return common


# Перевірка
assert common_elements() == {0, 15, 30, 45, 60, 75, 90}, "Test failed"
print("Test passed successfully!")
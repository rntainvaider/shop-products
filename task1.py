def generate_subsequence(number: int) -> list[int]:
    numbers = list()

    for item in range(1, number):
        numbers.extend([item] * item)
    return numbers[:number]


number = int(input("Введите количество элементов последоватиельности "))
result = generate_subsequence(number)

print(f"Первые {number} элементов последовательности: {result}")

def generate_even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num = num + 2

even = generate_even_numbers(4)

for num in even:
    print(num)


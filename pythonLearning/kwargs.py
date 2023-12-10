def print_details(**kwargs):
    print(f"kwargs : {kwargs}")
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Jill", age=23, city="Raccoon city")
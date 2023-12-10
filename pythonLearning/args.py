# positional first then variable arguments
# no keyword argument before positional argument
# postional , args, keywords

def calculate(*args):
    total = 0
    for num in args:
        total = total + num
    return total

result = calculate(1, 2, 3)
print(result)

# or

def calculate1(*args):
    return sum(args)

result = calculate1(1, 2, 3, 4)
print(result)

def animal_names(species, *names):
    names_str = ",".join(names)
    message = f"{species} names: {names_str}"
    return message

result = animal_names("Cat", "Whiskers", "Mittens")  # unpacking the list
print(result)

# unpacking list

def animal_names(animal_type, *names, habitat="Unknown"):
    animal_list = ",".join(names)
    description = f"The {animal_type} animals in the {habitat} habitat are: {animal_list}"
    return description
result = animal_names("Giraffe", *["Spike", "Melvin"], habitat="Grassland")
print(result)
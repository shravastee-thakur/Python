greeting = "Hello, "
question = "How are you?"
message = greeting + question
print(message)

laugh = "ha "
laugh *= 3
print(laugh)

password = "Password123!"
print(len(password))

my_string = "Hello World!"
print(my_string[0])  # indexing
print(my_string[:])  # slicing
print(my_string[-6:-1])  # negative indexing
print(my_string[::2])  # slicing with step


string = "hello"
print(string.capitalize())

my_string = "Hello World!"
print(my_string.casefold())  # To lowercase

name = "abababababab"
print(name.count("aba"))
print(name.count("aba", 4, 7))

msg = "you know you can do it"
print(msg.find('you', 1))
print(msg.find('you'))
print('you' in msg)

space_string = "     Too many spaces     "
print(space_string.strip())

dash_string = "-----Too many dashes----"
print(dash_string.lstrip("-"))
print(dash_string.rstrip("-"))

quote = "It is not a bug"
print(quote.startswith("It"))
print(quote.startswith("Is"))
print(quote.endswith("ug"))
print(quote.replace(" ", "-"))
print(quote.split())

my_list = ["TOO", "MANY", "DASHES"]
print(" ".join(my_list))
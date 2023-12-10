# def print_greeting():
#     print("Hello, Welcome")
#
# print_greeting()
#
# def add(a, b):
#     return a + b
# result = add(5, 10)
# print(result)
#
# def add():
#     pass
# print("hi")
#
# def greet(name, greeting="Hello"):
#     message = f"{greeting}, {name}"
#     print(message)
# greet("Bob")
#
# #  keyword arguments
# # def calculate_pyramid_volume(length, width, height=1):
# #     volume = (length * width * height) / 3
# #     print(volume)
# # calculate_pyramid_volume(width=4, length=5, height=10)
#
# def calculate_letter_grade(grade):
#     if grade >= 90:
#         return "A"
#     elif grade >= 80:
#         return "B"
#     elif grade >= 70:
#         return "C"
#     else:
#         return "F"
#
# print(calculate_letter_grade(95))
#
# #  packing unpacking
# def get_circle_info(radius):
#     pi = 3.14159
#     area = pi * radius ** 2
#     circumference = 2 * pi * radius
#     return area, circumference, pi
#
# # print(get_circle_info(5.0))  # packing
# a, c, p = get_circle_info(5.0)  # unpacking a tuple
# print(a, c, p)

def calculate_pyramid_volume(length, width, height=1):
    return (length * width * height) / 3

my_list = [5, 4, 3]
my_tuple = (5, 4, 3)
my_dict = {1:5, 2:4, 3:3}
result = calculate_pyramid_volume(*my_list)
result = calculate_pyramid_volume(*my_tuple)
result = calculate_pyramid_volume(*my_dict.values())
print(result)
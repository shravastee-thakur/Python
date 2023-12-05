numbers = (1, 2, 3)
print(type(numbers))

numbers1 = tuple("Hello")
print(numbers1)

numbers2 = tuple([1, 2, 3])
print(numbers2)

my_tuple = (1, 3.14, "hi")
print(my_tuple[2])

my_other_tuple = 1, 2, 3  # packing
a, b, c = my_other_tuple  # unpacking
con_tuple = my_tuple + my_other_tuple
# print(my_other_tuple)
print(a, b, c)
print(con_tuple)

tuple1 = (1, 3.14, 'hi', 1, 2, 3)
print(tuple1.count(1))
print(tuple1.index("hi"))

tuple2 = (1, 2, 3) * 3
print(tuple2)
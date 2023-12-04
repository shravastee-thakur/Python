my_list = ['cat', 'dog']
print(my_list)

my_list1 = list('cat')
print(my_list1)

my_list2 = list(['cat'])
print(my_list2)

my_list3 = [1, 2, 3]
my_list3.append(4)  # adds at the end of the list
print(my_list3)

my_list4 = ['cat', 'dog']
my_other_list = ['horse', 'cow']
# my_list4.insert(1,'duck')
my_list4.extend(my_other_list)
print(my_list4)

list1 = ['cat', 'dog', 'horse', 'crow', 'pig', 'elephant']
# list1.remove('cow')
# list1.pop(1)
# list1.clear()
# list1.sort(key=len)
# list1.sort(key=len, reverse=True)
list1.reverse()
print(list1)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[2][2])

numbers = [1, 2, 3, 4, 5]
# new_num = [num ** 2 for num in numbers]
new_num = [num for num in numbers if num % 2 == 0]
print(new_num)

list5 = [[] for i in range(10)]
list5[2].append(4)
print(list5)

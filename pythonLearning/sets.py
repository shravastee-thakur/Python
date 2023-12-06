my_set0 = {1, 2, 3, 1, 3}
print(my_set0)

my_set1 = set([1, 4, 3])
print(my_set1)

my_set2 = {l for l in "abcdeabcdeabcde" if l in 'abc'}  # sets are unordered
print(my_set2)

my_set3 = {1, 2, 3}
# my_set3.add(4)
# my_set3.remove(2)  # gives error if the element is not present
# my_set3.discard(4)  # discard doesnt give error if the element is not present
my_set3.clear()  # leaves traces of set
# del my_set3  # does not leave any trace
print(my_set3)

my_set4 = set("World")
print(my_set4.pop(), my_set4)

my_set = {1, 2, 3}
my_other_set = {4, 5, 6}
my_set.update(my_other_set)
print(my_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {1, 2, 3}
set4 = {5, 6, 7, 8}
# result = set1.difference(set2)  # set1 - set2 same result
# result = set1.intersection(set2)  # set1 & set2 same result
# result = set1.union(set2)
# result = set1.symmetric_difference(set2)
# set1.difference_update(set2)
# print(set1)
# result = set1.isdisjoint(set2)  # false
# result = set1.isdisjoint(set4)  # true
# result = set1.issuperset(set3)  # true
# result = set3.issubset(set1)  # true
print(result)

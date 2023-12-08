my_dict = dict(one='one', two=2)
print(my_dict)

my_dict1 = dict([[1, 'one']])
print(my_dict1)

my_dict2 = ([(1,'one'), [2,'two'], set([3, 'three'])])
print(my_dict2)

# person = {
#     "first_name": 'John',
#     "last_name": "Smith",
#     "age": 30,
# }
# print(person['first_name'])
# person['job'] = 'coder'
# result = person.get('job', 'no job found')
# result = person.setdefault('job', 'Programmer')
# print(result)

# new_info = {
# 'state' : 'Florida',
# 'job' : 'Programmer',
# }
# person.update(state='Florida', job='Programming')  # or ([['state' , 'Florida'], ['job' , 'Programmer']])
# person.update(new_info)
# print(person)


person1 = {
    "first_name": 'John',
    "last_name": "Smith",
    "age": 30,
    'state' : 'Florida',
}

# result = person1.pop('job', 'no job found')
# result = person1.popitem()  # returns tuple
# print(result)
# del person1['age']
print(person1)

print(person1.keys())
print(person1.values())
print(person1.items())

for value in person1.values():
    print(value)

for key, value in person1.items():
    print(key, value)
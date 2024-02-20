### Sets ###

#sets aren't organised, that is why they are similar to dictionaries

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))# it is supposed to be a dictionary

my_other_set = {'Mike', 'Treyu', 22}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[0]) this doesn't work with sets. TypeError: 'set' object is not subscriptable

my_other_set.add('Miketreyu')

print(my_other_set) #a set isn't an ordered structure

my_other_set.add('Miketreyu') # a set doesn't admit repeated data

print(my_other_set) 

print('Mike' in my_other_set)
print('Miki' in my_other_set)

my_other_set.remove('Mike')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {'Mike', 'Treyu', 22}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_new_set).union({'JavaScript', 'C#'}))# sets don't duplicate data, but we can add more data

print(my_new_set.difference(my_set))
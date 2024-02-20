### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Name':'Mike', 'Surname':'Treyu', 'Age':22, 1:'Python'}

my_dict = {
    'Name':'Mike', 
    'Surname':'Treyu', 
    'Age':22, 
    'Languages':{'Python', 'Swift', 'Kotlin'},
    1:1.89
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))#tells us the parameters that we have
print(len(my_dict))

print(my_dict['Name'])

print(my_dict[1])

my_dict['Address'] = 'Miketreyu st.'
print(my_dict)

del my_dict['Address']
print(my_dict)

print('Mike' in my_dict)
print('Surname' in my_dict)
print('Miki' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(('Name', 1)))

my_list = ['Name', 1, 'Floor']

#my_new_dict = dict.fromkeys(('Name', 1, 'Floor')) #it creates a new dictionary without data
#print(my_new_dict)
my_new_dict = dict.fromkeys((my_list)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(('Name', 1, 'Floor')) 
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict)) 
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ('MIke', 'Treyu'))
print(my_new_dict)

my_values = my_new_dict.values
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))




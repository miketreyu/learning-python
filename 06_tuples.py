### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.89, 'Mike', 'Treyu', 'Mike')
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) indexError
#print(my_tuple[-6]) indexError

print(my_tuple.count('Mike'))
print(my_tuple.index('Mike'))

'''
my_tuple[1] = 1.80
print(my_tuple)

you can't change the values of a tuple, nor add new information, no modification. it doesn't support item assignment
'''
print(my_tuple + my_other_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

'''
we can't change the values of a tuple, but we can convert a tuple in a list so we can change the values inside.
'''
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Miketreyu'
my_tuple.insert(1, 'Red')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple

#print(my_tuple) NameError: name 'my_tuple' is not defined. 
#the tuple has been deleted (this is strange because if you can't change tuples, you should't be able to delete)

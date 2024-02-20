### Loops ###

# We use loops when we want to use several times the same code line

# While

my_condition = 0

while my_condition < 10: #while is a looped if 
    print(my_condition)
    my_condition += 2
#if my_condition == 10:
#    print('My condition equals 10')
else: #it is optional
    print('My condition is bigger or equal to 10')

print('It continues running')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Execution stops')
        break

    print(my_condition) 

print('It continues running')

# For
# This executes as many times as items has on a list

my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (22, 1.89, 'Mike', 'Treyu', 'Mike')
for element in my_tuple:
    print(element)

my_set = {'Mike', 'Treyu', 22}
for element in my_set:
    print(element)

my_dict = {'Name':'Mike', 'Surname':'Treyu', 'Age':22, 1:'Python'}
for element in my_dict:
    print(element)
    if element == 'Age':
        break
    print('It runs')

my_dict = {'Name':'Mike', 'Surname':'Treyu', 'Age':22, 1:'Python'}
for element in my_dict:
    print(element)
    if element == 'Age':
        continue #is an other command that we can use
    print('It runs')
else:
    print('The dictionary loop has ended')


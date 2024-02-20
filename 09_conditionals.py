### Conditionals ###

# Conditionals are the ways to establish the flows of execution in our code.
#This means that by adding the condition, we allow to continue or stop the code from running.


my_condition = True

if my_condition: # It means the same as if my_condition == True:
    print('It runs the if condition')

print('It continues running')
'''
my_condition = False

if my_condition:
    print('It runs the if condition')

print('It continues running')
'''
my_condition = 5 * 5

if my_condition == 10:
    print('It runs the second if condition')

print('It continues running')

if my_condition >= 11:
    print('It runs the third if condition') #When we use if, we need the statements to be true, as we see in the examples before.

print('It continues running')

if my_condition > 10 and my_condition < 20:
    print('Is bigger than 10 and smaller than 20') 
elif my_condition == 25:
    print('Equals 25')
else: #We use this when we want to print anything that doesn't follow the condition
    print('Is smaller or equal to 10 or equal or bigger than 20') 

print('It continues running')

my_sting = 'My character string'

if my_sting:
    print('My character string is not empty')

if my_sting == 'My character stringgg':
    print('These character strings coincide')

my_sting = ''

if not my_sting:
    print('My character string is empty')
# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# String of variables on a print
print(my_string_variable, my_int_variable, my_bool_variable)
print("This is the value of:", my_bool_variable)

# Some system functions
print(len(my_string_variable))

# Variables in a single line
name, surname, nickname, age = 'Mike', 'Treyu', 'miketreyu', 'XX'
print('My name is:', name, surname, '. I am:', age, 'years old, and my nickname is', nickname)

# Inputs, we use them mainly in scrips for bash, cmd, etc

name = input('What is your name?:')
age = input('How old are you?')

print(name)
print(age)

# We can change the class/type

name = 35
age = 'mike'
print(name)
print(age)

# Can we force the type/class? It is more efficient if we use that with inputs. Python's types are dinamic.

adress: str = 'My adress'
adress = 32
print(adress)
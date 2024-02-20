### Strings ###

my_string = "My String"
my_other_string = "My other string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "This is a string\nwith a line break"
print(my_new_line_string)

my_tab_string = "\tThis is a string with a tab"
print(my_tab_string)

my_scape_string = "\\tThis is a string with a \\n scape"
print(my_scape_string)

#Format

name, surname, age = 'mike', 'treyu', 1009

print ('My name is {} {} and I am {} years old'.format(name, surname, age)) 
print ('My name is %s %s and I am %d years old' %(name, surname, age))
print ('My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old')
print (f'My name is {name} {surname} and I am {age} years old') #this is the best way of printing data, unless we want to format

#Character unpacking

language = 'Python'
a, b, c, d, e, f = language
print(a)
print(c)

#Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)
language_slice = language[0:6:2]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.upper().isupper())
print(language.startswith('Py'))
print('Py' == 'py') #not the same
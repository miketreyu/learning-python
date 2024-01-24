### OPERATORS ###

print(1 + 2)
print(9 - 6)
print(4 * 8)
print(3 / 4)

# MODULE OPERATION, IT GIVES US THE INFORMATION IF THERE ARE LEFTOVERS IN THE OPERATION
print(10 % 6)

# FLOOR DIVISION, IT GIVES US THE APPROXIMATE RESULT
print(10 // 3)

# THIS GIVES US THE POWER OF A NUMBER
print(5 ** 7)

# WE CAN PRINT THE ADDING OF TWO STRINGS, BUT WE WON'T BE ABLE TO DO OTHER OPERATIONS WITH 2 STRINGS 
print("Hello " + "Python")

# ANOTHER EXCEPTION
print('Hello ' * 5) 

# WE CAN'T ADD A STR TO AN INT: print("Hello" + 5), BUT WE CAN DO THIS
print("Hello " + "5")

# OR THIS
print("Hello " + str(5))

# PRINT A STRING MULTIPLIED BY A FLOAT
my_float = 2.5 * 2
print('Hello ' * int(my_float))

### COMPARATIVE OPERATORS ###

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

# ALPHABETICAL ORDER

print("Hello" > "Python")
print("Hello" < "Python")
print("Hello" <= "Python")
print("Hello" >= "Python")
print("Hello" == "Python")
print("Hello" != "Python")

### LOGICAL OPERATORS ###

print(3 > 4 and "Hello" > "Python")
print(3 > 4 or "Hello" > "Python")
print(3 < 4 and "Hello" < "Python")
print(3 < 4 or "Hello" > "Python") # IF THERE IS A TRUE STATEMENT, IT WILL BE TRUE, EVEN IF THERE ARE FALSE STATEMENTS

print(not(3 > 4))


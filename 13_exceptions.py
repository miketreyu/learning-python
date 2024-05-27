### Exception Handling ###

numberOne = 6
numberTwo = 1
numberTwo = '1'

# try except

try:
    print(numberOne + numberTwo)
    print('It complied')
except:
    # it runs if an exception occurs
    print('It did not comply')

# try expcept else 

try:
    print(numberOne + numberTwo)
    print('It complied')
except:
    print('It did not comply')
else: # Optional
    # it runs if an exception does not occur
    print('Execution continues running')

# try except else finally

try:
    print(numberOne + numberTwo)
    print('It complied')
except:
    print('It did not comply')
else:
    print('Execution continues running correctly')
finally: #Optiona
    # it always runs
    print('It continues running')

# Exceptions by type and value

try:
    print(numberOne + numberTwo)
    print('It complied')
except TypeError:
    print('A TypeError occurred')
except ValueError:
    print('A ValueError ocurred')

# Capturing exceptions information

try:
    print(numberOne + numberTwo)
    print('It complied')
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)



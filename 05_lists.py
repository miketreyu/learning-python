### Lists ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [22, 1.89, 'Mike', 'Treyu']

print(type(my_other_list))
print(type(my_list))

#Even if we have a list, we can access each element independently

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
print(my_list.count(30))#It is used to tell us how many times this value is being used in a list
#print(my_other_list[4]) IndexError

age, height, name, surname = my_other_list
print(name)

age, height, name, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("MikeTreyu")
print(my_other_list)

my_other_list.insert(1, "Red")
print(my_other_list)

my_other_list[1] = 'Blue'
print(my_other_list)

my_other_list.remove('Blue')#it removes an item we know is there
print(my_other_list)

#my_list.pop()#removes last item
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]#it removes by index
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

print([1, 2, 3, 4])

my_list = "Hola python"
print(my_list)
print(type(my_list))

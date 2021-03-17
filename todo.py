todos = ['fuck ur mom', 'run around town', 'makin my way downtown', 'he got a map wha']
print(todos)

first_item = todos[0]
second_item = todos[1]

# print("The first item is:", todos[1])

# What happens if I specify an invalid index?

# Python considers it an error if you use an index that falls outside the range of a sequence:

# print('This item  doesnt exists', todos[15])

# with just line 13, we get an IndexError

# try:
#     print('This item  doesnt exists', todos[15])
# except IndexError:
#     print("You almost got an index error!")

#
# How do I access groups of items in a Sequence?

print("Here are your todos")
print(todos[1:6])

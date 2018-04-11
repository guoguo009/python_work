friends_list=['a', 'b', 'c']
print(friends_list)

print('b')
friends_list[1]= 'd'
print(friends_list)

friends_list.insert(0, 'e')
friends_list.append('f')
print(friends_list)

print(friends_list.pop())
print(friends_list.pop())
print(friends_list.pop())
print('\n')
print(friends_list)

del friends_list[0]
print(friends_list)
del friends_list[0]
print(friends_list)
#del friends_list[]

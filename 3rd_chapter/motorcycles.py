motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducaki')
print(motorcycles)

motorcycle = []
motorcycle.append('a')
motorcycle.append('b')
motorcycle.append('c')
print(motorcycle) 
motorcycle.insert(0,'d')
print(motorcycle)
del motorcycle[0]
print(motorcycle)
print(motorcycle[0])
#弹出最后一个元素
#弹出之后在列表里就没有了
#pop的作用是可以保存删除的那个值
popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
print(motorcycle[-1])
print('The last motorcycle I owend was a ' + popped_motorcycle.title() + ' .')
first_owned = motorcycle.pop(0)
print('The first motorcycle I owend was a ' + first_owned.title() + ' .')
#remove只能删除第一个指定值
motorcycle.remove('b')
print(motorcycle)
motorcycle.append('a')
motorcycle.append('b')
motorcycle.append('c')
too_expensive = 'b'
motorcycle.remove(too_expensive)
print(motorcycle)
print('\nA ' + too_expensive + 'is too expensive for me')


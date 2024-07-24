#Первая часть задания

my_dict = {'Alex': 2001, 'Igor': 1997, 'Anton': 1999}
print(my_dict)
print(my_dict['Alex'])
my_dict['Anna'] = 2003
print(my_dict['Anna'])
my_dict.update({'Mary': 2000,
                'Andrey': 1995})
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict.get('Ann'))
print(a)
print(my_dict)

#Вторая часть задания

my_set = {1, 2, 3, 4, 1, 3, 'Anton', 'banana', 'Anton'}
print(my_set)
my_set.update({7,
               'apple'}) #Можно добавить элементы так, или способом на 23 строке
print(my_set)
my_set.add('coconut')
my_set.remove('banana') #Или my_set.discard('banana')
print(my_set)
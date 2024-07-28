my_dict={'Елена':1998, 'Василиса':1979, 'Каролина':1985}
print(my_dict)
print(my_dict['Елена'])
print(my_dict.get('Алёна', 'не существует'))
my_dict.update({'Маша': 1987, 'Паша': 1979})
print(my_dict)
del my_dict['Елена']
print(my_dict)

my_set={1,1,3,3,8,'Len',False,1.3,1.3}
print(my_set)
print(my_set.add(7))
print(my_set.discard(3))
print(my_set)


immutable_var = ('Apple', 666, True, 3.14)
print(immutable_var)
#immutable_var[0] = 'Grape'
# Изменить кортеж невозможно. Доступна только функция умножения '*' или если кортеж содержит список '[]' то его(список) можно изменить
print()
mutable_list = ['Яблоко' , 777, False, 1.618]
print(mutable_list)
mutable_list[2]=True
mutable_list.extend(['таблетка',778])
mutable_list.remove(777)
print(mutable_list)
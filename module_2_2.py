first = int(input('Введите 1е число: '))
second = int(input('Введите 2е число: '))
third = int(input('Введите 3е число: '))
if first == second == third :
    print('Количество одинаковых чисел 3')
elif first == second or second == third or first == third :
    print('Количество одинаковых чисел 2')
else:
    print('Количество одинаковых чисел 0')
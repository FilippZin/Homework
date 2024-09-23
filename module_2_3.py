i = 0
my_list = [-42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
while i <= len_list :
    if my_list[i] < 0:
        break
    elif my_list[i] == 0:
        my_list.pop(i)
    else:
        print(my_list[i])
        i += 1

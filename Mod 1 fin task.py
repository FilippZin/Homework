grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
first_len = len(grades[0])
first_sum = sum(grades[0])
j_grade = first_sum / first_len

sec_len = len(grades[1])
sec_sum = sum(grades[1])
b_grade = sec_sum / sec_len

thi_len = len(grades[2])
thi_sum = sum(grades[2])
s_grade = thi_sum / thi_len

fou_len = len(grades[3])
fou_sum = sum(grades[3])
k_grade = fou_sum / fou_len

fif_len = len(grades[4])
fif_sum = sum(grades[4])
a_grade = fif_sum / fif_len

#print(j_grade,b_grade,s_grade,k_grade,a_grade)

students_sort = sorted(students)
print({students_sort[0] : j_grade , students_sort[1] : b_grade ,students_sort[2] : s_grade ,students_sort[3] : k_grade ,students_sort[4] : a_grade })

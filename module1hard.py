grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

sum_num1 = grades[0]
sum_num2 = grades[1]
sum_num3 = grades[2]
sum_num4 = grades[3]
sum_num5 = grades[4]
print(sum(sum_num1) / 5)
sum_num1 = 4.0
print(sum(sum_num2) / 4)
sum_num2 = 2.25
print(sum(sum_num3) / 4)
sum_num3 = 4.0
print(sum(sum_num4) / 3)
sum_num4 = 3.6666666666666665
print(sum(sum_num5) / 5)
sum_num5 = 4.8

del grades[0:5]
grades.append(sum_num1)
grades.append(sum_num2)
grades.append(sum_num3)
grades.append(sum_num4)
grades.append(sum_num5)

average_grades = {sorted_students[0]: sum_num1,
                  sorted_students[1]: sum_num2,
                  sorted_students[2]: sum_num3,
                  sorted_students[3]: sum_num4,
                  sorted_students[4]: sum_num5}
print(average_grades)

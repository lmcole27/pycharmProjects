
my_list = [1, 2, 3]
new_list = [(n + 1) for n in my_list]
print(new_list)

name = "Linda"
name_list = [n for n in name]
print(name_list)

my_range = range(1, 5)
new_range = [(n * 2) for n in my_range]
print(new_range)

names = ["Mo", "Arkin", "Beatrix", "Elias", "Samay", "Linda", "Bonnie", "Ronald"]
short_names = [name.upper() for name in names if (len(name) < 5)]
print(short_names)

import random
student_scores = {student:random.randint(0, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if int(score) > 60}
print(passed_students)
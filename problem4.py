def print_student_averages(grades):
    student_number = 1
    for student_grades in grades:
        average = sum(student_grades) / len(student_grades)
        print(f"student {student_number}= grades: {student_grades} average: {average:.2f}")
        student_number += 1


grades = [
    [70,50,20,88,65],
    [85, 90, 78,61,52],
    [88, 76, 92,53,87],
    [70, 80, 65,100,50],
    [95, 93, 89,70,58]
]

print_student_averages(grades)
def calculate_result(name, marks):
    total_marks = sum(marks)
    percentage = total_marks / len(marks)

    if percentage >= 75:
        division = "1st Division with Distinction"
    elif percentage >= 60:
        division = "1st Division"
    elif percentage >= 45:
        division = "2nd Division"
    else:
        division = "Fail"

    print("\nStudent Name:", name)
    print("Total Marks:", total_marks)
    print("Percentage:", round(percentage, 2), "%")
    print("Result:", division)


# ---- Data for 3 Students ----
students = [
    ("Student 1", [80, 75, 70]),
    ("Student 2", [65, 60, 58]),
    ("Student 3", [85, 90, 88])
]

# ---- Display Result ----
for student in students:
    calculate_result(student[0], student[1])

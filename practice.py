students = [
    ("Tom", 80, "Math"),
    ("Zara", 55, "Science"),
    ("Mike", 72, "Math"),
    ("Lisa", 90, "Science"),
    ("Jane", 60, "Math")
]

def filter_students(students):
    student = []

    for name, score, subject in students:
        if score < 70:
            continue
        if "Math" not in subject:
            continue
    
        student.append(name)

    return student

print(filter_students(students))

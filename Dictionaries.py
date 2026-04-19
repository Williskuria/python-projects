student = {"name": "Kuria", "age": 20, "grade": "A"}

print(student["name"], " has scored an", student["grade"])

# adding items to a dictionary
student["City"] = "Nairobi"
student["age"] = 21
print(student)

# loop through items
scores  ={"math": 88, "English": 92, "Science": 75}

for subject, score in scores.items():
    print("You have scored", score, "in", subject)
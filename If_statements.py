class Student:
    def __init__(self, name):
        self.name = name

    def subjects(self, maths, science, english, kiswahili):
        subj = [maths, science, english, kiswahili]
        total = sum(subj)
        average = total / len(subj)
        if average > 80:
            grade = "A"
        elif average > 60:
            grade = "B"
        elif average > 40:
            grade = "C"
        else:
            grade = "D"

        print(f"{self.name} - average:{average} - You have a {grade}")
        self.save_to_file(average, grade)

    def save_to_file(self, average, grade):
        import csv
        with open("students.csv", "a", newline="")as file:
            writer = csv.writer(file)
            writer.writerow([self.name, average, grade])
    
    def read_file(self):
        import csv
        with open("students.csv", "r")as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} - average: {row[1]} - Grade: {row[2]}")
        

student1 = Student("Kuria")
student1.subjects(80, 75, 60, 70)
student1.read_file()

student2 = Student("Alex")
student2.subjects(55, 60, 70, 65)

student3 = Student("Jane")
student3.subjects(90, 85, 88, 92)
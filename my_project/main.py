import csv

with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"] + " lives in " + row["city"])

with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])
    
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "grade", "school"])
    writer.writerow(["willis", "A", "katchez"])

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"])

# Writing Dictionaries to CSV Files
with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})
    writer.writerow({'player_name': 'Willis Nganga', 'fide_rating': 7145})

# reading a CSV file using DictReader()
with open('players.csv', "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["player_name"])
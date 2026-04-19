# Example input
people = [
    ("Alice", 24, "Nairobi", ["reading", "coding", "hiking"]),
    ("Bob", 20, "Nairobi", ["gaming", "reading"]),
    ("Charlie", 25, "Mombasa", ["reading", "coding", "swimming", "music"]),
    ("Diana", 23, "Kisumu", ["coding", "travel"]),
    ("Eve", 26, "Nairobi", ["reading", "coding", "art", "yoga", "music"])
]

criteria = {
    "min_age": 22,
    "cities": ["Nairobi", "Mombasa", "Kisumu"],
    "required_hobbies": ["reading", "coding"],
    "max_hobbies": 4
}

def filter_members(people, criteria):
    qualified = []

    for name, age, city, hobbies in people:
        if age < criteria["min_age"]:
            continue
        if city not in criteria["cities"]:
            continue
        if not all(h in hobbies for h in criteria["required_hobbies"]):
            continue
        if len(hobbies) > criteria["max_hobbies"]:
            continue

        qualified.append(name)

    return qualified



# Call the function and print the result
print(filter_members(people, criteria))
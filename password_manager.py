class PasswordManager:
    def __init__(self):
        self.filename = "passwords.csv"

    def save_pass(self, site, username, password):
        import csv
        with open(self.filename, "a", newline="")as file:
            writer = csv.writer(file)
            writer.writerow([site, username, password])
        print(f"Password for {site} saved")

    def read_pass(self):
        import csv
        with open(self.filename, "r", newline="")as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Site: {row[0]} | username:{row[1]} | password:{row[2]}")

    def find_pass(self, site):
        import csv
        with open(self.filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == site:
                    print(f"Site: {row[0]} | Username: {row[1]} | Password: {row[2]}")
                    return
        print(f"No password found for {site}")

pm = PasswordManager()
pm.find_pass("instagram")


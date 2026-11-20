import csv
import os

FILE_NAME = "volunteers.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Phone", "Email", "Skill"])


def add_volunteer():
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    skill = input("Enter Skill: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, phone, email, skill])

    print("\nVolunteer Registered Successfully!\n")


def view_volunteers():
    print("\n===== Volunteer Records =====")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            if row:
                print(row)


def search_volunteer():
    keyword = input("\nEnter Volunteer Name: ").strip().lower()

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row

        for row in reader:
            if row and keyword in row[0].lower():
                print(row)
                found = True

    if not found:
        print("Volunteer Not Found")


def filter_by_skill():
    skill = input("\nEnter Skill: ").strip().lower()

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row

        for row in reader:
            if len(row) > 4 and skill in row[4].lower():
                print(row)
                found = True

    if not found:
        print("No Volunteers Found")


def generate_report():
    count = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row

        for row in reader:
            if row:
                count += 1

    print("\n===== REPORT =====")
    print("Total Volunteers:", count)


while True:
    print("\n====== VOLUNTEER MANAGEMENT SYSTEM ======")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Filter By Skill")
    print("5. Generate Report")
    print("6. Exit")

    choice = input("Enter Choice: ").strip()

    if choice == "1":
        add_volunteer()

    elif choice == "2":
        view_volunteers()

    elif choice == "3":
        search_volunteer()

    elif choice == "4":
        filter_by_skill()

    elif choice == "5":
        generate_report()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

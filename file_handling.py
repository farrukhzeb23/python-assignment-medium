import csv

try:
    print("======= Average Scores =======\n")
    with open("students.csv", 'r') as file:
        csv_reader = csv.reader(file)
        # Skipping the header
        next(csv_reader)
        for row in csv_reader:
            student_name = row[0]
            scores_str = row[1::]
            scores = [int(score) for score in scores_str]
            average = sum(scores) / len(scores)
            print(f"{student_name}: {average:.2f}")
    print("\n======= Average Scores =======\n")
except FileNotFoundError as error:
    print("students.csv file not found")


try:
    print("======= Address Book =======\n")
    with open("address-book.csv", "a", newline='') as file:
        csv_writer = csv.writer(file)

        name = input("Input name: ")
        phone = input("Input phone number: ")
        data = [name, phone]
        csv_writer.writerow(data)

    search_value = input("Enter name to search: ")
    found_address = None

    with open("address-book.csv", "r", newline='') as file:
        csv_reader = csv.reader(file)
        # Skipping the header
        next(csv_reader)
        for rows in csv_reader:
            if search_value.lower() in rows[0].lower():
                found_address = rows

    if found_address is None:
        print("Did not find this address")
    else:
        print(f"{found_address[0]} contact information:{found_address[1]}")

    print("\n======= Address Book =======\n")
except FileNotFoundError:
    print("address-book.csv file not found")

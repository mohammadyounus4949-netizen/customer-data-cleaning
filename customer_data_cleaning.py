import csv

input_file = "customer_data.csv"
output_file = "cleaned_customer_data.csv"

cleaned_data = []

try:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Remove rows with missing Name or Email
            if row["Name"].strip() and row["Email"].strip():
                row["Name"] = row["Name"].title()
                row["Email"] = row["Email"].lower()
                cleaned_data.append(row)

    with open(output_file, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Email", "City"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(cleaned_data)

    print("Data Cleaning Completed Successfully!")
    print("Total Clean Records:", len(cleaned_data))

except FileNotFoundError:
    print("customer_data.csv file not found.")

import csv
#writing to a csv file
with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(["Name", "Age", "City"])
    # Write some data
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])
# Reading from a csv file
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    # Read the header
    header = next(reader)
    print("Header:", header)
    # Read the data
    for row in reader:
        print("Row:", row)
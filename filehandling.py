import os
import csv
# Create a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Check if the file exists
if os.path.exists("example.txt"):
    print("File exists")

print("")

with open("test.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])



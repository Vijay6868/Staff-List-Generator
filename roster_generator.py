import random
from datetime import datetime, timedelta

print("MEETING MINUTE ROSTER 2023-2024")

names = ["staff name", "staff name","staff name"]

startDate = datetime(2023,11,14)
delta = timedelta(days=14)

random.shuffle(names)

print(f"| {'Date':<20} | {'Chair':<15} | {'Minute Taker':<15} |")

# Print separator line
print("+----------------------+-----------------+-----------------+")

# Loop through the range of names
for i in range(len(names)):
    # Format the date
    formatted_date = startDate.strftime("%d-%m-%Y")

    # Print the row
    if i < len(names) - 1:
        print(f"| {formatted_date:<20} | {names[i]:<15} | {names[i + 1]:<15} |")
    else:
        print(f"| {formatted_date:<20} | {names[i]:<15} | {names[0]:<15} |")

    # Update the start date
    startDate = startDate + delta




  


print("Welcome to the Interactive Personal Data Collector!\n")

# Convert user inputs to the correct types
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Use f-strings for clean output formatting
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})\n")

current_year = 2026
birth_year = current_year - age

print(f"Your birth year is approximately:\n{birth_year} (based on your age of {age})\n")
print("Thank you for using the Personal Data Collector. Goodbye!")


print("Welcome to the Interactive Personal Data Collector!")
print("Please enter your personal information.\n")



name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))



current_year = 2026
birth_year = current_year - age



print("\nThank you! Here is the information we collected:\n")

print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favourite Number:", favourite_number)

print("\nYour birth year is approximately:", birth_year)



print("\n--- Data Types and Memory Addresses ---")

print("Name:")
print("Value:", name)
print("Data Type:", type(name))
print("Memory Address:", id(name))

print("\nAge:")
print("Value:", age)
print("Data Type:", type(age))
print("Memory Address:", id(age))

print("\nHeight:")
print("Value:", height)
print("Data Type:", type(height))
print("Memory Address:", id(height))

print("\nFavourite Number:")
print("Value:", favourite_number)
print("Data Type:", type(favourite_number))
print("Memory Address:", id(favourite_number))



print("\nThank you for using the Personal Data Collector!")
print("Goodbye! Keep exploring Python.")
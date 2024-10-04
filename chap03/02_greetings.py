# Page 36
# Try-It-Yourself 3-2
# Start with the name list from 3-1
# Print a message to each person 
# Use the same message, but change the names

names = ["Alice", "Bob", "Carlos", "Diane"]
greeting = "Hello, my dear friend"

print(greeting, names[0] + ".")

# Using a loop
for name in names:
    print(greeting, name + "!")
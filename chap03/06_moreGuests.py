# Page 42
# Try It Yourself 3-6
# Continuing from exercise 3-5, add more guests using Python methods

guestList = ['stephen hawking', 'rhonda rousey', 'karl urban']

print("We bought a bigger table! Let's invite more people.")

guestList.insert(0, 'will ferrell')
print(f"Added {guestList[0].title()}")

guestList.insert(2, 'alice cooper')
print(f"Added {guestList[2].title()}")

guestList.append('steve jobs')
print(f"Added {guestList[-1].title()}")

print(f"Would you like to come to dinner, {guestList[0].title()}?")
print(f"Would you like to come to dinner, {guestList[1].title()}?")
print(f"Would you like to come to dinner, {guestList[2].title()}?")
print(f"Would you like to come to dinner, {guestList[3].title()}?")
print(f"Would you like to come to dinner, {guestList[4].title()}?")
print(f"Would you like to come to dinner, {guestList[5].title()}?")

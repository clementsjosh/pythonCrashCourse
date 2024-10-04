# Page 42
# Try It Yourself Exercise 3-5
# Using the list from 3-4, replace one of the the invitees

guestList = ['stephen hawking', 'isla fisher', 'karl urban']

print(f"{guestList[1].title()} can't make it. Let's invite someone else.")

guestList[1] = 'rhonda rousey'

print(f"Would you like to come to dinner, {guestList[0].title()}?")
print(f"Would you like to come to dinner, {guestList[1].title()}?")
print(f"Would you like to come to dinner, {guestList[2].title()}?")
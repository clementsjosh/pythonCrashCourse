# Page 42
# Try It Yourself 3-7
# Continuing from exercise 3-6, remove guests using Python methods

guestList = [
    'stephen hawking', 
    'rhonda rousey', 
    'karl urban', 
    'will ferrell', 
    'alice cooper', 
    'steve jobs',
]

print("Our new table won't make it in time. Need to prune the list.")

print(f"Sorry {guestList[-1].title()}, we don't have enough room.")
guestList.pop()
print(f"Sorry {guestList[-1].title()}, we don't have enough room.")
guestList.pop()
print(f"Sorry {guestList[-1].title()}, we don't have enough room.")
guestList.pop()
print(f"Sorry {guestList[-1].title()}, we don't have enough room.")
guestList.pop()

print(f"Can you still make it, {guestList[0].title()}?")
print(f"Can you still make it, {guestList[1].title()}?")

del guestList[0]
del guestList[0]
print(guestList)

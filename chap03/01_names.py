# Page 36
# Try-It-Yourself 3-1
# Store the names of a few of your friends in a list called names. 
# Print each person's name by accesing each element in the list. 

nameList = ["alice", "bob", "carlos", "diane"]

print(nameList[0].title())
print(nameList[1].title())
print(nameList[2].title())
print(nameList[3].title())

# Better version
for name in nameList: 
    print(name.title())
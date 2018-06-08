# Lists (Arrays)

spamA = ["cat", "bat", "rat", "tiger"]
print(spamA)
print(spamA[0])
print(spamA[1])
print(spamA[2])
print(spamA[3])

print("spamA Length: " + str(len(spamA)))

print()
print("Negative Indices")
print(spamA[-1])
print(spamA[-2])

print()
print("Array Search")
print("tiger" in spamA)
print("regit" in spamA)
print("tiger" not in spamA)

print()
print("In For Loop")
for i in range(len(spamA)):
    print("spam A " + str(i) + " is " + spamA[i])

print()    
print("Array Index")
print(spamA.index("tiger"))

print()
print("Multiple Assignment")
feline, mammal, rodent, bigcat = spamA
print(feline)
print(mammal)
print(rodent)
print(bigcat)

print()
print("Append")
print(spamA.append("elephant"))
print(spamA)

print()
print("Insert")
print(spamA.insert(1, "rhino"))
print(spamA)

print()
print("Remove")
print(spamA.remove("rhino"))
print(spamA)

print()
print("Append with +")
spamA = spamA + ["giraffe"]
print(spamA)

print()
print("Remove")
print(spamA.remove("giraffe"))
print(spamA)

print()
print("Converts a string to Array")
print(list("Hello"))
print(list(range(5)))
print(list(range(0, 10, 2)))
print(list(range(1, 10, 2)))

print()
print("Array Concatenation")
print(spamA + spamA)

print()
print("Array Multiplication")
print(spamA * 3)

print()
print("slice")
print(spamA[0:2])
print(spamA[1:2])

print()
print("slice again")
print(spamA[:2])
print(spamA[1:])

print()
print("Delete")
del spamA[2]
print(spamA)

print()
spamB = [["Apple", "Orange", "Banana"], ["Pelican", "Falcon", "Humming Bird"]]
print("2D Array")
print(spamB)
print(spamB[0])
print(spamB[1])
print(spamB[0][1])
print(spamB[1][2])

print("spamB Length: " + str(len(spamB)))

print()
print("Negative Indices")
print(spamB[-1][-2])

print()
print("Sort")
spamC = [19, 27, 99, 87, 36, 78]
spamC.sort()
print(spamC)
spamC.sort(reverse=True)
print(spamC)

print()
print("ASCII-betical Order")
spamD = ["Alligator", "Crocodile", "dog", "penguin", "Elephant"]
spamD.sort()
print(spamD)
#spamD.sort(key=str.lower)
spamD.sort(key=str.upper)
print(spamD)

print()
print("Varied arrays")
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

print()
print("Explicit Copy")
list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
print(list2)
print(list1)


print()
print("Use sorted for Sorting Array")
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
print(first)
print(second)

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

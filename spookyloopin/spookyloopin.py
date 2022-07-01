
count = 0
with open("dracula.txt", "r") as dracula:
    for line in dracula:
        if "vampire" in line.lower():
            print(line)
            count += 1
print("Vampire appeared:", count, "number of times.") 

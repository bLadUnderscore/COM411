from time import sleep
from tqdm import tqdm

# Task 1

apples = int(input("How many apples should I remove? \n"))
removed = 0

while removed < apples:
    removed = removed + 1
    print("Removed apple")

# Task 2

obstacles = int(input("How many obstacles must I avoid? \n"))

avoided = 0

while avoided < obstacles:
    avoided = avoided + 1
    print("Avoiding...Done!", avoided, "obstacles avoided.")

# Task 3

bars = int(input("How many bars should be charged"))

charged = 0
status = ""

while charged < bars:
    charged += 1
    status = status + "|"
    print("Charging...", status)

print("Finished Charging")

# Task 4

word = input("Please enter a phrase: \n")

d = len(word)

output = "Hi " * d
print(output)
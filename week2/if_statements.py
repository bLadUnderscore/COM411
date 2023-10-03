import time

#########

genre = input("What type of book is this \n").lower

if genre == "adventure" :
    print("I like adventure books")
else:
    print("Not really a big fan of that genre")
    quit()

print("Finished reading book.")
print("")

##########

activity = ""

while activity != "calculate":
    activity = input("Please enter the activity to be performed \n").lower
    if activity == "calculate":
        print("Performing activity...")
        time.sleep(5)
        print("Activity completed!")
    else:
        print("Sorry, i dont know that activity")

##########

robot = ""

while robot != "up" or robot != "down" or robot != "left" or robot != "right":
    robot = input("Towards which direction should i go? \n")
    if robot == "up":
        print("I am moving up!")
    elif robot == "left":
        print("I am moving left!")
    elif robot == "right":
        print("I am moving right")
    elif robot == "down":
        print("I am moving down")
    else:
        print("Please enter a valid direction")
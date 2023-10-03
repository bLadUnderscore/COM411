import time

#########

genre = input("What type of book is this \n")

if genre == "adventure" :
    print("I like adventure books")
else:
    print("Not really a big fan of that genre")
    quit()

print("Finished reading book.")
print("")

##########

activity = input(" Please enter the activity to be performed \n")

while activity != "calculate":
    if activity == "calculate":
        print("Performing activity...")
        time.sleep(5)
        print("Activity completed!")
    else:
        print("Sorry, i dont know that activity")



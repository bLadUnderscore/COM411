cover = input("Enter the cover type of your book: \n").lower() # Asks the user what type of cover is their book

if cover == "soft":
    bound = ""
    while bound != "Y" and bound != "N": # If bound doesnt equal Yes or No, the Code will display an error and loop
        bound = input("Is the book perfect-bound? Y/N \n").upper()
        if bound == "Y":
            print("Soft cover, perfect bound books are very popular!")
        if bound == "N":
            print("Soft covers with coils or stitches are great for short books")
        else:
            print("Please enter a valid answer")

if cover == "hard":
    print("Books with hard covers can be more expensive")
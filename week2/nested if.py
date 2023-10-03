cover = input("Enter the cover type of your book: \n").lower()

if cover == "soft":
    bound = ""
    while bound != "Y" and bound != "N":
        bound = input("Is the book perfect-bound? Y/N \n").upper()
        if bound == "Y":
            print("Soft cover, perfect bound books are very popular!")
        if bound == "N":
            print("Soft covers with coils or stitches are great for short books")
        else:
            print("Please enter a valid answer")

if cover == "hard":
    print("Books with hard covers can be more expensive")
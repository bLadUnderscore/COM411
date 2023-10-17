# Task 1

print("Program Started!")
print("Please enter a standard character:")

user_input = input()

if len(user_input) == 1:
    letter = user_input
    ascii_value = ord(letter)
    print(f"The ASCII code for {letter} is {ascii_value}.")
else:
    print("Error: Please enter a single character.")

print("Program Ended!")

# Task 2

print("Program Started!")
print("Please enter an ASCII code:")

user_input = input()  # Read the user's response as a string
user_input = int(user_input)  # Convert the input to an integer

if 32 <= user_input <= 126:
    character = chr(user_input)
    print(f"The character represented by the ASCII code {user_input} is {character}.")
else:
    print("Error: Please enter a positive integer within the range 32 - 126 (inclusive).")

print("Program Ended!")




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



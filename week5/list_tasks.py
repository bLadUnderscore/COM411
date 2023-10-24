# Define the directions function
def directions():
    # Create a list named 'steps' with the specified items
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps


# Define the run_task1 function
def run_task1():
    # Call the 'directions' function to get the list of steps
    steps = directions()

    # Display the list of steps
    for step in steps:
        print(step)


# Call the 'run_task1' function to execute the program
run_task1()



# Function to get the student ID
def get_Student_ID():
    student_id = input("Enter your Student_ID: ")
    return student_id

def costSlab1(student_id, source_data):

    # Displaying the cost for slab 1 along with student ID
    print(f"Bill for {student_id} - Slab 1 is:", end=" ")
    print(*source_data[0])

def costSlab2(source_data):
  #cost for slab2
    print("Bill for Slab 2 is:", end=" ")
    print(*source_data[1])

def costSlab3(source_data):
   

# cost for slab 3
    print("Bill for Slab 3 is:", end=" ")
    print(*source_data[2])

# Function to display the main menu
# Function to display the main menu
def displayMainMenu(student_id, source_data):
    while True:
        print()
        print(f"Student ID: {student_id}")
        print("1. Press 1 to display the bill for slab 1 and slab 2.")
        print("2. Press 2 to display the bill for slab 3.")
        print("Any other key to exit.")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Perform the selected operation
        if choice == "1":
            costSlab1(student_id, source_data)
            costSlab2(source_data)
        elif choice == "2":
            costSlab3(source_data)
        else:
            print("Invalid Choice. Exiting.")
            break  # Exit the loop if the choice is not 1 or 2

# Main function
def main():
    # Source  2d data matrix
    source_data = [
        [550, 650, 750],
        [1800, 2250, 2550],
        [4200, 4600, 4800]
    ]

    # To Print the electricity bill heading
    print("*********** Electricity Bill ***********\n")

    # Get the student ID
    student_id = get_Student_ID()

    # Display the main menu
    displayMainMenu(student_id, source_data)

if __name__ == "__main__":
    main()

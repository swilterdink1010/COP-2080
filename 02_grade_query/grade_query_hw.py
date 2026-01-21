#
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {} 

user_input = ""
valid_inputs = ["A", "R", "M", "P", "Q"]

# Loop until the user chooses to quit.
while (user_input != "Q"):
# Prevent unexected inputs by converting input to upper-case
# Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
    if (user_input := input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper) in valid_inputs:
        match user_input:

        # Use a condition to handle adding a new student.
        # Convert grade into integer
        # Gather user input for "Enter the name of the student: "
        # Check if student name already exists "Sorry, that student is already present."
        # Gather user input for student grade "Enter the student's grade: "
        # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
            case "A":
                pass

        # Handle removing a student if user inputs 'R'
        # Check input for "What student do you want to remove? "
        # use pop to remove key/value form grades
        # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
        # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
            case "R":
                pass

        # Handle modifying a student grade if user inputs 'M'
        # "Enter the name of the student to modify: "
        # Convert grade into integer
        # If student is in grades dictionary, show existing grade "The old grade is"
        # Gather input for new grade "Enter the new grade: "
        # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
            case "M":
                pass

        # Handle printing grade average as a string if user input is 'P'
        # Use "The average grade is "
        # Handle printing all of the student names with associated grade
        # Display explictly as strings
            case "P":
                pass

        # Handle the case for quiting if user inputs 'Q' "Goodbye!"
            case "Q":
                print("Goodbye!")

    # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    else:
        print("Sorry, that wasn't a valid choice.")
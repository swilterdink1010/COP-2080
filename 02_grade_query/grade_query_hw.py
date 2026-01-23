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
    if (user_input := str(input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ")).upper()) in valid_inputs:
        match user_input:

        # Use a condition to handle adding a new student.
        # Convert grade into integer
        # Gather user input for "Enter the name of the student: "
        # Check if student name already exists "Sorry, that student is already present."
        # Gather user input for student grade "Enter the student's grade: "
        # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
            case "A":
                input_student = str(input("Enter the name of the student: "))
                if input_student not in grades.keys():
                    print("Sorry, that student is already present.")
                    continue
                input_grade = -1
                while (input_grade < 0 or input_grade > 100):
                    try:
                        input_grade = int(input("Enter the student's grade: "))
                        if (input_grade < 0 or input_grade > 100):
                            print("Please enter grade as number 0-100")
                    except ValueError:
                        print("Please enter grade as number 0-100")
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
        print(user_input)
        print("Sorry, that wasn't a valid choice.")
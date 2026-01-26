#
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {} 

user_input = ""
valid_inputs = ["A", "R", "M", "P", "Q"]

# Loop until the user chooses to quit.
while user_input != "Q":
    # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
    # Prevent unexected inputs by converting input to upper-case
    if (user_input := input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()) in valid_inputs:
        match user_input:
            # Use a condition to handle adding a new student.
            case "A":
                # Gather user input for "Enter the name of the student: "
                input_student = str(input("Enter the name of the student: "))
                # Check if student name already exists "Sorry, that student is already present."
                if input_student in grades:
                    print("Sorry, that student is already present.")
                    continue
                input_grade = -1
                while input_grade < 0 or input_grade > 100:
                    try:
                        # Gather user input for student grade "Enter the student's grade: "
                        # Convert grade into integer
                        input_grade = int(input("Enter the student's grade: "))
                        # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
                        if input_grade < 0 or input_grade > 100:
                            print("Please enter grade as number 0-100")
                        else:
                            grades[input_student] = input_grade
                            print("Student added successfully.")
                    except ValueError:
                        print("Please enter grade as number 0-100")
            # Handle removing a student if user inputs 'R'
            case "R":
                # Check input for "What student do you want to remove? "
                input_student = str(input("What student do you want to remove? "))
                # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
                if input_student not in grades:
                    print("Sorry, that student doesn't exist and couldn't be removed.")
                    continue
                # use pop to remove key/value form grades
                grades.pop(input_student)
                print("Student removed successfully.")

            # Handle modifying a student grade if user inputs 'M'
            case "M":
                # "Enter the name of the student to modify: "
                input_student = str(input("Enter the name of the student to modify: "))
                # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
                if input_student not in grades:
                    print("Sorry, that student doesn't exist and couldn't be modified.")
                    continue
                # If student is in grades dictionary, show existing grade "The old grade is"
                print(f"The old grade is {grades[input_student]}")
                input_grade = -1
                while input_grade < 0 or input_grade > 100:
                    try:
                        # Gather input for new grade "Enter the new grade: "
                        # Convert grade into integer
                        input_grade = int(input("Enter the new grade: "))
                        if input_grade < 0 or input_grade > 100:
                            print("Please enter grade as number 0-100")
                        else:
                            grades[input_student] = input_grade
                            print("Student grade modified successfully.")
                    except ValueError:
                        print("Please enter grade as number 0-100")

            # Handle printing grade average as a string if user input is 'P'
            case "P":
                # Handle printing all of the student names with associated grade
                if grades:
                    total = 0
                    for key, value in grades.items():
                        total += value
                        # Display explictly as strings
                        print(f"{key}: {value}")
                    avg = round(total / len(grades), 1)
                    # Use "The average grade is "
                    print(f"The average grade is {avg}")
                else:
                    print("No grades to average.")
                    continue

            # Handle the case for quiting if user inputs 'Q' "Goodbye!"
            case "Q":
                print("Goodbye!")

    # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
    else:
        print(user_input)
        print("Sorry, that wasn't a valid choice.")
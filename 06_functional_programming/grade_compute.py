VALID_GRADES = []
for i in ("A", "B", "C", "D"):
    for j in ("+", "", "-"):
        VALID_GRADES.append(i + j)
VALID_GRADES.append("F")

GPA_GRADES = [4.0, 4.0]
for i in (3.0, 2.0, 1.0):
    for j in (0.7, 0.3, 0.0):
        GPA_GRADES.append(i + j)
GPA_GRADES.extend([0.7, 0.0])

def input_verify()->list:
    '''
    :return: List of letter grades
    :rtype: list
    '''
    valid = False
    while not valid:
        input_ = input("Enter grades: ").upper().split("$ ")
        if input_ == ["Q"]:
            quit(0)
        if len(input_) == 4:
            valid = True
            for i in input_:
                if i not in VALID_GRADES:
                    valid = False
        if not valid:
            print("Invalid input. Make sure to input 4 grades delimited by '$ '.")
        else:
            return input_
    


def to_letter(n_grade)->str:
    '''
    :param n_grade: Float grade
    :return: Corresponding letter grade
    :rtype: str
    '''
    if n_grade == 0.0:
        return "F"
    for i in range(len(GPA_GRADES)):
        if n_grade > GPA_GRADES[i+1]:
            return VALID_GRADES[i]


def to_number(l_grade)->float:
    '''
    :param l_grade: Letter grade
    :return: Corresponding number grade
    :rtype: float
    '''
    for i in range(len(VALID_GRADES)):
        if l_grade == VALID_GRADES[i]:
            return GPA_GRADES[i]


def gpa_parse(l_list)->list:
    '''
    :param l_list: List of letter grades
    :return: List of GPA values
    :rtype: list
    '''
    out = []
    for i in l_list:
        out.append(to_number(i))
    return out


def average_grade(n_list)->float:
    '''
    :param n_list: List of GPA grades
    :return: Average GPA Grade
    :rtype: float
    '''
    temp = n_list.copy()
    temp.remove(min(temp))
    bonus = False
    if max(temp) < 2.7:
        bonus = True
    sum = 0
    for i in temp:
        sum += i
    avg = round(sum / len(temp), 2)
    if bonus:
        avg += 0.25
    return avg


def str_grades(l_list)->str:
    '''
    :param l_list: List of letter grades
    :return: Formatted string listing grades entered
    :rtype: list
    '''
    stream = "Grades Entered: "
    for i in l_list:
        stream += i + ", "
    stream = stream[:-2]
    return stream


str_low = lambda n_list : "Lowest Grade Dropped: " + to_letter(min(n_list))


str_average = lambda avg : "Calculated Average: " + str(avg)


str_final = lambda avg : "Final Letter Grade: " + to_letter(avg)


def print_row(str_)->None:
    '''
    :param str_: String to print
    '''
    stream = "| " + str_
    spaces = 39 - len(stream)
    stream += " " * spaces + "|"
    print(stream)


def print_summary(l_list, n_list)->None:
    '''
    :param l_list: List of letter grades
    :param n_list: List of number grades
    '''
    EMPTY_LINE = "-" * 40
    
    avg = average_grade(n_list)
    
    print(EMPTY_LINE)
    print_row(" " * 8 + "GRADE REPORT SUMMARY")
    print(EMPTY_LINE)
    print_row(str_grades(l_list))
    print_row(str_low(n_list))
    print_row(str_average(avg))
    print_row(str_final(avg))
    print(EMPTY_LINE)
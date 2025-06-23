def arithmetic_arranger(problems, show_answers=False):
    # Create a string joining all the problems together
    probs = ' '.join(problems)

    # Create a string containing all the numbers in string format
    str_nums = "0123456789"

    # Create separate strings separating the numbers and the operations in order
    chars = probs.split(" ")

    # Every third character is the first number in the arithematic starting from index 0 (0, 3, 6, 9)
    # Every third character is the operator in the arithematic starting from index 1 (1, 4, 7, 10)
    # Every third character is the second number in the arithematic starting from index 2 (2, 5, 8, 11)
    first_row = chars[0: len(chars) + 1: 3] 
    operators = chars[1:len(chars) + 1:3]
    second_row = chars[2:len(chars) + 1: 3]
    answers = []

    # Create an array to contain the dashes according to maximum number of digits in the arithematic
    dashes = [""]

    # Create lines for each of the arithematic
    first_line = "" # Contains the first numbers
    second_line = "" # Contains the operations and second numbers
    third_line = "" # Contains the dashes
    fourth_line = "" # Contains the answers to the arithematic, if the user asks for it

    # ERROR Checking
    if len(operators) > 5:
        # If there are more than 5 operators in the operators list, then there are too many problems
        return "Error: Too many problems."
    else:
        # This arithematic formatter will only allow for addition and subtraction, any other operator is not allowed
        for signs in operators:
            if signs not in ['+', '-']:
                return "Error: Operator must be '+' or '-'."
    
    # Check if the number of digits is more than 4 or that the numbers have digits themselves
    for num in first_row:
        if len(num) > 4:
            # If there are more than 4 digits in the number, we return the error
            return 'Error: Numbers cannot be more than four digits.'
        # Checking if each character in the number is a digit
        for char in num:
            if char not in str_nums:
                return 'Error: Numbers must only contain digits.'
    
    # Check the numbers in the second set of numbers too
    for num in second_row:
        if len(num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        for char in num:
            if char not in str_nums:
                return 'Error: Numbers must only contain digits.'

    # This count will help keep track when we reach the last operation
    count = 0

    # We use a for loop to loop through all of the operations that we have to calculate
    for operand in operators:
        # Grab the first and second number in the first set of numbers and cast the string as an int so that we can perform arithematic
        first = int(first_row[count])
        second = int(second_row[count])

        # Check the operator associated with this set of numbers
        if operand == "+":
            # If "+", then we calculate the sum
            sum = first + second

            # Add the sum to the answers list
            answers.append(str(sum))

            # Increase the count so that we move to the next set of numbers in the next round of the for loop
            count += 1
            
        else:
            # Else "-", then we calculate the difference
            diff = first - second

            # Add the difference to the answers list
            answers.append(str(diff))

            count += 1

    # Add extra spaces to the numbers based on the number of digits
    for n in range(len(first_row)):
        digits_first = len(first_row[n])
        digits_second = len(second_row[n])
        digits_answer = len(answers[n])

        num_spaces = abs(digits_first - digits_second)
        # If the top number has more digits than the bottom number, we have to add spaces to the bottom number to right-align
        if digits_first > digits_second:
            second_row[n] = " " * num_spaces + second_row[n]
            dashes.append("-" * digits_first)

        # If the bottom number has more digits than the top number, we have to add spaces to the top number to right-align
        elif digits_first < digits_second:
            first_row[n] = " " * num_spaces + first_row[n]
            dashes.append("-" * digits_second)

        # If both top and bottom numbers have the same number of digits, then we dont have to do anything to right-align
        else:
            pass
            dashes.append("-" * digits_first)
    
    # Formatting the first line with all the first numbers, loop through all the numbers in the first row list
    for first in range(len(first_row)):
        # If the current number is the last number in the list, then we dont want to add 4 spaces after the number
        if first == (len(first_row) - 1):
            first_line += "  " + first_row[first]
        # Else we will add the 4 spaces after the number for the 4 spaces requirement in the problem
        else:
            first_line += "  " + first_row[first] + "    "
    
    # Formatting the second line with the operations and second numbers, loop through all the numbers in the second row list
    # The formatting is the same as the first line except there are operators involved here too
    for i in range(len(second_row)):
        if i == (len(second_row) - 1):
            second_line += operators[i] + " " + second_row[i]
        else:
            second_line += operators[i] + " " + second_row[i] + "    "

    # We remove the first index of the dashes index since it is blank (e.g., [0] = "")
    dashes = dashes[1:]

    # We loop through all the dashes to format the third line; the formatting is the same as the first line except we are working with dashes
    for _ in range(len(dashes)):
        if _ == (len(dashes) - 1):
             third_line += "--" + dashes[_]
        else:
            third_line += "--" + dashes[_]  + "    "

    # Calculating the number of spaces required to add the beginning of the answer in the fourth line
    for j in range(len(answers)):
        # Get the number of digits in the answer by acessing the answers list
        digits_answer = len(answers[j])
        # Get the number of dashes by acessing the dashes list
        num_dashes = len(dashes[j] + "--")

        # The number of additional spaces is the absolute value of the difference between the number of answer digits and the number of dashes
        ans_spaces = abs(num_dashes - digits_answer)

        # The answer will have that number of spaces added before the answer itself
        answers[j] = " " * ans_spaces + answers[j]


    # Formatting the fourth line; this is similar to the first line 
    for ans in range(len(answers)):
        if ans == (len(answers) -1):
            fourth_line += answers[ans]
        else:
            fourth_line += answers[ans] + "    "
    
    # Based on the boolean value provided by the user, we will return the formatted arithematic with the answers (TRUE) or not (FALSE)
    if show_answers:
        # With answers
        return str(first_line) + "\n" + str(second_line) + "\n" + str(third_line) + "\n" + str(fourth_line)
    else:
        # Without answers
        return str(first_line) + "\n" + str(second_line) + "\n" + str(third_line)
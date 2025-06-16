def verify_card_number(card_number):
    # Save the sum of the odd digits in the card number
    sum_of_odd_digits = 0

    # Save the reverse of the card number
    card_number_reversed = card_number[::-1]

    # Grab the odd numbers of the reversed card number
    odd_digits = card_number_reversed[::2]

    # Loop through the odd digits and add them to the sum of odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Save the sum of the even digits in the card number
    sum_of_even_digits = 0

    # Save the even numbers of the reversed card number
    even_digits = card_number_reversed[1::2]

    # Loop through the even digits
    for digit in even_digits:
        # In Luhn Algo, we take every even number and doubke it
        number = int(digit) * 2
        # If the doubled number is greater than 10, then sum the digits
        if number >= 10:
            # We use // 10 to get the first digit and % 10 to get the second digit
            number = (number // 10) + (number % 10)
        # We add the number to the sum of even digits
        sum_of_even_digits += number
    # Sum the sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    # Return True is the total is a multiple of 10, else return False
    return total % 10 == 0

# Main function
def main():
    # Give a card number to be verified
    card_number = '4111-1111-4555-1142'
    # Remove the '-' and ' ' with a empty string
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Provide a feedback if the card number is valid in terms of Luhn Algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Call the main function
main()
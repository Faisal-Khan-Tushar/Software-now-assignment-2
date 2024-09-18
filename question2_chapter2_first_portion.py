
# Function to separate numbers and letters from the string
def separate_string(input_string):
    # Creating two empty substrings: one for numbers and one for letters
    number_substring = ""
    letter_substring = ""

    # Iterating through the input string to check each character
    for char in input_string:
        # Checking if the character is a digit
        if char.isdigit():
            number_substring += char
        # Checking if the character is a letter
        elif char.isalpha():
            letter_substring += char

    return number_substring, letter_substring


# Function to convert even numbers to ASCII decimal values
def convert_even_numbers_to_ascii(number_string):
    # Creating an empty list to store ASCII values of even numbers
    even_ascii_values = []

    # Iterating through the number string to check each number
    for num in number_string:
        # Converting character to an integer
        if int(num) % 2 == 0:  # Checking if the number is even
            even_ascii_values.append(ord(num))  # Converting even number to ASCII value

    return even_ascii_values


# Function to convert uppercase letters to ASCII decimal values
def convert_uppercase_letters_to_ascii(letter_string):
    # Creating an empty list to store ASCII values of uppercase letters
    uppercase_ascii_values = []

    # Iterating through the letter string to check each letter
    for letter in letter_string:
        # Checking if the letter is uppercase
        if letter.isupper():
            uppercase_ascii_values.append(ord(letter))  # Converting uppercase letter to ASCII value

    return uppercase_ascii_values


# Main code block

# Taking input from the user (ensuring the string is at least 16 characters long)
input_string = input("Enter a string (at least 16 characters long, containing numbers and letters): ")

# Ensuring the input string is valid (minimum 16 characters)
if len(input_string) < 16:
    print("Error: The string must be at least 16 characters long.")
else:
    # Separating the string into number and letter substrings
    number_substring, letter_substring = separate_string(input_string)

    # Displaying the separated substrings
    print("Number Substring:", number_substring)
    print("Letter Substring:", letter_substring)

    # Converting even numbers to ASCII decimal values
    even_ascii_values = convert_even_numbers_to_ascii(number_substring)
    print("ASCII values of even numbers:", even_ascii_values)

    # Converting uppercase letters to ASCII decimal values
    uppercase_ascii_values = convert_uppercase_letters_to_ascii(letter_substring)
    print("ASCII values of uppercase letters:", uppercase_ascii_values)

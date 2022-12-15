
import string
import random


# characters to generate password from
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*" + "()")

def generate_random_password():
    # length of password from the user
    letter_count = int(input("Enter the desired amount of letters: "))

    # amount of numbers in password
    number_count= int(input("Enter the desired number count: "))

    # amount of special characters in password
    spec_char_count = int(input("Enter the desired special character count: "))

    # picking random characters from the list
    password = []
    for i in range(letter_count):
        password.append(random.choice(letters))

    for i in range(number_count):
        password.append(random.choice(numbers))
    
    for i in range(spec_char_count):
        password.append(random.choice(special_characters))


    # shuffling the resultant password
    random.shuffle(password)

	
	# printing the list
    print("".join(password))

    length = str(letter_count + number_count + spec_char_count)

    print("Your password is " + length + " characters long.")


## invoking the function
generate_random_password()


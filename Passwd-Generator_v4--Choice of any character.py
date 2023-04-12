import secrets
import string
import random

# characters to generate password from
letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list("!@#$%^&*" + "()")

def generate_random_password():
		# amount of letters in password with input validation
		while True:
			try:
				letter_count = int(input("Enter the desired amount of letters: "))
			except ValueError:
				print("Please use numbers only. No spaces, no special characters- just numbers.")
				continue
			else:
				break
			# amount of numbers in password
		while True:		
			try:
				number_count= int(input("Enter the desired amount of numbers: "))
			except ValueError:
				print("Please use numbers only. No spaces, no special characters- just numbers.")
				continue
			else:
				break
			# amount of special characters in password
		while True:	
			try:
				spec_char_count = int(input("Enter the desired amount of characters: "))
			except ValueError:
				print("Please use numbers only. No spaces, no special characters- just numbers.")
				continue
			else:
				break
		# picking random characters from the list
		password = []
		for i in range(letter_count):
			password.append(secrets.choice(letters))

		for i in range(number_count):
			password.append(secrets.choice(numbers))
		
		for i in range(spec_char_count):
			password.append(secrets.choice(special_characters))

		# shuffling the resultant password
		random.shuffle(password)

		
		# printing the list
		print("".join(password))

		length = str(letter_count + number_count + spec_char_count)

		print("Your password is " + length + " characters long.")


## invoking the function with error handling
generate_random_password()


""" Accredited links:
		Input validation and loop:
  			https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
		Entropy:
			https://docs.python.org/3/library/secrets.html
		Password generator base idea:
			https://gist.github.com/23maverick23/4131896
"""
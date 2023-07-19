# Breanna Blackwood

def encode(password):
	""" Encodes the user's inputted password by incrementing each number by 3."""
	encoded_password = []  # create empty list
	for num in password:  # increment each number in password by 3 for encoding
		new = int(num) + 3
		encoded_password.append(str(new))  # add the new number to the list
	enc = "".join(encoded_password)  # join the components of the list together
	return enc

def decoder(string):
	final = ''
	for char in string:
		char = int(char)
		result = char - 3
		result = str(result)
		final += result
	return final


def main():
	# print the menu
	while True:
		print("Menu\n-------------")
		print("1. Encode\n2. Decode\n3. Quit")
		print("\nPlease enter an option:", end=" ")
		opt = int(input())
		if opt == 1:  # implement encode function
			print("Please enter your password to encode:", end=" ")
			pw = input()
			encode(pw)
			print("Your password has been encoded and stored!")
		elif opt == 2:  # Cyara Meza: added decoder method and implemented it here in opt 2.
			decoded_pass = decoder(encode(pw))
			print(f"The encoded password is {encode(pw)}, and the original password is {decoded_pass}.")
		elif opt == 3:  # exit the program
			exit()
		else:
			print("Please enter a value between 1 and 3.")



if __name__ == "__main__":  # run the main function
	main()

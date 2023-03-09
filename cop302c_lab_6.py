# Sophya Wodchis
# COP3502C: Lab 6 (Encode)
# encodes the password
def encode(password):
	enc_pass = ""
	for x in password:
		# encodes by adding three to each integer
		enc_pass = enc_pass + str((int(x) + 3) % 10)
	# return statement
	return enc_pass

# main function
def main():
	while True:
		# main section of the program to display options for the user
		print(f'Menu')
		print(f'-------------')
		print(f'1. Encode')
		print(f'2. Decode')
		print(f'3. Exit')

		enc_pass = 0

		# collects user's selection
		choice = input('Please enter an option: ')

		# based on choice decodes, encodes, or exits program
		if choice in ('1', '2', '3'):
			if choice == '1':
				# collects the password from the user
				dec_pass = str(input('Please enter your password to encode: '))
				# stores encoded password
				enc_pass = encode(dec_pass)
				print(f'Your password has been encoded and stored!')
			elif choice == '2':
				# only if password has been encoded and stored
				if enc_pass != 0:
					print(f'The encoded password is {enc_pass}, and the original password is .') # add decoding function
				else:
					print('No password has been encoded yet.')
			elif choice == '3':
				break
		elif choice:
			print('Error: Invalid selection!')


if __name__ == '__main__':
	main()



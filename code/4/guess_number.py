import random			# A random number generator function
guess_number = random.randint(1, 100) 	# Generating integer random number between 1 and 100
print ("Guess number (1 ~ 100)")
users_input = int(input())	     	# Conver user input to integer type
while (users_input is not guess_number):    	# Determine if user input is equal to number of the generated random number
    if users_input > guess_number: 	# If user input is bigger
        print ("The number is bigger than random number")
    else: 		    		# If user input is smaller
        print ("The number is smaller than random number")
    users_input = int(input())	# Re-enter user input
else:
    print ("That's true. ",
        "The input number is", users_input)	# End condition

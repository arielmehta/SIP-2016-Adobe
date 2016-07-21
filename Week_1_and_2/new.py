number = 79
guess = input("Guess my favorite number!")


while number != int(guess):
	if number < int(guess):
		print("That is too high!!")
		guess = input("Try again!")
	elif number > int(guess):
		print("That is too low!")
		guess = input("Try again!")


if number == int(guess):
	print("You win!!")
	
	print("Game Over!")

print("You wake up one morning and find that you aren’t in your bed; you aren’t even in your room. You’re in the middle of a giant maze. A sign is hanging from the ivy: You have one hour. Don’t touch the walls. There is a hallway to your right and to your left.")





print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
	print("You decide to go left and you see an old man that resembles Gandalf at the end of the hall. He says he can give you either another 30 minutes to get out of the maze, or he can tell you which way to go next  ") 
	print("Type '30 mins' or 'next step'")
	user_input= input()
	if user_input== "30 mins":
		print("Interesting choice young child... Your request is granted. You continue down the hall and start to get scared as you see graffiti and dried blood on the walls. You start running as fast as you can and suddenly bump into an evil looking creature who says he knows how to get out of the maze. Will you fight him or follow him. ")
		print("Type 'fight' or 'follow'")
		user_input= input()
		if user_input== "fight":
			print("You easily defeat the slimy creature! His body decays in a few seconds and a key emerges from his remains. The key has a note attached to it: ' use me to get through any walls' Do you use the key to get through the wall right next to you or put it in your pocket for later use ")
			print("Type 'go through wall' or 'pocket it'")
			user_input= input()
			if user_input== "go through wall":
				print( "Nice risk taking! You see the opening of the maze above and make it out successfully! yay! ")
			elif user_input== "pocket it":
				print("You continue running, but time is running out! You start to hyperventilate. A farmer with a pitchfork and a cow calls out from behind you. He tells you he thinks he has figured out how to get out. Do you follow him, or kill him like you did to the slimy creature in hopes of finding another key or answer?")
				print(" Type 'kill' or 'trust and follow' ")
				user_input= input()
				if user_input== "kill":
					print("You kill him and a voice on the load speaker tells you that you have killed an innocent soul and will now die for your actions. GAME OVER!!")
				elif user_input== "trust and follow":
					print("Good Choice! The farmer does indeed know how to get out! You make it out and thank him for saving you in time! yay!")
		elif user_input == "trust and follow":
			print("You follow the creature to a dark hole, where he corners you and cooks you up for dinner. You die. GAME OVER!")
	elif user_input == "next step":
		print("Good Choice! Follow down this path and take a right. You do as the man says and you find a wad of money. Do you pick up the wad of money or run past it because you don't want to waste time.")
		print("Type 'Pick it up' or 'leave it and run' ")
		user_input= input()
		if user_input== "pick it up":
			print("Picking up the money detonated a bomb and you blow up! GAME OVER!!")
		elif user_input== "leave it and run":
			print("You made the right choice! You see the end of the maze and make it out alive! Yay!! ")
elif user_input == "right":
    print("You choose to go right and are eaten by a dinosaur! Game over!") 

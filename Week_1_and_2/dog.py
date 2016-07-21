class Dog():
	# Constructor Function
	def __init__(self, furColor, weight, eyeColor, name):
		self.furColor= furColor
		self.weight = weight
		self.eyeColor = eyeColor
		self.name = name

	# function
	def bark(self):
		#function that makes bark sound
		print("Woof")

	def wag(self):
		#function that makes tail move
		print("wagging tail!")

Toto = Dog("Brown", 30, "Brown", "Toto")

Toto.bark()
Toto.wag()
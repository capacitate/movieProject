class Parent():
	def __init__(self, last_name, eye_color):
		print "Parent constructor called"
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info(self):
		print("Last name " + self.last_name)
		print("Eye color " + self.eye_color)

class Child(Parent):
	def __init__(self, last_name, eye_color, num_of_toys):
		print "Child constructor called"
		Parent.__init__(self, last_name, eye_color)
		self.num_of_toys = num_of_toys

	def show_info(self):
		print("Last name " + self.last_name)
		print("Eye color " + self.eye_color)
		print("Num of toys " + str(self.num_of_toys))

billy_cyrus = Parent("cyrus", "blue")
# print billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()
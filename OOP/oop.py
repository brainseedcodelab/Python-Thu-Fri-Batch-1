#18.10.2019

#Classes

# class Person:
# 	pass #An empty block

# p = Person()	
# print(p)


#Methods

# class Person:
# 	def say_hi(self):
# 		print('Hello, how are you?')

# p = Person()
# p.say_hi()


# __init__ method

# class Person:
# 	def __init__(self, name):
# 		self.name = name

# 	def say_hi(self):
# 		print('Hello,my name is ', self.name)

# p = Person('Swaroop')
# p.say_hi()

# dog = dog('Name')
# dog.color = black
# dog.owner = 
# dog.function() - bark
# 			   - eat
# 			   - sleep
# 			   - bite 


#Class And Object Variables

class Robot:
	"""Represents a robot,with a name."""

	population = 0

	def __init__(self,name):
		"""Initializes the data."""

		self.name = name
		print("(Initializing{})".format(self.name))

		Robot.population += 1

	def die(self):
		"""I am dying."""

		print("{} is being destroyyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(
				Robot.population))	

	def say_hi(self):
		""""Greeting by the robot.	

		Yeah, they can do that."""		

		print("Greetings, my sisters call me{}.".format(self.name))


	@classmethod
	def how_many(cls):
			"""Prints the current population."""
			print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot ("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work.so let's destory them")
droid1.die()
droid2.die()

Robot.how_many()	


#Inheritance


class ShcoolMember:
	'''Represents any school member.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized ShcoolMember: {})'.format(self.name))


	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")


class Teacher(SchoolMember):
	'''Represents a student.'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))


class Student(SchoolMember)
	'''Represents a Student'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))	



t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)


print()


members =[t,s]
for member in members:
	membr.tell()						
class students_class:
	def __init__ ( self , name , age ) :
		self.name = name
		self.age = age
		
	def checkage(self) :
		if self.age < 18 :
			print("Underage")
			
		else:
			print("18 or abofe")



student_1 = students_class("ABC" , 15)
student_2 = students_class("DEF" , 20)


student_1.checkage()
student_2.checkage()
print()
print(student_1.name)
print(student_1.age)
print()
print(student_2.name)
print(student_2.age)

student_1.age = 20
student_1.name = "123"
print()
print(student_1.name)
print(student_1.age)


del student_1.age
del student_1
	
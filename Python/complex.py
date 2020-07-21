from math import sqrt

class Complex():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	
	def display(self):
		if self.b>=0:
			print(str(self.a)+"+"+str(self.b)+"i")
		else:
			print(str(self.a)+str(self.b)+"i")
	
	def add(self,z):
		self.a=self.a+z.a 
		self.b=self.b+z.b

	def subtract(self,z):
		self.a=self.a-z.a 
		self.b=self.b-z.b

	def multiply(self,z):
		self.a=self.a*z.a-self.b*z.b
		self.b=self.a*z.b+self.b*z.a

	def modulus(self):
		z=sqrt((self.a)**2+(self.b)**2)
		return z

	def conjugate(self):
		self.b=self.b*(-1)
		return Complex(self.a,self.b)

	def inverse(self):
		a_new=self.a/self.modulus()
		b_new=(-1)*self.b/self.modulus()
		return Complex(a_new,b_new)





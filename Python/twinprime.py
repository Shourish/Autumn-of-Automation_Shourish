
x=int(input("Enter number of digits:"))

def isprime(p):
	temp=0
	for k in range(2,p+1):
		if p%k==0:
			temp+=1

	if temp==1:
		return True
	else: 
		return False

		
def main():
	f=open("myFirstFile.txt","w")

	for z in range(10**(x-1)+2,10**x):
		if isprime(z) and isprime(z-2):

			f.write(str(z-2) + " " + str(z) + "\n")

		else:
			continue

main()
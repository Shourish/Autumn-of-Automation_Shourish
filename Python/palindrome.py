def isPalindrome(p):
	s=str(p)
	temp=0
	for z in range(0,int(len(s)/2)):
		if s[z]==s[len(s)-z-1]:
			temp+=1

		else:
			return False
			break
	if temp==int(len(s)/2):
		return True


def main():
	
	while True:
		x=int(input("Enter palindrome:"))
		if isPalindrome(x):
			temp2=x+1
			while True:
				if isPalindrome(temp2):
					print(temp2)
					break
				else:
					temp2+=1
			break
		else:
			print("Number is not a palindrome. Please enter again.")


main()

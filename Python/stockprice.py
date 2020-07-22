
n=int(input("Enter number of days:"))
lst=[]
for x in range(0,n):
	z=input("Enter price of stock on day {day}:".format(day=x+1))
	lst.append(z)

temp=0
buy=0
sell=0

for p in range(0,n-1):
	for q in range(p+1,n):
		if lst[q]-lst[p]>temp:
			temp=lst[q]-lst[p]
			buy=p+1
			sell=q+1

print(temp)
print(buy)
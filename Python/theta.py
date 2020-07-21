import numpy as np

#input array y here
y=np.array([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1,1,1,1,1])

y=y.astype(np.int32)


x=np.random.normal(loc=0,scale=1,size=(20,20))


theta=np.linalg.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)

print(theta)

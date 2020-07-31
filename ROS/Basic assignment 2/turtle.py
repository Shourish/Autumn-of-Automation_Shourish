#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32
import time

x_in=Float32()
y_in=Float32()
theta_in=Float32()
linear_velocity_in=Float32()
angular_velocity_in=Float32()
out=Twist()


def publisher():
	pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	rospy.init_node('my_initials',anonymous=True)
	


	global out
	out.linear.x = 1
	out.linear.y = 0
	out.linear.z = 0
	out.angular.x = 0
	out.angular.y = 0
	out.angular.z = 0


	while not rospy.is_shutdown():

		if out.linear.x==1:
			t0=time.time()
			t1=0
		
			while (t1-t0<2):
				pub.publish(out)
				t1=time.time()
				
			out.linear.x=0
			out.angular.z=1
			t0=time.time()
			t1=0
			while (t1-t0<1.57):
				pub.publish(out)
				t1=time.time()
				
			out.angular.z=0
			out.linear.x=1
			t0=time.time()
			t1=0
			while (t1-t0<2):
				pub.publish(out)
				t1=time.time()
				
			out.linear.x=0
			out.angular.z=1
			t0=time.time()
			t1=0
			while (t1-t0<1.57):
				pub.publish(out)
				t1=time.time()
				
			out.angular.z=0
			out.linear.x=1
			t0=time.time()
			t1=0
			while (t1-t0<2):
				pub.publish(out)
				t1=time.time()
				
			out.linear.x=0
			out.angular.z=-1
			t0=time.time()
			t1=0
			while (t1-t0<1.57):
				pub.publish(out)
				t1=time.time()
				
			out.angular.z=0
			out.linear.x=1
			t0=time.time()
			t1=0
			while (t1-t0<2):
				pub.publish(out)
				t1=time.time()
				
			out.linear.x=0
			out.angular.z=-1
			t0=time.time()
			t1=0
			while (t1-t0<1.57):
				pub.publish(out)
				t1=time.time()
				
			out.angular.z=0
			out.linear.x=1
			t0=time.time()
			t1=0
			while (t1-t0<2):
				pub.publish(out)
				t1=time.time()
				




			out.linear.x = 0
			out.linear.y = 0
			out.linear.z = 0
			out.angular.x = 0
			out.angular.y = 0
			out.angular.z = 0
			pub.publish(out)


if __name__=='__main__':
	try:
		publisher()

		
	except rospy.ROSInterruptException:
		pass
	
	
	




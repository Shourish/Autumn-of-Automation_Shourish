#!/usr/bin/env python

import rospy
import math
from umic_assignment.msg import quaternions
from umic_assignment.msg import euler
from std_msgs.msg import Float64

x_in=Float64()
y_in=Float64()
z_in=Float64()
w_in=Float64()

out=euler()


def quaternion_to_euler(x, y, z, w):

        t0 = 2 * (w * x + y * z)
        t1 = 1 - 2 * (x * x + y * y)
        X = math.atan2(t0, t1)

        t2 = 2 * (w * y - z * x)
        t2 = 1 if t2 > 1 else t2
        t2 = -1 if t2 < -1 else t2
        Y = math.asin(t2)

        t3 = 2 * (w * z + x * y)
        t4 = 1 - 2 * (y * y + z * z)
        Z = math.atan2(t3, t4)

        return X, Y, Z

def callback(var):
	print('callback working')
	global x_in
	global y_in
	global z_in
	global w_in
	x_in=var.x
	y_in=var.y
	z_in=var.z
	w_in=var.w

	

def publisher():
	pub=rospy.Publisher('topic2',euler, queue_size=10)
	rospy.init_node('my_convertor',anonymous=True)
	rate=rospy.Rate(10)
	global out
	while not rospy.is_shutdown():
		#print('publisher working')
		rospy.Subscriber('topic1', quaternions, callback)
		roll, pitch, yaw= quaternion_to_euler(x_in.data,y_in.data,z_in.data,w_in.data)
		out.roll=roll
		out.pitch=pitch
		out.yaw=yaw
		pub.publish(out)
		#print(out)
	rate.sleep()

if __name__=='__main__':
	try:
		publisher()

	except rospy.ROSInterruptException:
		pass


	
	

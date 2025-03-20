import rospy # biblioteca principal de python, para 
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, radians
import time

def move_turtle(pub, linear, angular, duration):
    msg = Twist()
    msg.linear.x = linear
    msg.angular.z = angular
    
    start_time = rospy.Time.now().to_sec()
    while rospy.Time.now().to_sec() - start_time < duration:
        pub.publish(msg)
        rospy.sleep(0.1)
    
    msg.linear.x = 0
    msg.angular.z = 0
    pub.publish(msg)
    rospy.sleep(0.5)

def draw_number(pub, number):
    for digit in str(number):
        if digit == '1':
            move_turtle(pub, 1, 0, 1)
        elif digit == '7':
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, -1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
        elif digit == '2':
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, -1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, -1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
        elif digit == '5':
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, -1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, 1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
        elif digit == '6':
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, -1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 0, 1.57, 0.5)
            move_turtle(pub, 1, 0, 1)
            move_turtle(pub, 1, 0, 1)
        rospy.sleep(1)

def main():
    rospy.init_node('turtle_draw_number', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.sleep(2)
    
    draw_number(pub, 172562)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
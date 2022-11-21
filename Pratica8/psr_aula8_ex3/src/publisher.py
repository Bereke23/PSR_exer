#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
import argparse

def main():
    # ---------------
    # Inicialization
    # ---------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t','--topic',type = str, required= False, default='chatter')
    parser.add_argument('-msg','--msge',type = str, required= False, default='hello world this is bereke')
    parser.add_argument('-f','--freq',type = int, required= False, default=1)
    args = vars(parser.parse_args())



    #Initialisation of ros node 
    rospy.init_node('publisher', anonymous=True)# de modo como ele é registado no 
    # ecosistema do ros a dizer eu sou um node eu vou comunicar com outros node ros
    # Create the publisher / someone who will send info
    publisher = rospy.Publisher(args['topic'], String, queue_size=10)
    # chatter => topic name, o topic é canal atraves do qual ocorre a comunicação 
    
    # ---------------
    # Execution
    # ---------------
    rate = rospy.Rate(args['freq']) # 1hz
    while not rospy.is_shutdown(): # This cycle is going to run until something bad happens with ros
        msg = args['msge'] + '  ' +  str(rospy.get_time())
        rospy.loginfo('Publishing ' + msg)
        publisher.publish(msg)
        rate.sleep()
    # ---------------
    # Termination
    # ---------------


if __name__ == '__main__':
    main()

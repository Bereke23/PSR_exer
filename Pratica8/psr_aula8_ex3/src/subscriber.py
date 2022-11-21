#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import argparse

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    # ---------------
    # Inicialization
    # ---------------
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-t','--topic',type = str, required= False, default='chatter')
    args = vars(parser.parse_args())

    # O subscriber é o nome caso outro node queira entrar na conversa
    # ele não pode ter o mesmo nome
    # Mas o anonymous true permite que dois nodes com o mesmo nome entrem na conversa
    # Pois, isso consegue-se atraves de acrescentar um determinado numero ao nome do subscriber
    # É o que anonymos no modo true faz
    rospy.init_node('subscriber', anonymous=True)
    # Init subscriber/ someone who will just listen to info
    rospy.Subscriber(args['topic'], String, callback)
    # ---------------
    # Execution
    # ---------------

    rospy.spin()

    # ---------------
    # Termination
    # ---------------

if __name__ == '__main__':
    listener()

#! /usr/bin/env python

import rospy
import rospkg
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('service_move_bb8_in_square_client')
rospy.wait_for_service('/move_bb8_in_square')
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square', Empty)
move_bb8_in_square_service_object = EmptyRequest()

result = move_bb8_in_square_service_client(move_bb8_in_square_service_object)
print result
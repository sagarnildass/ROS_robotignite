#! /usr/bin/env python

import rospy
import rospkg
from unit_3_services.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('service_move_bb8_in_square_custom_client')
rospy.wait_for_service('/move_bb8_in_square_custom')
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
move_bb8_in_square_service_object = BB8CustomServiceMessageRequest()


move_bb8_in_square_service_object.side = 0.1
move_bb8_in_square_service_object.repetitions = 2

rospy.loginfo("Start two small squares")
result = move_bb8_in_square_service_client(move_bb8_in_square_service_object)
rospy.loginfo(str(result))

move_bb8_in_square_service_object.side=0.6
move_bb8_in_square_service_object.repetitions=1

rospy.loginfo("Start One Big Square...")
result = move_bb8_in_square_service_client(move_bb8_in_square_service_object) # Send through the connection the path to the trajectory file to be executed
rospy.loginfo(str(result))

rospy.loginfo("END of Service call...")

result = move_bb8_in_square_service_client(move_bb8_in_square_service_object)
print result
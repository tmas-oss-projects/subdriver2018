#!/usr/bin/env python

from sub import *

# define state Foo
class start(sub):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Not_Found_Gate', 'Found_Gate'])
        

    def execute(self, userdata):
        gbl.run_start_time = rospy.get_time()
        self.init_state()
        rospy.loginfo("Run Start Time: " + str(gbl.run_start_time))

        gbl.init_depth = gbl.altitude

    	curr_msg = self.init_joy_msg()
    	curr_msg.axes[self.axes_dict['vertical']] = -1
    	curr_msg.axes[self.axes_dict['frontback']] = 1

    	self.joy_pub.publish(curr_msg)

        gbl.current_target = self.class_dict['start_gate']

        return 'Not_Found_Gate' # Debug Purpuses Only!


        while(1):
            if rospy.get_time() > (gbl.run_start_time + 15):
                if self.get_box_of_class(gbl.boxes, self.class_dict['start_gate']):
                    return 'Found_Gate' # Transitions to TRACK_GATE
                else:
                    return 'Not_Found_Gate' # Transitions to SEARCH_FRONT_GATE


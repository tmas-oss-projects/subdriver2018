#!/usr/bin/env python

import rospy
import smach
import smach_ros

# define state Foo
class search_front(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Found_Object','Not_Found_Object'])

    def log(self):
    	pass

    def execute(self, userdata):
    	self.log()
        return 'Found_Object'

#!/usr/bin/env python3
from ros_service_tutorial.srv import *
import rospy
from urllib3 import PoolManager

manager = PoolManager(10)


def handle_add_two_ints(req):
    date = manager.request('GET', 'http://www.naver.com').headers['Date']
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    return AddTwointsResponse(req.a + req.b, date)


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoints, handle_add_two_ints)
    print("ready")
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()

#!/usr/bin/env python3

import sys
import rospy
import time
from ros_service_tutorial.srv import *


def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoints)
        resp1 = add_two_ints(x, y)
        return resp1.time, resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [x y]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)

    while True:
        print("Requesting %s + %s" % (x, y))
        print("[%s] sum = %s " % (add_two_ints_client(x, y)))
        time.sleep(5)
#!/usr/bin/env python3

import pygame
import rospy

from controller_configurator.msg import Controller

class JoystickPublisher(object):
    def __init__(self, query_rate=20):
        pygame.init() #type:ignore
        pygame.joystick.init()
        self.j0 = pygame.joystick.Joystick(0)

        self.query_rate = query_rate
        self.timer_loop = None

        self.controller_publisher = rospy.Publisher('controller', Controller, queue_size=5)

    def shutdown(self):
        self.stop()
        pygame.quit() #type:ignore
        self.controller_publisher.unregister()

    def stop(self):
        if self.timer_loop is not None:
            self.timer_loop.shutdown()

    def start(self):
        self.timer_loop = rospy.Timer(rospy.Duration(1/self.query_rate), self.query)

    def query(self, event):
        del event
        self.j0.init()
        pygame.event.get()

        msg = Controller()

        msg.axis_count = self.j0.get_numaxes()
        msg.axis_state = []
        for j in range(msg.axis_count):
            msg.axis_state.append(self.j0.get_axis(j))

        msg.button_count = self.j0.get_numbuttons()
        msg.button_state = []
        for b in range(msg.button_count):
            msg.button_state.append(self.j0.get_button(b))

        msg.hat_count = self.j0.get_numhats()
        msg.hat_state = []
        for h in range(msg.hat_count):
            msg.hat_state.append(True if self.j0.get_hat(h)[0] == 1 else False)
            msg.hat_state.append(True if self.j0.get_hat(h)[0] == -1 else False)
            msg.hat_state.append(True if self.j0.get_hat(h)[1] == 1 else False)
            msg.hat_state.append(True if self.j0.get_hat(h)[1] == -1 else False)
        msg.hat_count *= 2

        self.controller_publisher.publish(msg)

def main():
    rospy.init_node('controller_publisher', anonymous=False)
    jp = JoystickPublisher()
    rospy.on_shutdown(jp.shutdown)

    jp.start()
    rospy.loginfo('Controller node ready to go!')
    rospy.spin()
    rospy.loginfo('Controller node shut down.')

if __name__ == '__main__':
    main()

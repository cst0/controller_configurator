#!/usr/bin/env python3

from controller_configurator.controller_configurator_utils import common
import argparse
import rospy

class ControllerConfiguratorAutogen:
    def __init__(self):
        common.init_controllers()
        ctrlr = common.get_controller_state()

        parser = argparse.ArgumentParser(description="Autogenerate functionality for a controller with your robot!")
        parser.add_argument('--publishers', nargs='+', help='On what topics will we need to be publishing?')
        parser.add_argument('--subscribers', nargs='+', help='On what topics will we need to be subscribed?')

        parser.add_argument('--joysticks', nargs='+', help='What joysticks should we be configuring? Defaults to all.')
        parser.add_argument('--buttons', nargs='+', help='What buttons should we be configuring? Defaults to all.')

        args = parser.parse_args(rospy.myargv())

        pub_topics = []
        for pub in args.publishers:
            pub_topics.append(common.get_topic_data(pub))
        sub_topics = []
        for sub in args.subscribers:
            sub_topics.append(common.get_topic_data(sub))

def main():
    cca = ControllerConfiguratorAutogen()

if __name__ == '__main__':
    main()

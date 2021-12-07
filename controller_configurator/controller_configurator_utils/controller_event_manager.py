from controller_configurator.controller_configurator_utils import common
import rospy

class ControllerManager(object):
    def __init__(self):
        self.attached_functions = {}
        self.publishers = {}
        self.subscribers = {}

    def on_start(self):
        pass

    def on_shutdown(self):
        self.safe_detatch()

    def safe_detatch(self):
        pass

    def attach(self, control_type:common.ControlType, action:function, response_type:common.ResponseType=common.ResponseType.ALWAYS):
        self.attached_functions[control_type] = (action, response_type)

class ControllerEventManager:
    def __init__(self, controller:ControllerManager, hz=30):
        pass

    def loop(self):
        pass

    def shutdown(self):
        pass

    def start(self):
        pass

def get_controller_manager():
    return ControllerManager()

def main():
    rospy.init_node('ConfiguredController', anonymous=False)
    cem = ControllerEventManager(get_controller_manager())
    rospy.on_shutdown(cem.shutdown)

if __name__ == '__main__':
    main()

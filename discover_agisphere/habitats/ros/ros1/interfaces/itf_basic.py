# Copyright (c) 2024-2028, The Discover Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: MIT

"""ROS1 basic interfaces.
This script contains the basic interfaces of Orbit simulation platform.
"""

from discover_agisphere.habitats.ros.ros1.configs import cfg_basic


class Originate:
    def __init__(self, config:cfg_basic.ConfigOriginate):
        # append AppLauncher cli args
        pass
    
    def is_running(self):
        return True
    
    def close(self):
        pass
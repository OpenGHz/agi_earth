# Copyright (c) 2024-2028, The Discover Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: MIT

"""Gazebo basic interfaces.
This script contains the basic interfaces of Orbit simulation platform.
"""

from discover_agisphere.habitats.sim.gazebo.configs import cfg_basic
from discover_agisphere.champaign.habitat.interface import com_basic as itf_basic


class Originate(itf_basic.ComOriginate):
    def __init__(self, config:cfg_basic.ConfigOriginate):
        super().__init__("gazebo")
        pass
    
    def is_running(self):
        return True
    
    def close(self):
        pass
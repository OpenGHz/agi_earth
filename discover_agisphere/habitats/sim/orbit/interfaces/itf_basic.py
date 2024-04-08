# Copyright (c) 2024-2028, The Discover Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: MIT

"""ORBIT basic interfaces.
This script contains the basic interfaces of Orbit simulation platform.
"""

from discover_agisphere.habitats.sim.orbit.configs import cfg_basic
from discover_agisphere.champaign.habitat.interface import com_basic as itf_basic

from omni.isaac.orbit.app import AppLauncher


class Originate(itf_basic.ComOriginate):
    def __init__(self, config:cfg_basic.ConfigOriginate):
        super().__init__("orbit")
        # append AppLauncher cli args
        parser = config.parser
        AppLauncher.add_app_launcher_args(parser)
        # parse the arguments
        args_cli = parser.parse_args()
        # launch omniverse app
        app_launcher = AppLauncher(headless=args_cli.headless)
        simulation_app = app_launcher.app
        self.habitat = simulation_app
    
    def is_running(self):
        return self.habitat.is_running()
    
    def close(self):
        self.habitat.close()
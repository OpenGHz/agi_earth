from discover_agisphere.champaign.habitat.config import com_basic as cfg_com_basic
from discover_agisphere.champaign.habitat.interface import com_basic as itf_com_basic
from typing import Any, Union

# use try to check the existence of the packages
HABITATS_STATE = {}
AVILIBLE_HABITAT_TYPES = ["orbit", "gazebo", "ros1"]

# ros1
try:
    from discover_agisphere.habitats.ros.ros1.configs import cfg_basic as ros1_cfg_basic
    from discover_agisphere.habitats.ros.ros1.interfaces import itf_basic as ros1_itf_basic
except ImportError as e:
    HABITATS_STATE["ros1"] = e
else:
    HABITATS_STATE["ros1"] = None

# gazebo
try:
    from discover_agisphere.habitats.sim.gazebo.configs import cfg_basic as gazebo_cfg_basic
    from discover_agisphere.habitats.sim.gazebo.interfaces import itf_basic as gazebo_itf_basic
except Exception as e:
    HABITATS_STATE["gazebo"] = e
else:
    HABITATS_STATE["gazebo"] = None

# orbit
try:
    from discover_agisphere.habitats.sim.orbit.configs import cfg_basic as orbit_cfg_basic
    from discover_agisphere.habitats.sim.orbit.interfaces import itf_basic as orbit_itf_basic
except ImportError as e:
    HABITATS_STATE["orbit"] = e
else:
    HABITATS_STATE["orbit"] = None

# get all the available habitats
AVAILABLE_HABITATS = [k for k, v in HABITATS_STATE.items() if v is None]
HABITATS_STATE["available"] = AVAILABLE_HABITATS


class HabitatSelector(object):
    def __init__(self, habitats:tuple):
        self.habitats = tuple(habitats)
        self.types = tuple([habitat.type for habitat in habitats])
        self.habitats_dict = {habitat.type: habitat for habitat in habitats}

    def get(self, type:str):
        return self.habitats_dict[type]

    def __call__(self, type:str):
        """Equal to get"""
        return self.habitats_dict[type]


def get_habitats(configs) -> Union[HabitatSelector, itf_com_basic.ComOriginate]:
    if isinstance(configs, cfg_com_basic.ComCfgOriginate):
        configs = [configs]
        one = True
    else:
        one = False
    habitats = []
    for config in configs:
        if isinstance(config, orbit_cfg_basic.ConfigOriginate):
            assert HABITATS_STATE["orbit"] is None, HABITATS_STATE["orbit"]
            habitats.append(orbit_itf_basic.Originate(config))
        elif isinstance(config, gazebo_cfg_basic.ConfigOriginate):
            assert HABITATS_STATE["gazebo"] is None, HABITATS_STATE["gazebo"]
            habitats.append(gazebo_itf_basic.Originate(config))
        elif isinstance(config, ros1_cfg_basic.ConfigOriginate):
            assert HABITATS_STATE["ros1"] is None, HABITATS_STATE["ros1"]
            habitats.append(ros1_itf_basic.Originate(config))
        else:
            raise ValueError(f"Unknown habitat config: {config}")
    if one:
        return habitats[0]
    else:
        return HabitatSelector(habitats)


if __name__ == "__main__":

    habitat_selector = HabitatSelector(AVAILABLE_HABITATS)
    habitat = habitat_selector("orbit")
    print(habitat)
    habitat = habitat_selector.get("gazebo")
    print(habitat)
    print(habitat_selector.types)
    print(habitat_selector.habitats_dict)

    # 循环等待按下Ctrl+C
    import time
    while True:
        time.sleep(1)
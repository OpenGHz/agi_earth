# use try to check the existence of the packages
HABITATS_STATE = {}

# ros
try:
    from discover_agisphere.habitats.ros import ros
except ImportError as e:
    HABITATS_STATE["ros"] = e
else:
    HABITATS_STATE["ros"] = None

# gazebo
try:
    from discover_agisphere.habitats.sim.gazebo import gazebo
except Exception as e:
    HABITATS_STATE["gazebo"] = e
else:
    HABITATS_STATE["gazebo"] = None

# orbit
try:
    from discover_agisphere.habitats.sim import orbit
except ImportError as e:
    HABITATS_STATE["orbit"] = e
else:
    HABITATS_STATE["orbit"] = None

# get all the available habitats
AVAILABLE_HABITATS = [k for k, v in HABITATS_STATE.items() if v is None]
HABITATS_STATE["available"] = AVAILABLE_HABITATS


# Path: source/extensions/discover/discover_biosphere/selection/habitat_selector.py
class HabitatSelector(object):
    def __init__(self, habitat_list):
        self.habitat_list = habitat_list
        self.habitat = None
        self.habitat_name = None
        self.habitat_id = None

    def select_habitat(self):
        self.habitat_name = self.habitat_list[0]
        self.habitat_id = 0
        self.habitat = self.habitat_list[0]
        return self.habitat

    def get_habitat(self):
        return self.habitat


def get_habitats(config):
    pass


if __name__ == "__main__":
    habitat_selector = HabitatSelector(AVAILABLE_HABITATS)
    habitat = habitat_selector.select_habitat()
    print(habitat)
    print(habitat_selector.get_habitat())
    print(habitat_selector.habitat_name)
    print(habitat_selector.habitat_id)
    print(HABITATS_STATE)

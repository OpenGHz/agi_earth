from discover_agisphere.champaign.habitat.config import com_basic
import argparse


class ConfigOriginate(com_basic.ComCfgOriginate):
    def __init__(self, args):
        self.parser:argparse.ArgumentParser = args
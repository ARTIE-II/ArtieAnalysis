"""

"""
import numpy as np
import uproot
import matplotlib.pyplot as plt

data_config = {
    "input_files": [],
}

class ArtieData:
    """
    """
    def __init__(self,
        cfg:    dict=data_config,
    ):
        self.cfg = cfg
        self.input_files = {
            key: uproot.open(key)
            for key in self.cfg["input_files"].keys()
        }

    def plot_timestamps(self,
        input_file
    ):
        data = self.input_files[input_file]
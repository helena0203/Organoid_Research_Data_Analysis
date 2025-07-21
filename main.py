import numpy as np
import pandas as pd
from src.load_and_preprocess_MS_files import load_stream_data
from src.plotting_functions import test_plot_channels
import os


def main():

    # First we define the working environment where we are
    cwd = os.getcwd()
    # TODO: Fix hardcoded sample and do auto explore
    data_path = os.path.join(cwd, "Data", "2025-06-27T11-08-461_E-00232.h5")

    # laod the stream data from the h5 file
    df_stream_0 = load_stream_data(data_path, stream_index=0)
    df_stream_1 = load_stream_data(data_path, stream_index=1)

    test_plot_channels(df_stream_0, 0)









main()
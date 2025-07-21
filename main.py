import numpy as np
import pandas as pd
from src.load_and_preprocess_MS_files import load_stream_data
from src.plotting_functions import test_plot_channels
from src.FFT_Signal import compute_fft_all_channels
from src.Cluster_Channels_PCA import get_KMeans_cluster_MS_System
import os


TEST_PLOT_STREAM = False




def main():

    # First we define the working environment where we are
    cwd = os.getcwd()
    # TODO: Fix hardcoded sample and do auto explore
    data_path = os.path.join(cwd, "Data", "2025-06-27T11-08-461_E-00232.h5")

    # laod the stream data from the h5 file
    np_stream_0 = load_stream_data(data_path, stream_index=0)

    if TEST_PLOT_STREAM == True:
        # TODO: Plot and allocate the right number of the array to the stream in the images MS
        test_plot_channels(np_stream_0, 20)

    freqs, fft_data = compute_fft_all_channels(np_stream_0)

    get_KMeans_cluster_MS_System(freqs, fft_data)

    print("Stop")







if __name__ == '__main__':
    main()





main()
import pandas as pd
import h5py


def explore_structure(file_path):
    with h5py.File(file_path, 'r') as f:
        def print_structure(name, obj):
            print(name)
        f.visititems(print_structure)


def load_stream_data(h5_path, stream_index=0):
    stream_path = f"Data/Recording_0/AnalogStream/Stream_{stream_index}"

    with h5py.File(h5_path, 'r') as f:
        signal = f[f"{stream_path}/ChannelData"][:]
        timestamps = f[f"{stream_path}/ChannelDataTimeStamps"][:]
        channels = f[f"{stream_path}/InfoChannel"]['Label'][:]

        # Decode channel names from bytes to strings
        channels = [ch.decode('utf-8') for ch in channels]

        # Convert to DataFrame: shape is (n_samples, n_channels)
        df = pd.DataFrame(signal.T, columns=channels)
        df["Time"] = timestamps

        return df



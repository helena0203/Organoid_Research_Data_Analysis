import matplotlib.pyplot as plt


def test_plot_channels(data, channel=40):

    subset = data[channel, :100_000]

    plt.plot(subset)
    plt.title(f"Channel {channel} - First 100,000 samples")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.show()
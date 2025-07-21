import matplotlib.pyplot as plt


def test_plot_channels(df, channel):

    df.plot(x="Time", y=df.columns[0])
    plt.show()
import numpy as np
import matplotlib.pyplot as plt


def plot_waveform_sweeps(data_set, sweep_number, title=None):
   
    sweep_data = data_set.get_sweep(sweep_number)

    index_range = sweep_data["index_range"]
    i = sweep_data["stimulus"][0:index_range[1]+1] # in A
    v = sweep_data["response"][0:index_range[1]+1] # in V
    i *= 1e12 # to pA
    v *= 1e3 # to mV

    sampling_rate = sweep_data["sampling_rate"] # in Hz
    t = np.arange(0, len(v)) * (1.0 / sampling_rate)

    plt.style.use('ggplot')
    fig, axes = plt.subplots(2, 1, sharex=True)
    axes[0].plot(t, v, color='black')
    axes[1].plot(t, i, color='gray')
    axes[0].set_ylabel("mV")
    axes[1].set_ylabel("pA")
    axes[1].set_xlabel("seconds")

    plt.tight_layout()
    return fig

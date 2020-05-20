from scipy import signal
import numpy as np

def prototype_filter():
    """ 

        Computes the prototype filter used in subband coding. The filter
        is a 512-point lowpass FIR h[n] with bandwidth pi/64 and stopband
        starting at pi/32
    """

    # number of lowpass points
    lowpass_points = 512

    #setting sampling frequency
    fs = np.pi

    #pass frequency
    pass_frequency = fs/128

    #stop frequency
    stop_frequency = fs/32

    #filter
    filter = signal.remez(numtaps = lowpass_points, bands = [0, pass_frequency,stop_frequency,fs],desired = [2,0], fs = 2*fs)

    return filter
import numpy as np

def subband_filtering(x, h):
    """ 

        implementing the efficient version of the subband filter
        as specified by the MP3 standard

        Arguments:
        x:  a new 512-point data buffer, in time-reversed order [x[n],x[n-1],...,x[n-511]].
        h:  The prototype filter of the filter bank

        Returns:
        s: 32 new output samples
    """

    r = np.multiply(x,h)

    q = np.arange(64) 

    c = np.sum((-1)**np.arange(8)[:, np.newaxis] * r[q + 64*np.arange(8)[:, np.newaxis]], axis=0)

    s = np.sum(np.cos(np.pi / 64. * (2 * np.arange(32)[:, np.newaxis] + 1) * (np.arange(q.shape[0]) - 16))*c, axis=1)

    return s

import numpy as np

def scaled_fft_db(x):
    """ 
        1) Computes a 512-point Hann window and use it to weigh the input data.
        2) Computes the DFT of the weighed input, take the magnitude in dBs and
        normalize so that the maximum value is 96dB.
        3) Return the first 257 values of the normalized spectrum

        Arguments:
        x: 512-point input buffer.

        Returns:
        first 257 points of the normalized spectrum, in dBs
    """

    #computing length of input buffer
    n = len(x)

    #python has an inbuilt function to return a hanning window of length n
    hanning_window = np.hanning(n)

    #applying the window along the input buffer
    y = np.multiply(x,hanning_window)

    #fourier transform of y on real values of x
    fft_y = np.fft.rfft(y)

    #taking magnitude
    abs_fft_y = np.absolute(fft_y)

    #normalizing by dividing by length of buffer
    normlized_fft_y = np.divide(abs_fft_y, n)

    #we only require the first 257 values of the normalised spectrum since input signl is real
    weighted = normlized_fft_y[0:258]

    #convert magnitude to dB's if value is 0, it is set to -100 dB
    weighted_in = [20*(np.log10(m)) if m!= 0 else -100 for m in weighted]

    #rescaling output to have a maximum of -96 dB
    weighted_in = 96 - max(weighted_in) + weighted_in

    return weighted_in[0:258]
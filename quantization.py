
import numpy as np
import math

def quantization(sample, sf, ba, QCa, QCb):
    """ 

        Arguments:
        sample: the sample to quantize
        sf:     the scale factor
        ba:     the bit allocation
        QCa:    the multiplicative uniform quantization parameter
        QCb:    the additive uniform quantization parameter

        Returns:
        The uniformly quantized sample.
    """

    power = math.pow(2, (ba-1))
    scaled = sample/sf
    q = np.floor((QCa*scaled + QCb)*power)

    return q
# Brief background on the Mp3 format
<p>Mp3 is a lossy audio compression algorithm.It is popular for its ability to greatly reduce the amount of data needed 
to encode a file at a very reasonable tradeoff, with respect to sound quality degradation.It takes advantage of a perceptual limitation of 
the human auditory system called auditory masking. Thus, the sound is encoded in such a way that the loss introduced by the encoder is in
the spectral parts of the signal we can't hear.</p>

## Simplified working process:
Mp3 encoding takes place in 3 parts:
1. Dividing the signal into smaller pieces called channels spanning the entire frequency range of the input.
2. Each channel is quantized independently using the psychoacoustic model.
3. Quantized samples are then properly formatted in a bit stream.
<p> Fourier transform is first used to estimate the energy of each channel. We then try to differentiate between the tonal and non-
tonal components of the channel. The individual masking effect for tonal and non-tonal components is computed for each critical band.
Then these results are summed together to obtain a global masking curve for the audio frame that we're analyzing.
This masking curve is mapped on to the 32 subbands. Quantization is done with respect to the psychoacoustic model.</p>
<p>The file subband_filtering implements part 1. The file scaled_fft is used to calculate the fourier transform and scaling of the input.
The file quantization implements the quantization formula on each sample. The encoder file takes in the input file and bitrate as parameters.
In this simplistic implementation of an Mp3 encoder,only bitrates in steps of 32kbps are supported (because we divide the input signal into 
32 equal parts).</p>

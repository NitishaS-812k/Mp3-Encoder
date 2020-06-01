# Mp3-Encoder
Implementation of a simple Mp3 encoder from scratch using python3 
## Libraries used:
<ul>
  <li>Numpy</li>
  <li>Scipy.signal</li>
  <li>math</li>
</ul>

## Installation:
To use this encoder to encode some .wav files(only standard integer PCM WAVE files are supported) clone this repository. Navigate to the cloned directory using terminal/cmd. To encode a .wav file, the following syntax must be used,<br>
<code>python encoder.py inwavfile.wav [outmp3file] bitrate</code><br>
To encode one of the .wav files in the samples folder( for example: sine.wav), use:<br>
<code>python encoder.py samples/sine.wav samples/sine.mp3 320</code><br>
If the name of the output file isn't provided, the output file will be created having the same name and a .mp3 extension. The last argument passed to the file is the bitrate. Bitrates starting from 64kbps to 448 kbps with steps of 32kbps are supported. Lower bitrates compress the file more reducing quality and size of the file and vice versa.

# Copyright 2017 Nick VanDeusen nv314961@bu.edu

# WAV file support
import scipy.io.wavfile as wavfile

# arrays
import numpy

# plotting facilities
import matplotlib.pyplot as pyplot

fname = "bachish.wav"

def read_wave(fname, debug=False):
    "return a time signal read from the WAV file fname"
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim > 1:
        nframes, nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music, frame_rate, nframes, nchannels
	
def loudest_band(music, frame_rate, bandwidth):
	N = music.size
	T = music.size/frame_rate
	df = 1/T
	music_coef = numpy.fft.fft(music) # time -> frequency domain
	music_freq = numpy.fft.fftfreq(N)*frame_rate
	#df = 
	# Determine location of the highest amplitude sample in music_coef
	# Only need to parse the first half of music_coef; input is real,
	# so the ft is conjugate symmetric_difference
	loud_area = music_coef[0:(music.size-1)//2].argmax()
	# Calculate bounds of bandwidth (centered at loud_area)
	loud_freq = music_freq[loud_area]
	
	mag = 0
	best_mag = 0
	low = 0
	high = 0
		
	for i in range(0, int(bandwidth)):
		templow = loud_area - i
		temphigh = templow + int(bandwidth)

		if templow < 0 or temphigh >= music.size//2:
			continue
		mag = music[templow:temphigh-1].real.sum()
		if mag >= best_mag:
			best_mag = mag
			low = templow
			high = temphigh
	
	# frequency values to pass
	low_bandpass = numpy.arange(low, high)
	high_bandpass = numpy.arange(music.size - high, music.size - low)
	bandpass = numpy.append(low_bandpass, high_bandpass)
	
	loudest = numpy.zeros(music.size)	
	for i in bandpass:
		loudest[i] = music_coef[i]
	
	
	loudest = numpy.fft.ifft(loudest) # freq -> time domain
	
	# t = numpy.arange(0, loudest.size)/frame_rate
	# pyplot.figure(1)
	# pyplot.plot(t, loudest)
	# pyplot.show()

	return music_freq[low], music_freq[high], loudest
	
def main():
	music, frame_rate, nframes, nchannels = read_wave(fname, debug=False)
	if nchannels > 1:
		music = music.sum(axis=1)
	bandwidth = 500
	loudest_band(music, frame_rate, bandwidth)
	
if __name__ == '__main__':
    main()
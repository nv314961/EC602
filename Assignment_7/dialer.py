import scipy.io.wavfile as wavfile
from numpy import pi, linspace, sin, int16, append, empty, array, concatenate
from numpy.fft import fftshift, fft
freq = [697.0, 770.0, 852.0, 941.0, 1209.0, 1336.0, 1477.0, 1633.0]

tones = {	
"1": (freq[0], freq[4]),
"2": (freq[0], freq[5]),
"3": (freq[0], freq[6]),
"4": (freq[1], freq[4]),
"5": (freq[1], freq[5]),
"6": (freq[1], freq[6]),
"7": (freq[2], freq[4]),
"8": (freq[2], freq[5]),
"9": (freq[2], freq[6]),
"*": (freq[3], freq[4]),
"0": (freq[3], freq[5]),
"#": (freq[3], freq[6])}

def dialer(file_name, frame_rate, phone, tone_time):
	
	A = 10000 # amplitude
	T = frame_rate * tone_time # T = N*tau
	x = linspace(0, tone_time, T)

	dialtone = array([])
	for i in range(len(phone)):
		#Retrive frequency values for current tone
		currentTone = tones.get(phone[i])
		signal = A*sin(2*pi*currentTone[0]*x) + A*sin(2*pi*currentTone[1]*x)
		dialtone = concatenate([dialtone,signal])
	
	dialtone.flatten()
	wavfile.write(file_name, frame_rate, dialtone.astype(int16))

def main():
	teststr = "8602017433"
	dialer("dial.wav", 48000, "8602017433", 0.5)
	
if __name__ == '__main__':
    main()
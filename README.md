# WavConverter
Converts wave files into an array of unsigned integers for any size DAC

How to use

If you have python installed you can download the .py file and run the script. 
If you do not have python installed you can download the .exe file and to run it.

Once you download and run the program a file explorer will be opened so you can choose the wav file you want to convert.
This program should work with all bit depths of wave files. I have only tested 16 but I think it should work for 8, 16, 24 and 32.
After you choose the file a command prompt will ask you for (all inputs need to be positive integer values:

The DAC Size- Type a positive integer value. This value is the number of bits in your dac.

The Target Sampling rate - This is the sampling rate you want the converted file to be. This value is probably 11025. If you want more points you can increase it. 

The size of the sound - Type a positive integer value that you want the length of the song to be divided by. Example if you want the first half of the song type 2. This will divide the length by 2 and stop the program halfway through. If you want the first tenth of a song then type 10. You can type any positive integer value >= 1.

If you find any bugs let me know.




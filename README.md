# WavConverter

### This program converts wave files from signed to unsigned integers to work with a custom DAC

### Purpose:

I wrote this program to convert any wav file into a C array that would work with a custom DAC that was built and programmed for a class project. The DAC driver only used unsigned integers and the typical wav format uses signed integer so the program shifts the data points up to be all positive integers. The DAC I built was only 6 bit so this program also needed to be able to convert the wav file to a lower bit depth. 

### How to use

If you have python installed you can download the .py file and run the script. 
If you do not have python installed you can download the .exe file and to run it.

Once you download and run the program a file explorer will be opened so you can choose the wav file you want to convert (The file explorer can take up to around 5-10 seconds to pop up so be patient).

This program should work with all bit depths of wave files. I have only tested 16 but I think it should work for 8, 16, 24 and 32.
After you choose the file a command prompt will ask you for (all inputs need to be positive integer values:

The DAC Size- Type a positive integer value. This value is the number of bits in your dac.

The Target Sampling rate - This is the sampling rate you want the converted file to be. This value is probably 11025. If you want more points you can increase it. 

The length of the sound - Type a positive integer value that you want the length of the song to be divided by. Example if you want the first half of the song type 2. This will divide the length by 2 and stop the program halfway through. If you want the first tenth of a song then type 10. If you want the whole song type 1. You can type any positive integer value >= 1.

The program will then run and once the command prompt closes there will be  a text file call "Converted..." in the same folder as the originial wav file. 

If you find any bugs let me know.




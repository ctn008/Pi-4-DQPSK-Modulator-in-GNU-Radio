# Pi/4 DQPSK Modulator in GNU Radio
A simple GR flowgraph with embedded Python module for pi/4 dqpsk signal mapper.

In learning GNU Radio, I am unable to find any example for pi/4 dqpsk modulation, therefore try to develop this modulator flowgrapth to understand GNU Radio and pi/4 DQPSK modulation. The program is inspired by https://gitlab.com/larryth/tetra-kit and referenced to the article https://www.ti.com/lit/an/spra341/spra341.pdf, which provides good explanation of pi/4 dqpsk and implementation. 

## 1. Construction of Pi/4 DQPSK Modulator 
The modulator shall take an input stream of dibits (0-3) and convert to the modulated waveform. It essentially consists of 03 sub-functions: 
a) Mapping the input dibits stream to IQ complex signal stream at the correct phases of pi/4 dqpsk (called Pi4-DQPSK Mapper). Each dibit is mapped to one IQ sample.
b) Interpolating the IQ stream to Nsps samples per symbol. To visuallize the process, it is constructed in GNU Radio block with fixed Nsps = 4. It can be easily included in the Python code instead. 
c) Pulseshaped Filter that takes the input of IQ complex signal stream and push out the pulseshaped complex IQ samples at the rate Nsps samples per symbol.

Pi/4 DQPSK Modulator Flowgraph
![image](https://github.com/ctn008/Pi-4-DQPSK-Modulator-in-GNURadio/assets/116415125/12069afa-22f0-466d-a737-f601bdd274ff)

Python code: can be seen by open the Python block and click edit.

## 2. Testing of Pi/4 DQPSK Modulator 
In order to test and verify the modulator functions correctly, a pi/4 DQPSK demodulator is required to demodulate the generated IQ complex signal stream and compare with the original dibits stream. 

For this verification purpose, a random source of dibits will be used to feed the modulator, and an modified pi/4 DQPSK demodulator from Tetra-Kit is used to receive the output stream of the modulator and demodulate. The resulted dibit stream shall be compare with the input dibit stream.

Because the demodulation process takes certain time and cause delays to the resulted dibit stream, to compare the two stream, a delay block is inserted to delay the input dibit stream so that the input and demodulated stream (as shown on the QT GUI Time Sink) can be compared for matching. 

![image](https://github.com/ctn008/Pi-4-DQPSK-Modulator-in-GNURadio/assets/116415125/27471bad-8597-46ff-89d0-4b4d229976f8)

The delay is set default at 48 to sync the input dibit stream with the output. It may change to different values on different computer on the Range Slider. 

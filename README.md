# Hagamos_lo_que_diga_el_corazon
Sciense hack day project for a low cost ECG using Arduino and python for real time heart beat visualization.
The matirial needed for this, is: An Arduino, some leds, 1k resitences and a computer with Unix. This project can be brokedown in two stages: First become your computer an ossiloscope, Second amplifie and clean the heart beat signal.  

# Convert your computer an ossiloscope

metrials: arduino, camputer, temperature sensor(LM35 ot tmp36), 1 LED, protoboard and 1kOhm resistance.

1) Go to ecg folder and open sinGrap in Arduino interface, connect your aduino and run. 
2) open printSignal.py and check the line "s = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)", the prot is different for mac and linux, and the baudrate should be the same in Serial.begin() in arduino script(sinGraph)
3) Execute printSignal.py.
4) Open animation_plot.py check for the port and baudrate. Them go to line 31 and set ax.set_ylim(10, 30) for the amplitude of a sin function.
5) restart arduino sonGraph and execute animation_plot.py. You should see a graph

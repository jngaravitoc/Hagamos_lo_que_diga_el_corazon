
import serial

s = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)


#s.write(b'text')
#print s.read()
#print s.readline()
while True:
    print s.readline().rstrip()
    

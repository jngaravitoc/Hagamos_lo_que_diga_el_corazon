import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
Lview=20
s = serial.Serial(port='/dev/tty.usbmodem1421', baudrate=9600)
st=0
while st < 100:
    print s.readline().rstrip()
    st+=1

def data_gen():
    t = data_gen.t
    cnt = 0
    
    while True:
        #print np.sin(2*np.pi*t) * np.exp(-t/10.) 
        
        t += 0.05
        yield t, s.readline().rstrip()
    """
    while cnt < 1000:
        cnt+=1
        t += 0.05
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
    """   
data_gen.t = 0

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(10, 30)
ax.set_xlim(0, Lview)
ax.grid()
xdata, ydata = [], []
def run(data):
    # update the data
    t,y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin+Lview, xmax+Lview)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
    repeat=False)
plt.show()

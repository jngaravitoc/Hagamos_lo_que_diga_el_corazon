import numpy as np
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import time

stream_ids = tls.get_credentials_file()['stream_ids']

stream_id = stream_ids[1]

# Make instance of stream id object 
stream = Stream(
    token=stream_id,  # (!) link stream id to 'token' key
    maxpoints=60      # (!) keep a max of 80 pts on screen
)

trace2 = Scatter(
    x=[],
    y=[],
    mode = "markers",
     marker=Marker(
     color='rgb(255, 128, 0)'
     ),

    stream=stream  # (!) embed stream id, 1 per trace


)

data = Data([trace2])

axis_style = dict(
    showgrid=False,    # remove grid
    showline=False,    # remove axes lines
    zeroline=False     # remove x=0 and y=0 lines
)

layout = Layout(
    title='Heart Attack',  # set plot's title
    
    width=1200,
    height=800,
    xaxis=XAxis(
        axis_style,     # add style options
        range=[-1.5,3.5]    # set x-axis range
    ),
    yaxis=YAxis(
        axis_style,     # add style options
        range=[-1.5,1.5]  # set y-axis range
    ),
    showlegend=False,   # remove legend
    paper_bgcolor='rgb(6, 31, 90)',
    plot_bgcolor='rgb(6, 31, 90)',
    
)
# Add title to layout object

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='s7_first-stream2')

# (@) Make instance of the Stream link object, 
#     with same stream id as Stream id object
s = py.Stream(stream_id)

# (@) Open the stream
s.open()

i=0
while i<10000000:
    i += 1   # add to counter
    data = np.loadtxt("data.dat")
    X = data[i:,0]
    Y = data[i:,1]
    x = X[i]
    y = Y[i]
    # Current time on x-axis, random numbers on y-axis
   
    # (-) Both x and y are numbers (i.e. not lists nor arrays)
    
    # (@) write to Plotly stream!
    s.write(dict(x=x, y=y))    
    # (!) Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot (more in 7.2).
            
    time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting
    
# (@) Close the stream when done plotting
s.close() 


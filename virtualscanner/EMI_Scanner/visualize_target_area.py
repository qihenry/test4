import numpy as np
from plotly.graph_objs import *
import plotly.graph_objs as go
import os

# Function to create Plotly display to show target area in room
# least_avg_coords = list of tuples, containing ordered list of potential target locations
def visualize_target_area (full_list, least_avg_coords):
    # Initialize empty variables
    tempx = []
    tempy = []
    tempz = []
    d = []
    for i in range(10):
        tempx.append([])
        tempy.append([])
        tempz.append([])
        d.append([])
    alldata = []

    # Get data in terms of x, y, z, data for plotly processing
    for choice in range(len(least_avg_coords)):
        for i in list(range(least_avg_coords[choice][0],least_avg_coords[choice][3]+1)):
            for j in list(range(least_avg_coords[choice][1],least_avg_coords[choice][4]+1)):
                for k in range(len(full_list[1][1])):
                    tempx.append(i*80)
                    tempy.append(j*80)
                    tempz.append(k*80)
                    alldata.append(1)

                    # Populate x, y, z values, and corresponding magnitudes
                    tempx[choice].insert(0,i*80)
                    tempy[choice].insert(0,j*80)
                    tempz[choice].insert(0,k*80)

    # Convert to np arrays for plotly usage
    x = []
    y = []
    z = []
    for i in range(10): x.append(np.array(tempx[i]))
    for i in range(10): y.append(np.array(tempy[i]))
    for i in range(10): z.append(np.array(tempz[i]))

    # Plotly visual settings
    traces = []
    color_selection = list(reversed(['#2f0559','#4a167d','#5b2491','#5b2491','#8149ba','#9963cf','#aa7cd9','#ba94e0','#d0b2ed','#dec9f2']))
    for choice in range(len(least_avg_coords)):
        traces.append(
            go.Scatter3d(
                x = x[choice], y = y[choice], z = z[choice], mode = 'lines+markers',
                marker = dict(
                    size = 17,
                    opacity=1
                ),
                line=dict(
                    width=20
                ),
                name = "Choice " + str(choice+1) + ":<br>" +
                    str((least_avg_coords[choice][0]*80,least_avg_coords[choice][1]*80,least_avg_coords[choice][2]*80)) + " --> " +
                    str((least_avg_coords[choice][3]*80,least_avg_coords[choice][4]*80,least_avg_coords[choice][5]*80)) + "<br>"
            )
        )

    # Plotly axis and graph labels
    layout = go.Layout(showlegend=True,
        scene=Scene(
            xaxis=XAxis(title='Room Width (x-axis), mm'),
            yaxis=YAxis(title='Room Length (y-axis), mm'),
            zaxis=ZAxis(title='Room Height (z-axis), mm')),
        title = 'Target Area'
    )

    # Display figure
    fig = go.Figure(data = traces, layout = layout)
    fig.update_scenes(xaxis_range=[0,len(full_list)*80])
    fig.update_scenes(yaxis_range=[0,len(full_list[0])*80])
    fig.update_scenes(zaxis_range=[0,len(full_list[0][0])*80])
    fig.update_scenes(aspectratio=dict(x=len(full_list)/5,y=len(full_list[0])/5,z=len(full_list[0][0])/5))
    
    # Save to html file
    return fig
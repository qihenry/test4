import math
import numpy as np
from plotly.graph_objs import *
import plotly.graph_objs as go
import os

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def visualize_EMI (full_list):
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
    max_val = 0
    min_val = 1000

    # Iterate through data in given measurements
    for i in range(len(full_list)):
        for j in range(len(full_list[1])):
            for k in range(len(full_list[1][1])):
                # Find largest and smallest values in the dataset
                if(full_list[i][j][k].get_magnitude() > max_val): max_val = full_list[i][j][k].get_magnitude()
                if(full_list[i][j][k].get_magnitude() < min_val): min_val = full_list[i][j][k].get_magnitude()

                # Store all data to map to colorscale
                alldata.append(full_list[i][j][k].get_magnitude())

    # Separate data in groups of 10
    intervals = (max_val-min_val)/10
    for i in range(len(full_list)):
        for j in range(len(full_list[1])):
            for k in range(len(full_list[1][1])):                
                # Map to range of 10
                leftSpan = max_val - min_val  
                rightSpan = 9
                valueScaled = float(full_list[i][j][k].get_magnitude() - min_val) / float(leftSpan)
                d[math.floor(valueScaled * rightSpan)].append(full_list[i][j][k].get_magnitude())

                # Populate x, y, z values, and corresponding magnitudes
                tempx[math.floor(valueScaled * rightSpan)].insert(0,i*80)
                tempy[math.floor(valueScaled * rightSpan)].insert(0,j*80)
                tempz[math.floor(valueScaled * rightSpan)].insert(0,k*80)

    # Convert to np arrays for plotly usage
    x = []
    y = []
    z = []
    for i in range(10): x.append(np.array(tempx[i]))
    for i in range(10): y.append(np.array(tempy[i]))
    for i in range(10): z.append(np.array(tempz[i]))
    colorscale_data = np.array(alldata)

    # Create slider to view different magnitudes of data
    steps = []

    for i in range(10):
        step = dict(
            method = 'update',
            label = str(round(intervals*i,5)),
            args=[{'visible': [False] * 11}],
        )
        for j in range(11):
            if(j >= i): step["args"][0]["visible"][j] = True
        steps.append(step)
    sliders = [dict(
        active=10,
        pad={"t": 50},
        steps=steps
    )]

    # Plotly visual settings
    traces = []
    color_selection = list(reversed(['#2f0559','#4a167d','#5b2491','#5b2491','#8149ba','#9963cf','#aa7cd9','#ba94e0','#d0b2ed','#dec9f2']))
    for i in range(10):
        traces.append(
            go.Scatter3d(
                x = x[i], y = y[i], z = z[i], mode = 'markers', 
                name = "Mag. Level %d"%(i),
                marker = dict(
                    size = 12,
                    opacity=0.5,
                    color = color_selection[i]
                ),
                text = ['<br><br>Magnitude: %f'%(j) for j in d[i]],
                showlegend = False
            )
        )

    # Plotly axis and graph labels
    layout = go.Layout(showlegend=True,
        scene=Scene(
            xaxis=XAxis(title='Room Width (x-axis), mm'),
            yaxis=YAxis(title='Room Length (y-axis), mm'),
            zaxis=ZAxis(title='Room Height (z-axis), mm')),
        title = 'EMI in Room'
    )

    # Create figure
    fig = go.Figure(data = traces, layout = layout)

    # Create static colorbar to show EMI level scaling
    colorbar_trace  = go.Scatter3d(x=[None], y=[None], z=[None], mode='markers',
        marker=dict(
            colorscale='Purples', 
            showscale=True,
            cmin=-5,
            cmax=5,
            colorbar=dict(thickness=20, tickvals=[-5, 5], ticktext=[str(round(min_val,5)), str(round(max_val,5))], outlinewidth=0)),
        hoverinfo='none',
    )
    fig['layout']['showlegend'] = False
    fig.add_trace(colorbar_trace)

    # Display figure
    fig.update_scenes(xaxis_range=[0,len(full_list)*80])
    fig.update_scenes(yaxis_range=[0,len(full_list[0])*80])
    fig.update_scenes(zaxis_range=[0,len(full_list[0][0])*80])
    fig.update_scenes(aspectratio=dict(x=len(full_list)/5,y=len(full_list[0])/5,z=len(full_list[0][0])/5))
    fig.update_layout(sliders=sliders)

    # Save to html file
    return fig
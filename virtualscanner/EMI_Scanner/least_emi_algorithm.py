'''
Designer notes:

The function performs a search algorithm on the "condensed_data array" (target 
room) to find the coordinates of the rectangular area (with length "w" and 
"width h") that has the lowest average EMI (electromagnetic interference) value
and meets the EMI requirement specified by device specification(EMI_max).

To do this, the function first performs a data preprocessing step on the 
"condensed_data array" to generate two new arrays: "sum_preprocess_list" and 
"detection_preprocess_list". These arrays are used to quickly calculate the EMI
sum and number of points that do not meet the EMI requirement for any 
rectangular area of the condensed_data array.

The function then iterates through the "condensed_data array" to check each 
rectangular area with length "l", width "w" and height "h". For each 
rectangular area, the function uses the "sum_preprocess_list" to quickly 
calculate the average EMI in curret rectangular area and use 
"detection_preprocess_list" arrays to check if current rectangular area 
meets the EMI requirement. In other words, if the area meets the EMI 
requirement, the function calculates the average EMI value for that area and 
checks if it is the current lowest average EMI value. If it is, the function 
updates the current lowest average EMI values and records the coordinates of 
the current rectangular area.

Finally, the function returns a list containing three lowest average EMI value 
and the coordinates of these areas.


Input clarification:
condensed_data: a 2D array with EMI measurement of the target room.
l: an integer that shows the length of the wanted rectangular area.
w: an integer that shows the width of the wanted rectangular area.
h: an integer that shows the height of the wanted rectangular area.
EMI_max: maximum EMI allowed for safely operate the device.

Output clarification:
The function will return a tuple containing least_avg_val and least_avg_coord
least_avg_val_list: a list of the three least average EMI in the target room
least_avg_coord : a list of three ranked least average EMI location 
Each components in the list is a tuple contains 6 integer. 
- The first two integers shows the coordinates of the top left corner of the 
  wanted rectangular area.
- The third and fourth integer shows the coordinates of the bottom right corner
  of the wanted rectangular area.
'''
import math
import numpy as np

from virtualscanner.EMI_Scanner.emi_measurement_class import emi_measurement

# this algorith uses 3D prefix sum
def search_algorithm (condensed_data, l, w, h, EMI_max):
    least_avg_val_list = [math.inf, math.inf, math.inf]
    least_avg_coord = [(-1,-1,-1,-1,-1,-1),
                            (-1,-1,-1,-1,-1,-1),
                            (-1,-1,-1,-1,-1,-1)]
    total_num_points = l * w * h

    # Preprocessing the data
    # list to calculate the sum
    sum_preprocess_list = []
    # list to detect EMI requirement
    detection_preprocess_list =[]

    # define the two list
    for i in range (len(condensed_data)):
        temp_one_layer_array_1 = []
        temp_one_layer_array_2 = []
        for j in range (len(condensed_data[i])):
            temp_list_1 = []
            temp_list_2 = []
            for k in range (len(condensed_data[i][j])):
                temp_list_1.append(None)
                temp_list_2.append(None)
            temp_one_layer_array_1.append(temp_list_1)
            temp_one_layer_array_2.append(temp_list_2)
        sum_preprocess_list.append(temp_one_layer_array_1)
        detection_preprocess_list.append(temp_one_layer_array_2)

    for i in range (len(condensed_data)):
        for j in range (len(condensed_data[i])):
            for k in range (len(condensed_data[i][j])):
                s1 = sum_preprocess_list[i-1][j-1][k-1]
                s2 = sum_preprocess_list[i-1][j-1][k]
                s3 = sum_preprocess_list[i-1][j][k-1]
                s4 = sum_preprocess_list[i-1][j][k]
                s5 = sum_preprocess_list[i][j-1][k-1]
                s6 = sum_preprocess_list[i][j-1][k]
                s7 = sum_preprocess_list[i][j][k-1]
                s8 = condensed_data[i][j][k]
                
                d1 = detection_preprocess_list[i-1][j-1][k-1]
                d2 = detection_preprocess_list[i-1][j-1][k]
                d3 = detection_preprocess_list[i-1][j][k-1]
                d4 = detection_preprocess_list[i-1][j][k]
                d5 = detection_preprocess_list[i][j-1][k-1]
                d6 = detection_preprocess_list[i][j-1][k]
                d7 = detection_preprocess_list[i][j][k-1]
                d8 = 0
                if condensed_data[i][j][k].get_magnitude() > EMI_max: 
                    d8 = 1
                
                if i == 0: 
                    s1 = s2 = s3 = s4 = emi_measurement(0,0,0)
                    d1 = d2 = d3 = d4 = 0
                if j == 0: 
                    s1 = s2 = s5 = s6 = emi_measurement(0,0,0)
                    d1 = d2 = d5 = d6 = 0
                if k == 0: 
                    s1 = s3 = s5 = s7 = emi_measurement(0,0,0)
                    d1 = d3 = d5 = d7 = 0
                    
                sum_preprocess_list[i][j][k] = (s8 + s1 - s2 - s3
                                                + s4 - s5 + s6 + s7)

                # determine if the current point meets the EMI requirement.
               
                detection_preprocess_list[i][j][k] = (d8 + d1 - d2 - d3 + d4 
                                                      - d5 + d6 + d7)
                    
    # Find least_average_EMI_position
    iteration = 0
    while (iteration < 2):
        for i in range (len(condensed_data)):               
            for j in range (len(condensed_data[0])):
                for k in range (len(condensed_data[0][0])):
                    if not (i >= l - 1 and j >= w - 1 and k >= h - 1): continue 
                    s1 = sum_preprocess_list[i-l][j-w][k-h]
                    s2 = sum_preprocess_list[i-l][j-w][k]
                    s3 = sum_preprocess_list[i-l][j][k-h]
                    s4 = sum_preprocess_list[i-l][j][k]
                    s5 = sum_preprocess_list[i][j-w][k-h]
                    s6 = sum_preprocess_list[i][j-w][k]
                    s7 = sum_preprocess_list[i][j][k-h]
                    s8 = sum_preprocess_list[i][j][k]
                                             
                    d1 = detection_preprocess_list[i-l][j-w][k-h]
                    d2 = detection_preprocess_list[i-l][j-w][k]
                    d3 = detection_preprocess_list[i-l][j][k-h]
                    d4 = detection_preprocess_list[i-l][j][k]
                    d5 = detection_preprocess_list[i][j-w][k-h]
                    d6 = detection_preprocess_list[i][j-w][k]
                    d7 = detection_preprocess_list[i][j][k-h]
                    d8 = detection_preprocess_list[i][j][k]
                    
                    if i < l: 
                        s1 = s2 = s3 = s4 = emi_measurement(0,0,0)
                        d1 = d2 = d3 = d4 = 0
                    if j < w: 
                        s1 = s2 = s5 = s6 = emi_measurement(0,0,0)
                        d1 = d2 = d5 = d6 = 0
                    if k < h: 
                        s1 = s3 = s5 = s7 = emi_measurement(0,0,0)
                        d1 = d3 = d5 = d7 = 0

                    current_detection = d8 - d1 + d2 + d3 - d4 + d5 - d6 - d7
                    
                    # Calculate the average EMI if nessary
                    if not current_detection:
                        # Calculate current average
                        c_a = (s8 - s1 + s2 + s3 - s4 + s5 
                                           - s6 - s7) / total_num_points
                        for m in range (len(least_avg_val_list)):
                            if (c_a.get_magnitude() < least_avg_val_list[m]):
                                least_avg_val_list[m] = c_a.get_magnitude()
                                least_avg_coord[m] = (i - l + 1, j - w + 1,
                                                   k - h + 1, i, j, k)
                                break
        # flip length and width
        temp = w
        w = l
        l = temp
        iteration += 1
        
    return (least_avg_val_list, least_avg_coord) 


import math

from virtualscanner.EMI_Scanner.least_emi_algorithm import search_algorithm
from virtualscanner.EMI_Scanner.emi_measurement_class import emi_measurement
from virtualscanner.EMI_Scanner.visualize_EMI import visualize_EMI
from virtualscanner.EMI_Scanner.visualize_target_area import visualize_target_area
from virtualscanner.EMI_Scanner.convert_to_emi_class import convert_to_emi_class




###### MOCK DATA ######

# Would we have to process our data beforehand?
full_list_INTS = [[[1, 0, 0, 1, 2], [1, 0, 1, 2, 2], [3, 2, 3, 5, 6], [4, 5, 3, 2, 1], [2, 4, 6, 7, 8], [9, 8, 5, 6, 6], [4, 3, 2, 3, 4]],
[[0, 1, 0, 1, 0], [2, 1, 1, 3, 3], [2, 4, 3, 4, 5], [3, 4, 2, 1, 1], [0, 3, 5, 6, 8], [7, 7, 6, 7, 8], [6, 4, 3, 3, 3]],
[[1, 1, 0, 0, 1], [1, 2, 2, 1, 2], [3, 4, 4, 5, 5], [4, 6, 5, 3, 2], [1, 2, 4, 5, 9], [8, 6, 4, 5, 7], [5, 3, 2, 2, 1]],
[[2, 1, 2, 2, 3], [2, 3, 3, 3, 4], [4, 3, 4, 4, 3], [5, 5, 4, 4, 3], [2, 1, 3, 4, 6], [7, 6, 5, 5, 6], [5, 4, 3, 2, 2]],
[[1, 2, 3, 2, 3], [3, 4, 3, 4, 5], [5, 4, 4, 5, 4], [4, 4, 3, 3, 4], [3, 2, 2, 3, 3], [5, 4, 5, 4, 4], [3, 4, 2, 2, 1]],
[[2, 3, 3, 2, 4], [5, 5, 4, 4, 3], [4, 5, 5, 3, 5], [5, 6, 5, 4, 3], [4, 3, 2, 3, 2], [4, 5, 3, 3, 3], [2, 2, 3, 3, 2]],
[[3, 2, 3, 3, 3], [4, 4, 3, 4, 3], [3, 4, 4, 4, 3], [4, 5, 4, 4, 3], [3, 2, 3, 2, 3], [3, 4, 5, 4, 4], [3, 4, 3, 2, 2]],
[[4, 3, 3, 3, 2], [3, 2, 3, 3, 2], [3, 4, 3, 3, 2], [2, 3, 4, 5, 4], [4, 3, 3, 2, 3], [2, 2, 4, 3, 3], [2, 2, 3, 2, 3]],
[[5, 4, 4, 3, 3], [2, 2, 2, 3, 2], [3, 3, 3, 4, 4], [3, 4, 3, 2, 2], [3, 3, 4, 3, 3], [2, 3, 4, 3, 3], [3, 2, 3, 2, 1]]]


###### CONVERT TO CLASS INSTANCES INSTEAD OF INTEGERS ######

full_list = []
l_num_points = 0
w_num_points = 0
h_num_points = 0
for i in range(len(full_list_INTS)):
    temp_array1 = []
    for j in range(len(full_list_INTS[0])):
        temp_array2 = []
        for k in range(len(full_list_INTS[0][0])):
            val = full_list_INTS[i][j][k]
            temp_array2.append(emi_measurement(val,val,val))
        temp_array1.append(temp_array2)
    full_list.append(temp_array1)








def run_emi(data=full_list):
    ###### RUN SEARCH ALGORITHM ######
    # set max value that can be present in any given solution target area
    EMI_max = math.inf

    # set target area dimensions
    tax = 1
    tay = 1
    taz = 1

    # test room w/ MRI lengthwise along x-axis
    least_avg_val = math.inf
    least_avg_coord = (-1,-1,-1,-1,-1,-1) # x1, y1, z1, x2, y2, z2

    # find the least average EMI area
    (least_avg_val, least_avg_coord) = search_algorithm(data, tax, tay, taz, EMI_max)


    ###### CREATE VISUALIZATIONS ######

    fig1 = visualize_EMI (data)
    fig2 = visualize_target_area (data, least_avg_coord)
    return [fig1, fig2]
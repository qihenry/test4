from virtualscanner.EMI_Scanner.emi_measurement_class import emi_measurement

# function to take in nested list of measured data and convert
# values from ints to class instances
def convert_to_emi_class(full_list_ints):
    full_list = []
    l_num_points = 0
    w_num_points = 0
    h_num_points = 0
    for i in range(len(full_list_ints)):
        temp_array1 = []
        for j in range(len(full_list_ints[0])):
            temp_array2 = []
            for k in range(len(full_list_ints[0][0])):
                val = full_list_ints[i][j][k]
                temp_array2.append(emi_measurement(val,val,val))
            temp_array1.append(temp_array2)
        full_list.append(temp_array1)

    return full_list
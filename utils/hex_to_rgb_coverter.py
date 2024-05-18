'''
This function coverts a string representing hex color code
to a list containing rgb values
'''

def convert(hex):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
    alphabet_values = [10, 11, 12, 13, 14, 15]
    base_10 = [0, 1, 2, 3, 4 , 5, 6, 7, 8, 9]
    rgb = []

    r = hex[0:2]
    g = hex[2:4]
    b = hex[4:6]


    def convert_color(color):
        for i, value in enumerate(color):
            if i == 0:
                for j, corresponding_value in enumerate(alphabet):
                    if corresponding_value == value:
                        value1 = alphabet_values[j] * 16
                for base_10_value in base_10:
                    if base_10_value == value or str(base_10_value) == str(value):
                        value1 = int(value) * 16

            elif i == 1:
                for j, corresponding_value in enumerate(alphabet):
                    if corresponding_value == value:
                        value2 = alphabet_values[j]
                for base_10_value in base_10:
                    if base_10_value == value or str(base_10_value) == str(value):
                        value2 = int(value)

        result = value1 + value2
        return result
    

    rgb.append(convert_color(r))
    rgb.append(convert_color(g))
    rgb.append(convert_color(b))
    # Add a fourth element containing transparency data
    rgb.append(1)

    return rgb
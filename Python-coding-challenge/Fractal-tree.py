import matplotlib.pyplot as plt
import numpy as np
Length_of_line = 50
offset_angle = 45 # float(input("input an offset angle in degrees:\n"))
offset_angle_in_radians = offset_angle * np.pi / 180
angle = np.pi / 2
x = 140
y = 159
number_of_levels = 2
def delta_length(current_length):
    dl = current_length * (2/3)
    return dl
def delta_angle(current_angle):
    da = current_angle + offset_angle_in_radians
    return da
i = 0
max_levels = 2
x_values = np.zeros(max_levels+1)
y_values = np.zeros(max_levels+1)
x_values[0] = x
y_values[0] = y
while i < max_levels:
    Length_of_line = delta_length(Length_of_line)
    dx = x_values[i] + Length_of_line * np.cos(angle)
    dy = y_values[i] + Length_of_line * np.sin(angle)
    plt.plot([x_values[i],dx],[y_values[i],dy])
    angle = angle + offset_angle_in_radians
    i += 1
    x_values[i] = dx
    y_values[i] = dy
plt.show()
print(x_values,y_values)

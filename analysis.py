# Open a .txt file and get the step (column 0), time(column 1), fx (column 18), fy (column 19), fz (column 20). Remove the first 3 lines

import numpy as np
import matplotlib.pyplot as plt

# Open the file
name = 'wing_edit_1'
f = open(f'{name}.txt', 'r')
lines = f.readlines()
f.close()

# Remove the first 3 lines
lines = lines[3:]

# Create empty lists
step = []
time = []
fx = []
fy = []
fz = []

# Loop through the lines
for line in lines:
    p = line.split()
    step.append(float(p[0]))
    time.append(float(p[1]))
    fx.append(float(p[18]))
    fy.append(float(p[19]))
    fz.append(float(p[20]))

# Convert the lists to numpy arrays
step = np.array(step)
time = np.array(time)
fx = np.array(fx)
fy = np.array(fy)
fz = np.array(fz)

#Get the average of the last 20% of the data
n = int(0.2 * len(fx))
fx_avg = np.mean(fx[-n:])
fy_avg = np.mean(fy[-n:])
fz_avg = np.mean(fz[-n:])

print(f'Average drag: {fx_avg}')
print(f'Average lift: {fy_avg}')

# Plot the data
plt.plot(time, fx, label='Drag')
plt.plot(time, fy, label='Lift')
plt.plot(time, fz, label='Lateral force')
plt.xlabel('Time [s]')
plt.ylabel('Force [N]')
plt.legend()

#Add a title
plt.title(name)

plt.show()

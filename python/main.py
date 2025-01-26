import matplotlib.pyplot as plt
import matplotlib.animation as animation
from serial import Serial
import numpy as np

serial = Serial(
    port="/dev/ttyUSB0",
    baudrate=9600,
)

# try:
#     while True:
#         if serial.in_waiting > 0:
#             data = serial.readline().decode("utf-8").strip()
#             print(data)
# finally:
#     serial.close()


class SerialWatcher:
    count = 0

    def __init__(self, serial: Serial):
        self.serial = serial
        while self.serial.in_waiting > 0:
            self.serial.readline()

        fix, ax = plt.subplots()
        x_data, y_data = [], []
        (line,) = plt.plot(x_data, y_data)

        self.x_data = x_data
        self.y_data = y_data
        self.line = line
        self.ax = ax

        ani = animation.FuncAnimation(
            fix, self.update, frames=np.arange(10000), interval=50
        )

        plt.show()

    def update(self, frame):
        if self.serial.in_waiting > 0:  # Check if data is available
            data = self.serial.readline().decode("utf-8").strip()  # Read a line of data
            print(self.serial.in_waiting)

            new_x = self.count
            new_y = int(data)

            self.last_value = new_y

            # Append new data to the lists
            self.x_data.append(new_x)
            self.y_data.append(new_y)

            self.x_data = self.x_data[-100:]
            self.y_data = self.y_data[-100:]

            # Update the line data
            self.line.set_data(self.x_data, self.y_data)

            # Adjust the x-axis and y-axis limits to fit the new data
            self.ax.relim()  # Recalculate limits
            self.ax.autoscale_view()  # Rescale the view

            self.count += 1

        return (self.line,)


try:
    SerialWatcher(serial)
finally:
    serial.close()

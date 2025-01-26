import matplotlib.pyplot as plt
import matplotlib.animation as animation
from serial import Serial
import numpy as np

# ser = Serial(
#     port="/dev/ttyUSB0",
#     baudrate=9600,
#     timeout=1,
# )

# try:
#     while True:
#         if ser.in_waiting > 0:  # Check if data is available
#             data = ser.readline()  # Read a line of data
#             print(data.decode("utf-8").strip())  # Decode and print the data
# except KeyboardInterrupt:
#     print("Exiting...")
# finally:
#     ser.close()  # Close the serial port


class SerialWatcher:
    def __init__(self):
        fix, ax = plt.subplots()
        x_data, y_data = [], []
        (line,) = plt.plot(x_data, y_data)

        self.x_data = x_data
        self.y_data = y_data
        self.line = line
        self.ax = ax

        ani = animation.FuncAnimation(
            fix, self.update, frames=np.arange(1000), interval=50, blit=True
        )

        plt.show()

    def update(self, frame):
        new_x = frame * 0.1
        new_y = np.sin(new_x)

        # Append new data to the lists
        self.x_data.append(new_x)
        self.y_data.append(new_y)

        # Update the line data
        self.line.set_data(self.x_data, self.y_data)

        # Adjust the x-axis and y-axis limits to fit the new data
        self.ax.relim()  # Recalculate limits
        self.ax.autoscale_view()  # Rescale the view

        return (self.line,)


# def animate(i):
#     graph_data = open("example.txt", "r").read()
#     lines = graph_data.split("\n")
#     xs = []
#     ys = []
#     for line in lines:
#         if len(line) > 1:
#             x, y = line.split(",")
#             xs.append(float(x))
#             ys.append(float(y))
#     ax1.clear()
#     ax1.plot(xs, ys)
#

serial = SerialWatcher()

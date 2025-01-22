import serial.tools.list_ports

import matplotlib.pyplot as plt

# ser = serial.Serial(
#     port="/dev/ttyUSB0",
#     baudrate=9600,
#     timeout=1,
# )
#
# try:
#     while True:
#         if ser.in_waiting > 0:  # Check if data is available
#             data = ser.readline().decode("utf-8").strip()  # Read and decode data
#             print(f"Received: {data}")
#
#             ser.write(b"ACK\n")
#
# except KeyboardInterrupt:
#     print("Exiting...")
# finally:
#     ser.close()  # Close the serial port
#

# Read the CSV file into a DataFrame
df = {"Time": [0, 1, 2, 3, 4, 5], "Value": [10, 15, 13, 17, 20, 18]}

# Plot the data
plt.figure(figsize=(8, 5))  # Set the figure size
plt.plot(
    df["Time"],
    df["Value"],
    marker="o",
    linestyle="-",
    color="b",
    label="Value over Time",
)

# Add labels and title
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Time vs Value")
plt.legend()  # Show legend
plt.grid(True)  # Add grid

# Show the plot
plt.show()

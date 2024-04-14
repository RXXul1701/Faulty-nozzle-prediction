import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def generate_data(num_samples, min_voltage, max_voltage, noise_level):
    # Generate a clean signal
    signal = np.random.uniform(min_voltage, max_voltage, num_samples)

    # Generate noise
    noise = np.random.normal(0, noise_level, num_samples)

    # Return the sum of the signal and noise
    return signal + noise

def analyze_data(data):
    # Calculate mean, standard deviation and range
    mean = np.mean(data)
    std_dev = np.std(data)
    range_data = np.ptp(data)

    # Logic to find faulty nozzles
    threshold = mean - 2*std_dev
    faulty_nozzles = np.where(data < (threshold))[0]
    print(f"Threshold = ",threshold)

    return mean, std_dev, range_data, faulty_nozzles, threshold

def update_plot(canvas, subplot, data, threshold):
    # Clear the previous plot
    subplot.clear()

    # Plot the new data
    subplot.plot(data)
    subplot.set_xlabel('Sample_Index')
    subplot.set_ylabel('Voltage(in V)')
    subplot.axhline(y=threshold, color='r', linestyle='--', label='Threshold')

    # Redraw the canvas
    canvas.draw()
    

def update_labels(mean_label, std_dev_label, range_label, mean, std_dev, range_data):
    # Update the labels with the new data analysis results
    mean_label.config(text=f"Mean: {mean}")
    std_dev_label.config(text=f"Standard Deviation: {std_dev}")
    range_label.config(text=f"Range: {range_data}")

def simulate_data():
    # Generate new data
    data = generate_data(num_samples, min_voltage, max_voltage, noise_level)

    # Analyze the data
    mean, std_dev, range_data, faulty_nozzles, threshold = analyze_data(data)
    print("Faulty nozzles are = ",faulty_nozzles)
    print("No of faulty samples = ", len(faulty_nozzles))

    

    # Update the plot and labels
    update_plot(canvas, subplot, data, threshold)
    update_labels(mean_label, std_dev_label, range_label, mean, std_dev, range_data)

# Parameters for data generation
num_samples = 150
min_voltage = 1.5
max_voltage = 10
noise_level = 0.8

# Create the main window
root = tk.Tk()

# Create a Figure and a subplot
fig = plt.Figure(figsize=(5, 4), dpi=100)
subplot = fig.add_subplot(111)

# Add the Figure to the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create labels for displaying the data analysis results
mean_label = tk.Label(master=root, text="")
mean_label.pack()
std_dev_label = tk.Label(master=root, text="")
std_dev_label.pack()
range_label = tk.Label(master=root, text="")
range_label.pack()

# Create a button for simulating new sensor data
simulate_button = tk.Button(master=root, text="Simulate Data", command=simulate_data)
simulate_button.pack()

# Start the Tkinter event loop
tk.mainloop()
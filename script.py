import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def generate_data(num_samples, min_voltage, max_voltage, noise_level):
    
    signal = np.random.uniform(min_voltage, max_voltage, num_samples)

    
    noise = np.random.normal(0, noise_level, num_samples)

    
    return signal + noise

def analyze_data(data):
    
    mean = np.mean(data)
    std_dev = np.std(data)
    range_data = np.ptp(data)

    
    threshold = mean - 2*std_dev
    faulty_nozzles = np.where(data < (threshold))[0]
    print(f"Threshold = ",threshold)

    return mean, std_dev, range_data, faulty_nozzles, threshold

def update_plot(canvas, subplot, data, threshold):
    
    subplot.clear()


    subplot.plot(data)
    subplot.set_xlabel('Sample_Index')
    subplot.set_ylabel('Voltage(in V)')
    subplot.axhline(y=threshold, color='r', linestyle='--', label='Threshold')

    
    canvas.draw()
    

def update_labels(mean_label, std_dev_label, range_label, mean, std_dev, range_data):
    
    mean_label.config(text=f"Mean: {mean}")
    std_dev_label.config(text=f"Standard Deviation: {std_dev}")
    range_label.config(text=f"Range: {range_data}")

def simulate_data():
    
    data = generate_data(num_samples, min_voltage, max_voltage, noise_level)

    
    mean, std_dev, range_data, faulty_nozzles, threshold = analyze_data(data)
    print("Faulty nozzles are = ",faulty_nozzles)
    print("No of faulty samples = ", len(faulty_nozzles))

    

    
    update_plot(canvas, subplot, data, threshold)
    update_labels(mean_label, std_dev_label, range_label, mean, std_dev, range_data)


num_samples = 150
min_voltage = 1.5
max_voltage = 10
noise_level = 0.8


root = tk.Tk()


fig = plt.Figure(figsize=(5, 4), dpi=100)
subplot = fig.add_subplot(111)


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


mean_label = tk.Label(master=root, text="")
mean_label.pack()
std_dev_label = tk.Label(master=root, text="")
std_dev_label.pack()
range_label = tk.Label(master=root, text="")
range_label.pack()


simulate_button = tk.Button(master=root, text="Simulate Data", command=simulate_data)
simulate_button.pack()


tk.mainloop()

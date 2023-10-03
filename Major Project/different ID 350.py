import matplotlib.pyplot as plt

# Provided data
x_data = [0, 100, 200, 300, 400, 500, 600, 700, 800]

y_data_21 = [0, 0.086839, 0.125914, 0.130577, 0.183309, 0.134998, 0.129542, 0.112946, 0.0984636]
y_data_28 = [0, 0.2975, 0.2073, 0.27, 0.2974, 0.3923, 0.3949, 0.3961, 0.341]
# Custom tick values
x_ticks = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
y_ticks = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

# Create the plot
plt.figure(figsize=(8, 6))  # Optional: set the figure size

plt.plot(x_data, y_data_21, linestyle='-.', label='ID = 21 mm', color='k')
plt.plot(x_data, y_data_28, linestyle=':', label='ID = 28 mm', color='k')
# Customize x and y-axis ticks
plt.xticks(x_ticks)
plt.yticks(y_ticks)

plt.xlim(0, max(x_ticks))
plt.ylim(0, max(y_ticks))

plt.xlabel('Power, Q (kW)')
plt.ylabel('Mass Flow Rate, W (kg/s)')
plt.title('Mass Flow Rate vs. Power')
plt.legend(loc='upper right')

plt.text(800, 0.58, 'HHHC', fontsize=12, ha='right', va='bottom')
plt.text(800, 0.55, 'P = 25MPa', fontsize=12, ha='right', va='bottom')
plt.text(800, 0.52, 'T = 350°C', fontsize=12, ha='right', va='bottom')
plt.text(800, 0.49, 'H = 4.1 m', fontsize=12, ha='right', va='bottom')

# Show the plot
plt.show()

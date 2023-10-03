import matplotlib.pyplot as plt

# Provided data
x_data = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
y_data_350 = [0, 0.051387, 0.083307, 0.09971, 0.09953, 0.09373]
y_data_370 = [0, 0.0622, 0.076, 0.08686, 0.091, 0.09624, 0.09890, 0.09975, 0.10206, 0.10083, 0.09112, 0.086]
y_data_390 = [0, 0.068, 0.084, 0.096, 0.102, 0.104, 0.105, 0.106, 0.104, 0.103, 0.098, 0.092]
y_data_410 = [0, 0.0622, 0.076, 0.08686, 0.091, 0.09624, 0.09890, 0.09975, 0.10206, 0.10083, 0.09112, 0.086]
# Custom tick values
x_ticks = [0, 20, 40, 60, 80, 100, 120]
y_ticks = [0, 0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16]

# Create the plot
plt.figure(figsize=(8, 6))  # Optional: set the figure size

plt.plot(x_data, y_data_350, linestyle=':', label='Heater Inlet Temp = 350', color='k')
plt.plot(x_data, y_data_370, linestyle='-.', label='Heater Inlet Temp = 370', color='k')
plt.plot(x_data, y_data_390, linestyle='-', label='Heater Inlet Temp = 390', color='k')
plt.plot(x_data, y_data_410, linestyle='--', label='Heater Inlet Temp = 410', color='k')
# Customize x and y-axis ticks
plt.xticks(x_ticks)
plt.yticks(y_ticks)

plt.xlim(0, max(x_ticks))
plt.ylim(0, max(y_ticks))

plt.xlabel('Power, Q (kW)')
plt.ylabel('Mass Flow Rate, W (kg/s)')
plt.title('Mass Flow Rate vs. Power')
plt.legend(loc='lower right')

plt.text(100, 0.06, 'HHHC', fontsize=12, ha='right', va='bottom')
plt.text(100, 0.05, 'P = 30MPa', fontsize=12, ha='right', va='bottom')
plt.text(100, 0.04, 'H = 4.1m', fontsize=12, ha='right', va='bottom')
plt.text(100, 0.03, 'D = 14mm', fontsize=12, ha='right', va='bottom')

# Show the plot
plt.show()
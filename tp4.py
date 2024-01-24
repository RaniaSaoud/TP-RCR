import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define fuzzy variables
temperature = ctrl.Antecedent(np.arange(0, 111, 1), 'temperature')
speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Membership functions for temperature
temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['medium'] = fuzz.trimf(temperature.universe, [30, 50, 70])
temperature['high'] = fuzz.trimf(temperature.universe, [50, 100, 100])

# Membership functions for speed
speed['slow'] = fuzz.trimf(speed.universe, [0, 0, 50])
speed['moderate'] = fuzz.trimf(speed.universe, [30, 50, 70])
speed['fast'] = fuzz.trimf(speed.universe, [50, 100, 100])

# Membership functions for fan_speed
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [30, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['low'] & speed['slow'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['medium'] | speed['moderate'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['high'] & speed['fast'], fan_speed['high'])

fan_control = ctrl.ControlSystem([rule1, rule2, rule3])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)
fan_simulation.input['temperature'] = 85
fan_simulation.input['speed'] = 60
fan_simulation.compute()
print(fan_simulation.output['fan_speed'])
temperature.view()
speed.view()
fan_speed.view()
plt.show()

fan_simulation.compute()
fan_speed_output = fan_simulation.output['fan_speed']
print(f"Fan speed output: {fan_speed_output}")
fan_speed.view(sim=fan_simulation)
# Show the plot
plt.show()
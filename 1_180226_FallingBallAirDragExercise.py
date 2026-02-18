import numpy as np
import matplotlib.pyplot as plt

# Parameter
g = 9.81
dt = 0.01

m = 80       # Masse (kg)
c_d = 1.0    # Luftwiderstandsbeiwert
A = 0.7      # Querschnittsfläche (m²)
rho = 1.225  # Luftdichte (kg/m³)

# Startwerte
v = 0
y = 1000      
t = 0

zeiten = []
hoehen = []
geschwindigkeiten = []

while y > 0:
    F_drag = 0.5 * c_d * rho * A * v**2
    a = g - F_drag / m

    v = v + a * dt
    y = y - v * dt

    zeiten.append(t)
    hoehen.append(y)
    geschwindigkeiten.append(v)

    t = t + dt

# Terminal Velocity berechnen (theoretisch)
v_terminal = np.sqrt(2 * m * g / (c_d * rho * A))
print("Theoretische Terminal Velocity:", v_terminal, "m/s")

# Plot Geschwindigkeit
plt.plot(zeiten, geschwindigkeiten, label="v(t)")
plt.axhline(v_terminal, color='r', linestyle='--', label="v_terminal")
plt.xlabel("Zeit (s)")
plt.ylabel("Geschwindigkeit (m/s)")
plt.title("Freier Fall mit Luftwiderstand")
plt.legend()
plt.show()

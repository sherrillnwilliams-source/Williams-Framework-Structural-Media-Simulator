import matplotlib
matplotlib.use("QtAgg")
import math
import numpy as np
import matplotlib.pyplot as plt

G = 9.8
C = 3e8

def williams_velocity(S, g, h):
    return math.sqrt(2 * S * g * h)

def williams_beta(S, E):
    return -S / (1 - E)

def classical_beta(g, h, v):
    return 1 - (g*h + 0.5*v*v) / (C*C)

# Parameters
N = 80
H = 1.0
S = 3.0
E = 0.6
CP = 4.0

dz = H / N
h_vals = np.array([(i + 1) * dz for i in range(N)])
release_times = h_vals / CP

beta_W_global = williams_beta(S, E)
v_vals = np.array([williams_velocity(S, G, h) for h in h_vals])
beta_W_vals = np.array([0.0 if i == 0 else beta_W_global for i in range(N)])  # just to show scale
beta_class_vals = np.array([classical_beta(G, h, v) for h, v in zip(h_vals, v_vals)])

# Simple pressure/temperature profiles (ramp with depth)
depth = np.linspace(0, 1, N)
pressure = 0.2 + 0.8 * depth
temperature = 0.2 + 0.8 * depth

fig, axes = plt.subplots(2, 3, figsize=(14, 8))
axes = axes.ravel()

# 1. β_W vs segment
axes[0].plot(range(N), [beta_W_global]*N, color="purple")
axes[0].set_title("Williams β_W vs segment")
axes[0].set_xlabel("Segment index")
axes[0].set_ylabel("β_W")

# 2. β_class vs segment
axes[1].plot(range(N), beta_class_vals, color="green")
axes[1].set_title("Classical β vs segment")
axes[1].set_xlabel("Segment index")
axes[1].set_ylabel("β_class")

# 3. Velocity vs segment
axes[2].plot(range(N), v_vals, color="blue")
axes[2].set_title("Velocity vs segment")
axes[2].set_xlabel("Segment index")
axes[2].set_ylabel("v (m/s)")

# 4. Pressure vs segment
axes[3].plot(range(N), pressure, color="red")
axes[3].set_title("Pressure vs segment")
axes[3].set_xlabel("Segment index")
axes[3].set_ylabel("Pressure (arb.)")

# 5. Temperature vs segment
axes[4].plot(range(N), temperature, color="orange")
axes[4].set_title("Temperature vs segment")
axes[4].set_xlabel("Segment index")
axes[4].set_ylabel("Temperature (arb.)")

# 6. Release time vs segment
axes[5].plot(range(N), release_times, color="black")
axes[5].set_title("Release time vs segment")
axes[5].set_xlabel("Segment index")
axes[5].set_ylabel("t_release (s)")

plt.tight_layout()

if __name__ == "__main__":
    plt.show()


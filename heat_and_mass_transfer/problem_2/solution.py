import numpy as np
import matplotlib.pyplot as plt

# Constants
DOMAIN_SIZE = 1.0  # Domain length (m)
Nx, Ny = 50, 50    # Grid points in x and y
t_max = 1.0        # Total time (s)
dt = 0.001         # Time step (s)
alpha = 0.1        # Thermal diffusivity (m²/s)
k = 1.0            # Thermal conductivity (W/m·K)
q = 100.0          # Heat flux (W/m²)

# Grid setup
x = np.linspace(0, DOMAIN_SIZE, Nx)
dx = x[1] - x[0]
y = np.linspace(0, DOMAIN_SIZE, Ny)
dy = y[1] - y[0]
Nt = int(t_max / dt) + 1
t = np.linspace(0, t_max, Nt)

# Stability check
if alpha * dt / dx**2 > 0.25:
    raise ValueError(f"Unstable! alpha * dt / dx² > 0.25")

# Temperature array
T = np.zeros((Nt, Nx, Ny))
T[0, :, :] = 0  # Initial condition: T=0 at t=0

# Time loop
for n in range(Nt-1):
    # Compute second derivatives for interior points
    x_dim = (T[n, :-2, 1:-1] - 2*T[n, 1:-1, 1:-1] + T[n, 2:, 1:-1]) / dx**2
    y_dim = (T[n, 1:-1, :-2] - 2*T[n, 1:-1, 1:-1] + T[n, 1:-1, 2:]) / dy**2
    T[n+1, 1:-1, 1:-1] = T[n, 1:-1, 1:-1] + alpha * dt * (x_dim + y_dim)
    
    # Boundary conditions
    T[n+1, 0, :] = T[n+1, 1, :] + (q/k) * dx    # x=0: Heat flux in
    T[n+1, -1, :] = T[n+1, -2, :]               # x=1: Insulated
    T[n+1, :, 0] = T[n+1, :, 1] + (q/k) * dy    # y=0: Heat flux in
    T[n+1, :, -1] = T[n+1, :, -2]               # y=1: Insulated

# Plotting
xv, yv = np.meshgrid(x, y)
plt.figure(figsize=(12, 8))
plt.contourf(xv, yv, T[-1, :, :], levels=100, cmap='jet')
plt.colorbar(label='Temperature (°C)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title(f'Temperature at t={t_max} s')
plt.show()

# Output max/min temperatures
print(f"Max Temperature: {np.max(T[-1, :, :]):.2f} °C")
print(f"Min Temperature: {np.min(T[-1, :, :]):.2f} °C")
import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
rho = 1        # Density (kg/m^3)
mu = 0.001       # Viscosity (Pa·s)
G = 0.1     # Pressure gradient magnitude (-dp/dx, Pa/m)

# Grid parameters
ny = 31          # Number of spatial points
y_max = 1.0      # Domain length (m)
dy = y_max / (ny - 1)  # Spatial step size
y = np.linspace(0, y_max, ny)

# Time parameters
t_max = 20     # Total simulation time (s)
dt = 0.005       # Time step (s) - chosen for stability
nt = int(t_max / dt) + 1  # Number of time steps
t = np.linspace(0, t_max, nt)

# Stability check
stability = mu * dt / (rho * dy**2)
print(f"Stability parameter: {stability:.3f} (must be <= 0.5)")
if stability > 0.5:
    raise ValueError("Time step too large for stability!")

# Initialize velocity array
vx = np.zeros((nt, ny))  # v_x(t, y)
vx[0, :] = 0        # Initial condition: fluid at rest

# Time-stepping loop
for n in range(nt - 1):
    # Interior points update (finite difference)
    for i in range(1, ny - 1):
        diffusion = (vx[n, i + 1] - 2 * vx[n, i] + vx[n, i - 1]) / dy**2
        vx[n + 1, i] = vx[n, i] + dt * (G / rho + mu / rho * diffusion)
        
    # Boundary conditions
    vx[n + 1, 0] = 0.0   # Bottom plate
    vx[n + 1, -1] = 0.0  # Top plate

# Visualization
plt.figure(figsize=(12, 8))
tv, yv = np.meshgrid(t,y)
plt.contourf(tv, yv, vx.T, levels=50)
plt.colorbar(label='Velocity v_x (m/s)')
plt.xlabel('Time (s)')
plt.ylabel('y (m)')
plt.title('Evolution of v_x(y, t)')
plt.savefig('./result.png')
plt.show()
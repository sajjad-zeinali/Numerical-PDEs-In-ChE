import numpy as np
import matplotlib.pyplot as plt

# Domain parameters
L = 1          # Domain length (m)
t_total = 4    # Total time (s)
nx = 50        # Number of spatial points
nt = 500       # Number of time points
dx = L / (nx - 1)  # Spatial step size
dt = t_total / nt  # Time step size

# Physical constants
D = 0.01       # Diffusion coefficient (m^2/s)
alpha = 0.02   # Thermal diffusivity (m^2/s)
v = 0.1        # Advection velocity (m/s)
k0 = 1         # Reaction rate constant (1/s)
E = 5000       # Activation energy (J/mol)
R = 8.314      # Universal gas constant (J/mol.K)
delta_H = 100  # Heat of reaction (J/mol)

# Time and space arrays
t = np.linspace(0, t_total, nt)  # Time array
x = np.linspace(0, L, nx)        # Space array

# Main arrays for concentration and temperature
C = np.zeros((nt, nx))  # Concentration (mol/m^3)
T = np.zeros((nt, nx))  # Temperature (K)

# Initial conditions
C[0, :] = 1    # Uniform initial concentration
T[0, :] = 300  # Uniform initial temperature (K)

# Numerical solution using finite difference method
for n in range(nt - 1):
    for i in range(1, nx - 1):
        # Terms for concentration equation (C)
        diffusion_C = D * dt / dx**2 * (C[n, i-1] - 2 * C[n, i] + C[n, i+1])  # Diffusion term
        advection_C = -v * dt / dx * (C[n, i] - C[n, i-1])                    # Advection term
        reaction_C = -k0 * dt * np.exp(-E / (R * T[n, i])) * C[n, i]          # Reaction term
        
        # Update concentration
        C[n + 1, i] = C[n, i] + diffusion_C + advection_C + reaction_C

        # Terms for temperature equation (T)
        diffusion_T = alpha * dt / dx**2 * (T[n, i-1] - 2 * T[n, i] + T[n, i+1])  # Heat diffusion term
        advection_T = -v * dt / dx * (T[n, i] - T[n, i-1])                        # Heat advection term
        reaction_T = delta_H * k0 * dt * np.exp(-E / (R * T[n, i])) * C[n, i]     # Heat generation term
        
        # Update temperature
        T[n + 1, i] = T[n, i] + diffusion_T + advection_T + reaction_T

    # Boundary conditions
    C[n + 1, 0] = 1       # Fixed concentration at inlet
    T[n + 1, 0] = 300     # Fixed temperature at inlet
    C[n + 1, -1] = C[n + 1, -2]  # Zero flux at outlet for concentration
    T[n + 1, -1] = T[n + 1, -2]  # Zero flux at outlet for temperature

# Create meshgrid for plotting
xv, tv = np.meshgrid(x, t)

# Plotting
plt.figure(figsize=(12, 6))

# Concentration plot
plt.subplot(1, 2, 1)
contour_C = plt.contourf(tv, xv, C, levels=40, cmap="viridis")
plt.colorbar(contour_C, label="Concentration (mol/m³)")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Concentration Profile")

# Temperature plot
plt.subplot(1, 2, 2)
contour_T = plt.contourf(tv, xv, T, levels=40, cmap="viridis")
plt.colorbar(contour_T, label="Temperature (K)")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Temperature Profile")

plt.tight_layout()
plt.show()
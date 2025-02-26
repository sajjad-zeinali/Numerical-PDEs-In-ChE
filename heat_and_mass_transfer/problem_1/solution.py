import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
L = 1
T0 = 100
T_L = 200
k = 50
rho = 800
Cp = 1000
alpha = k / (rho * Cp)

# Time and space discretization
Nt = 500
t = np.linspace(0, 500, Nt)

Nx = 20
x = np.linspace(0, L, Nx)
dx = x[1] - x[0]

# Initial temperature distribution
T_init = 200 + 50 * np.sin(np.pi * x / L)
T_init[0] = T0
T_init[-1] = T_L

# PDE function (Method of Lines)
def rhs_pde(t, T):
    dTdt = np.zeros_like(T)
    
    # Boundary conditions
    T[0] = T0
    T[-1] = T_L
    
    # Loop version
    for i in range(1, len(T) - 1):
        dTdt[i] = alpha * (T[i + 1] - 2 * T[i] + T[i - 1]) / dx**2

    # Vectorized version (alternative to the loop)
    # dTdt[1:-1] = alpha * (T[2:] - 2 * T[1:-1] + T[:-2]) / dx**2
    return dTdt

# Solve PDE using solve_ivp
sol = solve_ivp(fun=rhs_pde, y0=T_init, t_span=[0, 500], t_eval=t)

# Create meshgrid for plotting
X, T = np.meshgrid(x, t)

# Plot temperature distribution
plt.figure(figsize=(8, 5))
plt.contourf(X, T, sol.y.T, levels=100, cmap='jet')
plt.colorbar(label='Temperature (°C)')
plt.xlabel('Position (x)')
plt.ylabel('Time (t)')
plt.title('Temperature Distribution in the Rod')

plt.show()
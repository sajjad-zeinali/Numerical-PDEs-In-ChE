import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Constants
Mg = 0.008      # Gas mass flow rate [kg/s]
Ml = 0.4        # Liquid mass flow rate [kg/s]
di = 20e-3      # Inner diameter [m]
L = 1.3         # Pipe length [m]
T = 20 + 273.15 # Temperature [K]
R = 287         # Gas constant [J/(kg·K)]
P_e = 1e5       # Initial pressure [Pa]
Vl = 1 / 1000   # Liquid specific volume [m³/kg]
g = 9.81        # Gravitational acceleration [m/s²]

# Derived parameters
omega = Mg / (Mg + Ml)  # Quality (mass fraction of gas)
G = (Ml + Mg) / (np.pi / 4 * di**2)  # Mass flux [kg/(m²·s)]

def Vg_cal(P):
    """Calculate gas specific volume using ideal gas law"""
    return R * T / P

def dVgdP(P):
    """Derivative of gas specific volume with respect to pressure"""
    return -R * T / P**2

def Vbar_cal(vg, vl):
    """Calculate homogeneous mixture specific volume"""
    return vg * omega + (1 - omega) * vl

def dPdx_sh_cal(Pe):
    """Calculate static head pressure gradient [Pa/m]"""
    return g / Vbar_cal(Vg_cal(Pe), Vl)

def dPdx_f_cal(Pe):
    """Calculate frictional pressure gradient [Pa/m]"""
    vg = Vg_cal(Pe)
    Vbar = Vbar_cal(vg, Vl)
    
    # Reynolds number calculation (using liquid viscosity)
    Re = G * di / 1.0016e-3  # Water viscosity at 20°C
    
    # Colebrook-White equation for friction factor
    def CB(f):
        return -2 * np.log10(2.51 / (Re * np.sqrt(f))) - 1 / np.sqrt(f)
    
    f = fsolve(CB, 0.02)[0] / 4  # Solving for friction factor
    
    # Pressure gradient calculation
    dPdx_LO = 2 * f * G**2 * Vl / di  # All liquid flow
    return dPdx_LO * Vbar / Vl         # Homogeneous model correction

def pressure_drop_segment(Pe, dx):
    """Calculate pressure drop over a segment dx [Pa]"""
    term1 = G**2 * omega * dVgdP(Pe)  # Compressibility term
    term2 = dPdx_f_cal(Pe)            # Frictional term
    term3 = dPdx_sh_cal(Pe)           # Static head term
    
    return (term2 + term3) / (1 + term1) * dx

# Numerical integration along pipe length
n = 20              # Number of segments
dx = L / n          # Segment length [m]
total_dP = 0        # Cumulative pressure drop [Pa]
pressure = [P_e]    # Pressure at each segment [Pa]
positions = [L]     # Positions along pipe [m]

for i in range(n):
    segment_dP = pressure_drop_segment(P_e, dx)
    P_e += segment_dP  # Update pressure for next segment
    total_dP += segment_dP
    
    # Store values for plotting
    pressure.append(P_e)
    positions.append(L - (i+1)*dx)
    
    print(f"Segment {i+1}: Position = {L - (i+1)*dx:.3f} m, Pressure = {P_e/1e5:.4f} bar, ΔP = {segment_dP/1e5:.6f} bar")

print(f"\nTotal pressure drop: {total_dP/1e5:.6f} bar")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(positions, np.array(pressure)/1e5, 'b-', linewidth=2)
plt.scatter(positions, np.array(pressure)/1e5, color='red', s=30)
plt.title('Pressure Distribution Along the Pipe', fontsize=14)
plt.xlabel('Pipe Position (m) from Inlet', fontsize=12)
plt.ylabel('Pressure (bar)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(np.arange(0, L+0.1, 0.1))
plt.yticks(np.arange(min(pressure)/1e5, max(pressure)/1e5+0.1, 0.1))
plt.tight_layout()
plt.show()
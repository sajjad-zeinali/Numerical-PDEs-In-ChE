### Problem 1: Laminar Flow Between Parallel Plates
This problem simulates the evolution of fluid velocity (`v_x`) between two stationary plates under a constant pressure gradient using the finite difference method. The governing PDE is:

**∂v_x/∂t = G/ρ + (μ/ρ) ∂²v_x/∂y²**

- **Domain**: 0 ≤ y ≤ 1 m  
- **Boundary conditions**: v_x = 0 at y = 0 and y = 1  
- **Initial condition**: v_x(t=0) = 0  
- **Parameters**:  
  - Density (ρ) = 1 kg/m³  
  - Viscosity (μ) = 0.001 Pa·s  
  - Pressure gradient (G = -dp/dx) = 0.1 Pa/m  
- **Simulation time**: 0 to 20 s  

The output shows the velocity profile development over time as a contour plot.
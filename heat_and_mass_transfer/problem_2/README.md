# Problem 2: Heat Transfer in a 2D Square Plate with Heat Flux and Insulated Boundaries

Simulate heat transfer in a 2D square plate (1 m × 1 m) governed by the 2D heat equation:

∂T/∂t = α (∂²T/∂x² + ∂²T/∂y²)

## Parameters
- Domain: x, y ∈ [0, 1] m
- Thermal diffusivity (α): 0.1 m²/s
- Thermal conductivity (k): 1 W/m·K
- Heat flux (q): 100 W/m²
- Grid: 50 × 50 points
- Time: 0 to 1 s, Δt = 0.001 s

## Conditions
- Initial: T(x, y, 0) = 0°C
- Boundaries:
  - x = 0: q = 100 W/m² (heat flux in)
  - x = 1: Insulated (∂T/∂x = 0)
  - y = 0: q = 100 W/m² (heat flux in)
  - y = 1: Insulated (∂T/∂y = 0)

## Objective
Use the finite difference method to compute the temperature distribution. Ensure stability (α * Δt / Δx² < 0.25). Plot the temperature at t = 1 s as a contour map and report max/min temperatures.
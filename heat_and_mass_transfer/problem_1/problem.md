### Problem Statement:

A **1-meter-long** rod experiences **heat conduction** over time. The temperature at the left end (**x = 0**) is **100°C**, and at the right end (**x = L = 1 m**), it is **200°C**. The initial temperature distribution along the rod is given by:

### T(x, 0) = 200 + 50 sin(πx/L)

The rod's material properties are:

*   **Thermal conductivity**: `k = 50` W/(m·K)
*   **Density**: `ρ = 800` kg/m³
*   **Specific heat capacity**: `C_p = 1000` J/(kg·K)

The **heat equation** governing this system is:

### ∂T/∂t = α (∂²T/∂x²)

where **thermal diffusivity** α is:

### α = k / (ρ * Cp)

The task is to numerically solve for the temperature distribution over time (**0 to 500 seconds**) within the rod.


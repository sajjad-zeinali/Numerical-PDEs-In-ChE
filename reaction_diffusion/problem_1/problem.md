
### Problem Statement:

A **1-meter-long** domain experiences coupled **mass and heat transfer** with a **chemical reaction** over time. The system is governed by two partial differential equations (PDEs) describing concentration (`C`) and temperature (`T`) along the domain. At the inlet (**x = 0**), the concentration is fixed at **1 mol/m³**, and the temperature is fixed at **300 K**. At the outlet (**x = L = 1 m**), zero-flux boundary conditions are applied. The initial conditions are uniform across the domain:

- **C(x, 0) = 1 mol/m³** (initial concentration)
- **T(x, 0) = 300 K** (initial temperature)

The governing equations are:

1. **Concentration equation**:  
   ∂C/∂t = D (∂²C/∂x²) - v (∂C/∂x) - k₀ e^(-E/(RT)) C  
   (Diffusion + Advection + Reaction)

2. **Temperature equation**:  
   ∂T/∂t = α (∂²T/∂x²) - v (∂T/∂x) + ΔH k₀ e^(-E/(RT)) C  
   (Diffusion + Advection + Heat generation from reaction)

The material and reaction properties are:

- **Diffusion coefficient**: `D = 0.01 m²/s`
- **Thermal diffusivity**: `α = 0.02 m²/s`
- **Advection velocity**: `v = 0.1 m/s`
- **Reaction rate constant**: `k₀ = 1 1/s`
- **Activation energy**: `E = 5000 J/mol`
- **Universal gas constant**: `R = 8.314 J/(mol·K)`
- **Heat of reaction**: `ΔH = 100 J/mol`

The task is to numerically solve for the concentration (`C`) and temperature (`T`) distributions over time (**0 to 4 seconds**) within the domain using the finite difference method.

---
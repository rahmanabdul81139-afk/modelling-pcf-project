# Modeling a Photonic Crystal Fiber (PCF) Sensor for Basal Cancer Cell Detection

A finite-element (COMSOL Multiphysics) study of a dual-side-polished, gold-coated
Photonic Crystal Fiber sensor that uses Surface Plasmon Resonance (SPR) to detect
basal cancer cell biomarkers through refractive-index shifts


## Overview

The sensor combines a Photonic Crystal Fiber with an external gold plasmonic
layer to detect minute refractive-index (RI) changes caused by cancer
biomarkers in an analyte layer. Structural parameters (air-hole diameter, core
diameter, gold-coating thickness) were optimized using a Taguchi L9 orthogonal
array, and confinement-loss behavior was further modeled with Multiple Linear
Regression (MLR) and a Multi-Layer Perceptron Artificial Neural Network
(MLP-ANN).

**Reported performance**
- Spectral sensitivity: ~1200 nm/RIU
- Amplitude sensitivity: ~112 RIU⁻¹
- Validated RI detection range: 1.33 – 1.42 (normal tissue → cancer-associated RI shift)

## Method summary

1. **Structural design** — circular-core PCF with air-hole cladding, a TOPAS
   substrate layer, an analyte layer to hold the biological sample, and a
   perfectly matched layer (PML) at the simulation boundary to absorb outgoing
   waves and prevent reflection artifacts.
2. **Material modeling** — refractive-index dispersion for TOPAS and the
   analyte was computed with the Sellmeier equation.
3. **FEM simulation (COMSOL Multiphysics)** — mesh generation, structural
   analysis, and computation of the effective refractive index and
   confinement loss (Lc) across a wavelength sweep, for analyte RI values of
   1.38, 1.39, and 1.40.
4. **Optimization** — Taguchi L9 array used to tune geometric parameters;
   MLR and MLP-ANN used to predict confinement loss and cross-check the FEM
   results.

## Repository structure

```
├── paper/
│   └── PCF_SPR_Cancer_Cell_Detection_Paper.pdf   # published conference paper
├── figures/
│   ├── fig1_cross_section.jpeg      # PCF sensor cross-section
│   ├── fig2_mesh_analysis.png       # FEM mesh
│   ├── fig3_pml_layer.jpeg          # simulated PML boundary layer
│   ├── fig4_materials.jpeg          # materials used in the sensor
│   ├── fig5_loss_vs_wavelength.jpeg # confinement loss vs wavelength (original result)
│   ├── eq_sellmeier.png             # Sellmeier dispersion equation
│   └── eq_confinement_loss.png      # confinement loss equation
├── demo/
│   ├── confinement_loss_demo.py     # illustrative reproduction of the loss-vs-wavelength trend
│   └── confinement_loss_demo.png    # output of the demo script
└── README.md
```

## Running the demo

```bash
cd demo
pip install numpy matplotlib
python confinement_loss_demo.py
```

This regenerates `confinement_loss_demo.png`, an illustrative plot showing the
same qualitative trend as Fig. 5 in the paper: the confinement-loss peak
red-shifts and grows taller as the analyte refractive index increases from
1.38 → 1.39 → 1.40.

## Tech / tools

`COMSOL Multiphysics` (FEM simulation) · `Taguchi L9 orthogonal array` (design
optimization) · `MLR`, `MLP-ANN` (loss prediction) · `Python` (illustrative
post-processing demo)


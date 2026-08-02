"""
Confinement Loss vs Wavelength — Illustrative Demo
----------------------------------------------------
The original COMSOL Multiphysics FEM project files for this sensor were
lost, so this script does NOT reproduce the exact simulation data from
the paper. Instead, it recreates the *qualitative* resonance behaviour
reported in the paper (a Lorentzian-shaped confinement-loss peak that
red-shifts and grows as the analyte refractive index increases from
1.38 -> 1.39 -> 1.40) so the trend can still be visualised and discussed
without the original FEM model.

Paper: "Modeling Photonic Crystal Fiber Sensor For Basal Cancer Cell
Detection Using Comsol Multiphysics"

Run:
    pip install numpy matplotlib
    python confinement_loss_demo.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Wavelength sweep (micrometers), roughly matching the NIR range used in the paper
wavelength = np.linspace(0.74, 1.00, 500)

# Illustrative resonance centers / peak heights per analyte refractive index.
# These are NOT extracted from the original simulation (data lost) — they are
# tuned only to reproduce the reported qualitative trend: red-shift and
# increasing peak loss as RI rises from 1.38 to 1.40.
curves = {
    1.38: {"center": 0.80, "width": 0.035, "peak": 40, "color": "blue"},
    1.39: {"center": 0.85, "width": 0.035, "peak": 55, "color": "red"},
    1.40: {"center": 0.90, "width": 0.035, "peak": 70, "color": "green"},
}


def lorentzian(x, center, width, peak):
    return peak / (1 + ((x - center) / width) ** 2)


plt.figure(figsize=(7, 5))
for ri, p in curves.items():
    loss = lorentzian(wavelength, p["center"], p["width"], p["peak"])
    plt.plot(wavelength, loss, color=p["color"], label=f"RI = {ri}")

plt.xlabel("Wavelength (µm)")
plt.ylabel("Confinement Loss, Lc (dB/cm) — illustrative")
plt.title("Illustrative Confinement Loss vs Wavelength\n(qualitative reproduction — not original simulation data)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("confinement_loss_demo.png", dpi=150)
print("Saved confinement_loss_demo.png")

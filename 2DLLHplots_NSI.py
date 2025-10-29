import matplotlib.pyplot as plt
import numpy as np
import os
import uproot
import math

# The definition of Eps_emu
def Eps_emu_imaginary(eps_emu, delta_emu):
    return abs(eps_emu)*np.exp(1j*delta_emu)

file = uproot.open("inputs/LLHScans/test_t2k_NSI_LLHscans_allstartatzero.root")

# Access the directory
nsi_dir = file["Sample_LLH"]

# Retrieve the histograms
eps_emu = nsi_dir["Eps_emu_sam"]
delta_emu = nsi_dir["Delta_emu_sam"]

# If you want to access the histogram data:
eps_emu_values, eps_emu_edges = eps_emu.to_numpy()
delta_emu_values, delta_emu_edges = delta_emu.to_numpy()

real_parts = []
imag_parts = []
LLH_values = []

for i in range(len(eps_emu_edges) - 1):
    #value = Eps_emu_imaginary(eps_emu_edges[i], delta_emu_edges[i])
    #value = Eps_emu_imaginary(eps_emu_edges[i], 1.57)
    value = Eps_emu_imaginary(0.25, delta_emu_edges[i])
    real_part = value.real
    imag_part = value.imag
    real_parts.append(value.real)
    imag_parts.append(value.imag)
    LLH_values.append(eps_emu_values[i])
    print(real_part, imag_part, eps_emu_values[i])


real_parts = np.array(real_parts)
imag_parts = np.array(imag_parts)
LLH_values = np.array(LLH_values)

# Create 2D scatter plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(real_parts, imag_parts, c=LLH_values, cmap='viridis', s=50)

# Highlight axes
plt.axhline(0, color='black', linewidth=1.5, linestyle='--')
plt.axvline(0, color='black', linewidth=1.5, linestyle='--')

# Add colorbar for LLH values
cbar = plt.colorbar(scatter)
cbar.set_label('LLH Value')

# Set axis labels and title
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Eps_emu LLH Scatter Plot')

plt.grid(True)
plt.tight_layout()
plt.savefig("Epsemu_2DLLHscans_allstartatzero_pi2deltaemu.jpg", format="jpg", dpi=300)
plt.show()
plt.close()







    



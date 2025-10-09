import matplotlib.pyplot as plt
import numpy as np
import os
import uproot

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings_NOvAbaseline.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings_NOvAbaseline.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings_NOvAbaseline.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings_NOvAbaseline.txt" : "eps_tautau = 0.25"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings.txt" : "eps_tautau = 0.25"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=0", "New_inputs/oscillation_weights_epsetaudeltaetaupi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi/2", "New_inputs/oscillation_weights_epsetaudeltaetaupi_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi", "New_inputs/oscillation_weights_epsetaudeltaetau3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline_NEW.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings_NOvAbaseline_NEW.txt" : "eps_tautau = 0.25"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_minusepsemudeltaemupi_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=0", "New_inputs/oscillation_weights_epsetaudeltaetaupi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi/2", "New_inputs/oscillation_weights_epsetaudeltaetaupi_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi", "New_inputs/oscillation_weights_epsetaudeltaetau3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=0", "New_inputs/oscillation_weights_epsetaudeltaetaupi2_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=pi/2", "New_inputs/oscillation_weights_epsetaudeltaetaupi_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=pi", "New_inputs/oscillation_weights_epsetaudeltaetau3pi2_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=3pi/2"}

custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}

#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings_NOvAbaseline_deltaCPfix.txt" : "eps_tautau = 0.25"}

text_files = list(custom_labels.keys())


# Function to find closest key within tolerance
def get_closest_value(dictionary, key, tol=1e-3):
    for k in dictionary:
        if abs(k - key) < tol:
            return dictionary[k]
    return None


#Get the data from a txt file into a dictionary
data = {}
for file_name in text_files:
    energy = []
    probability = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 7:
                    NuType = int(parts[1]) 
                    generated_flavour = int(parts[2])
                    detected_flavour = float(parts[3])  
                    energy_val = float(parts[4])
                    prob_val = float(parts[6])
                    if generated_flavour == 2 and detected_flavour ==1 and NuType == 1 and energy_val < 4 and prob_val < 0.1:
                        energy.append(energy_val)
                        probability.append(prob_val)
        data[file_name] = (energy, probability)


# Now get the data from NOvA Root files
file = uproot.open("NOvA_oscprobs/nue/P_asimov0_nue_NSI_epsemu_NO.root")

graphs = {}
for key in file.keys():
    obj = file[key]
    
    # Check if the object has TGraph-like members
    if "fX" in obj.member_names and "fY" in obj.member_names:
        x_vals = obj.member("fX")
        y_vals = obj.member("fY")
        graphs[key] = dict(zip(x_vals, y_vals))
        

# Plotting
#plt.figure(figsize=(10, 6))


# Create subplots with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6), gridspec_kw={'height_ratios': [3, 1]})

        
linestyles = ["-", "--"]

for file_name, (energy, probability) in data.items():
    if file_name == "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline_deltaCPfix.txt":
   # style = linestyles[0] if file_name == "New_inputs/oscillation_weights_allzero_onlyecouplings.txt" else linestyles[1]
        label = custom_labels.get(file_name, file_name)
        ax1.plot(energy, probability, linestyle = "-", markersize=1.5, label="T2K (OscProb)") #'o'  linemarker = style
    else:
        continue

for name, xy_dict in graphs.items():
    if name == "prob_3;1":
        x_vals = list(xy_dict.keys())
        y_vals = list(xy_dict.values())
        ax1.plot(x_vals, y_vals, linestyle='-', label="NOvA (OscLib)")
    else:
        continue

ax1.set_xlabel("Energy (GeV)")
ax1.set_ylabel("Probability")
ax1.legend()
ax1.set_ylim(0, 0.1)
#ax1.set_ylim(0, 1.2)
ax1.set_xlim(0.25, 4)
ax1.grid(True)

energy, probability_data = data["New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline_deltaCPfix.txt"]
xy_dict = graphs["prob_3;1"]

# Match energy values and compute ratio
ratio = []
for e, p_data in zip(energy, probability_data):
    p_graph = get_closest_value(xy_dict, e)
    if p_graph is not None and p_graph != 0:
        #(OscLib-OscProb)/Osc_Prob
        ratio.append((p_data-p_graph)/p_graph)
        #print(p_data, p_graph)
    else:
        ratio.append(float('nan'))  # Avoid division by zero 
        
# Plot the ratio
ax2.plot(energy, ratio, marker = 'o', linestyle='None', color='purple', label='Data / Graph Ratio')
ax2.set_title('Ratio')
ax2.set_xlabel('Energy (GeV)')
ax2.set_ylabel('Difference')
#ax2.set_ylim(-0.2, 0.2)
#ax2.set_xlim(0, 4)
ax2.grid(True)
#ax2.legend()

# Save and show the combined plot
plt.tight_layout()
plt.savefig("Comparison_plots/Diffplots_NOvAbaseline_nue_epsemudeltaemupi_025limit_CPfix.jpg", format="jpg", dpi=300)
plt.show()





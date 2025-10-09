import matplotlib.pyplot as plt
import os

# List of text files to process
#custom_labels = {"oscillation_weights_NSIallzero_DUNEbaseline.txt" : "NSI zero", "oscillation_weights_NSIepsee_DUNEbaseline.txt" : "eps_ee = 0.25", "oscillation_weights_NSIepsemu_DUNEbaseline.txt": "eps_emu = 0.25", "oscillation_weights_NSIepsetau_DUNEbaseline.txt" : "eps_etau = 0.25"}
#custom_labels = {"New_inputs/oscillation_weights_allzero.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsemumuonly.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly.txt" : "eps_tautau = 0.25"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_01couplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_01couplings.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_01couplings.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_01couplings.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_01couplings.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_01couplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_01couplings.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_01couplings.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_01couplings.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_01couplings.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_01couplings.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_01couplings.txt" : "eps_tautau = 0.25"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings.txt" : "eps_tautau = 0.25"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "New_inputs/oscillation_weights_epsemudeltaemupi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi/2", "New_inputs/oscillation_weights_epsemudeltaemupi_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "New_inputs/oscillation_weights_epsemudeltaemu3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=3pi/2"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epseeonly_onlyecouplings_NOvAbaseline.txt" : "eps_ee = 0.25", "New_inputs/oscillation_weights_epsemuonly_onlyecouplings_NOvAbaseline.txt" : "eps_emu = 0.25", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25", "New_inputs/oscillation_weights_epsmumuonly_onlyecouplings_NOvAbaseline.txt" : "eps_mumu = 0.25", "New_inputs/oscillation_weights_epsmutauonly_onlyecouplings_NOvAbaseline.txt" : "eps_mutau = 0.25", "New_inputs/oscillation_weights_epstautauonly_onlyecouplings_NOvAbaseline.txt" : "eps_tautau = 0.25"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings_NOvAbaseline.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=0", "New_inputs/oscillation_weights_epsetaudeltaetaupi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi/2", "New_inputs/oscillation_weights_epsetaudeltaetaupi_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=pi", "New_inputs/oscillation_weights_epsetaudeltaetau3pi2_onlyecouplings_NOvAbaseline.txt" : "eps_etau = 0.25 delta_etau=3pi/2"}
#custom_labels = {"New_inputs/oscillation_weights_allzero_onlyecouplings.txt" : "PMNS Model", "New_inputs/oscillation_weights_epsetauonly_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=0", "New_inputs/oscillation_weights_epsetaudeltaetaupi2_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=pi/2", "New_inputs/oscillation_weights_epsetaudeltaetaupi_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=pi", "New_inputs/oscillation_weights_epsetaudeltaetau3pi2_onlyecouplings.txt" : "eps_etau = 0.25 delta_etau=3pi/2"}

text_files = list(custom_labels.keys())

# Dictionary to store energy and probability data for each file
data = {}

# Process each file
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
                    if generated_flavour == 2 and detected_flavour == 2 and NuType == 1 and energy_val < 4 and prob_val < 1.0:
                        energy.append(energy_val)
                        probability.append(prob_val)
        data[file_name] = (energy, probability)

# Plotting
#plt.figure(figsize=(10, 6))
linestyles = ["-", "--"]
for file_name, (energy, probability) in data.items():
    style = linestyles[0] if file_name == "New_inputs/oscillation_weights_allzero_onlyecouplings.txt" else linestyles[1]
    print(file_name)
    label = custom_labels.get(file_name, file_name)
    plt.plot(energy, probability,linestyle = style, markersize=1.5, label=label) #'o'  linemarker = style

#if energy and probability:
#        plt.plot(energy, probability, 'o', markersize=3, label=filename)

plt.xlabel("Energy (GeV)")
plt.ylabel("Probability")
plt.title("Energy vs. Probability")
plt.legend()
plt.grid(True)
plt.savefig("energy_vs_probability_numudisapperance_epsilons_onlyecouplings_NOvAplotlimits.jpg", format="jpg", dpi=300)
plt.show()


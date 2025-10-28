import matplotlib.pyplot as plt
import os

# List of text files to process

#custom_labels = {"inputs/NOvA2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NOvA2020like.txt" : "PMNS Model", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epseeonly_onlyecoupling_NOvA2020like.txt" : "eps_ee = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsetauonly_onlyecoupling_NOvA2020like.txt" : "eps_etau = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NOvA2020like.txt" : "eps_mumu = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NOvA2020like.txt":"eps_mutau = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epstautauonly_onlyecoupling_NOvA2020like.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NOvA2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NOvA2020like.txt" : "PMNS Model", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=pi/2", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"} 

#custom_labels = {"inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" : "PMNS Model", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epseeonly_onlyecoupling_T2K2020_T2Kbaseline.txt" : "eps_ee = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsetauonly_onlyecoupling_T2K2020like.txt" : "eps_etau = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsmumuonly_onlyecoupling_T2K2020like.txt" : "eps_mumu = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsmutauonly_onlyecoupling_T2K2020like.txt":"eps_mutau = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epstautauonly_onlyecoupling_T2K2020like.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" : "PMNS Model", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi/2", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}

#custom_labels = {"inputs/NuFit2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "PMNS Model", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epseeonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_ee = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsetauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_etau = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_mumu = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt":"eps_mutau = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epstautauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NuFit2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "PMNS Model", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NuFit2020_NOvAbaseline.txt" :"eps_emu = 0.25 delta_emu=pi/2", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}  

#custom_labels = {"inputs/NuFit2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "PMNS Model", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epseeonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_ee = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsetauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_etau = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_mumu = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt":"eps_mutau = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epstautauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NuFit2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "PMNS Model", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NuFit2020_T2Kbaseline.txt" :"eps_emu = 0.25 delta_emu=pi/2", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}    

custom_labels = {"inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" : "PMNS Model", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi4_onlyecoupling_T2K2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=pi/4", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi/2", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi4_onlyecoupling_T2K2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=3pi/4", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemu5pi4_onlyecoupling_T2K2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu = 5pi/4", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"} 


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
                    if generated_flavour == 2 and detected_flavour == 1 and NuType == 1 and energy_val < 4 and prob_val < 1.0:
                        energy.append(energy_val)
                        probability.append(prob_val)
        data[file_name] = (energy, probability)

# Plotting
#plt.figure(figsize=(10, 6))
linestyles = ["-", "--"]
for file_name, (energy, probability) in data.items():
    style = linestyles[0] if file_name == "inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" else linestyles[1]
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
plt.savefig("energy_vs_probability_nueapperance_deltaemuextended_onlyecouplings_T2Kplotlimits.jpg", format="jpg", dpi=300)
plt.show()


import matplotlib.pyplot as plt
import numpy as np
import os
import uproot

#custom_labels = {"inputs/NOvA2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NOvA2020like.txt" : "PMNS Model", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epseeonly_onlyecoupling_NOvA2020like.txt" : "eps_ee = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsetauonly_onlyecoupling_NOvA2020like.txt" : "eps_etau = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NOvA2020like.txt" : "eps_mumu = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NOvA2020like.txt":"eps_mutau = 0.25", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epstautauonly_onlyecoupling_NOvA2020like.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NOvA2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NOvA2020like.txt" : "PMNS Model", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=pi/2", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NOvA2020_NOvAbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NOvA2020like.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"} 

#custom_labels = {"inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" : "PMNS Model", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epseeonly_onlyecoupling_T2K2020_T2Kbaseline.txt" : "eps_ee = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsetauonly_onlyecoupling_T2K2020like.txt" : "eps_etau = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsmumuonly_onlyecoupling_T2K2020like.txt" : "eps_mumu = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsmutauonly_onlyecoupling_T2K2020like.txt":"eps_mutau = 0.25", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epstautauonly_onlyecoupling_T2K2020like.txt" : "eps_tautau = 0.25"}

custom_labels = {"inputs/T2K2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_T2K2020like.txt" : "PMNS Model", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi/2", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/T2K2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_T2K2020like.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}

#custom_labels = {"inputs/NuFit2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "PMNS Model", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epseeonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_ee = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsetauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_etau = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_mumu = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt":"eps_mutau = 0.25", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epstautauonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NuFit2020_NOvAbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "PMNS Model", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NuFit2020_NOvAbaseline.txt" :"eps_emu = 0.25 delta_emu=pi/2", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NuFit2020_NOvAbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NuFit2020_NOvAbaseline.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}  

#custom_labels = {"inputs/NuFit2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "PMNS Model", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epseeonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_ee = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsetauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_etau = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsmumuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_mumu = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsmutauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt":"eps_mutau = 0.25", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epstautauonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_tautau = 0.25"}

#custom_labels = {"inputs/NuFit2020_T2Kbaseline/oscillation_weights_PMNSonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "PMNS Model", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemuonly_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=0", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi2_onlyecoupling_NuFit2020_T2Kbaseline.txt" :"eps_emu = 0.25 delta_emu=pi/2", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemupi_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu=pi", "inputs/NuFit2020_T2Kbaseline/oscillation_weights_epsemudeltaemu3pi2_onlyecoupling_NuFit2020_T2Kbaseline.txt" : "eps_emu = 0.25 delta_emu = 3pi/2"}    


text_files = list(custom_labels.keys())

#Values are bit annoying so have to add tolerance to get the closest value
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
                    # NuType 1 neutrinos, NuType 1 anti-neutrinos
                    #generated 2 detected 1 -> Nue appearance, generated 2 detected 2 -> Numu disappeareance
                    if generated_flavour == 2 and detected_flavour == 1 and NuType == 1 and energy_val < 4: #and prob_val < 0.1:
                        energy.append(energy_val)
                        probability.append(prob_val)
        data[file_name] = (energy, probability)



# Now get the data from NOvA root files
#file = uproot.open("inputs/NOvA2020_NOvAbaseline_OscLib/nova2020/P_nova2020_nue_NSI_eps_general_NO.root")
file = uproot.open("inputs/NOvA2020_NOvAbaseline_OscLib/nova2020/P_nova2020_nue_NSI_epsemu_NO.root") 
#file = uproot.open("inputs/T2K2020_T2Kbaseline_OscLib/t2k2020/P_t2k2020_nue_NSI_eps_general_NO.root")
#file = uproot.open("inputs/T2K2020_T2Kbaseline_OscLib/t2k2020/P_t2k2020_numu_NSI_epsemu_NO.root")
#file = uproot.open("inputs/NuFit2020_NOvAbaseline_OscLib/nufit2020-nova/P_nufit2020-nova_numu_NSI_eps_general_NO.root")
#file = uproot.open("inputs/NuFit2020_NOvAbaseline_OscLib/nufit2020-nova/P_nufit2020-nova_nue_NSI_epsemu_NO.root") 
#file = uproot.open("inputs/NuFit2020_T2Kbaseline_OscLib/nufit2020-t2k/P_nufit2020-t2k_nue_bar_NSI_eps_general_NO.root")
#file = uproot.open("inputs/NuFit2020_T2Kbaseline_OscLib/nufit2020-t2k/P_nufit2020-t2k_numu_bar_NSI_epsemu_NO.root")

graphs = {}
for key in file.keys():
    obj = file[key]
    
    # Check if the object has TGraph-like members
    if "fX" in obj.member_names and "fY" in obj.member_names:
        x_vals = obj.member("fX")
        y_vals = obj.member("fY")
        graphs[key] = dict(zip(x_vals, y_vals))

#Let's do some loops
for idx, (file_name, label) in enumerate(custom_labels.items()):
    energy, probability = data[file_name]
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6), gridspec_kw={'height_ratios': [3, 1]})
    # Plot T2K OscProb subplots
    ax1.plot(energy, probability, linestyle="-", markersize=1.5, label="T2K (OscProb)")

    # Get corresponding NOvA OscLib TGraph
    graph_key = f"prob_{idx};1"
    if graph_key in graphs:
        xy_dict = graphs[graph_key]
        x_vals = list(xy_dict.keys())
        y_vals = list(xy_dict.values())
        ax1.plot(x_vals, y_vals, linestyle='-', label="NOvA (OscLib)")

        # Compute ratio
        ratio = []
        for e, p_data in zip(energy, probability):
            p_graph = get_closest_value(xy_dict, e)
            if p_graph is not None and p_graph != 0:
                ratio.append((p_data - p_graph) / p_graph)
            else:
                ratio.append(float('nan'))

        # Plot ratio
        ax2.plot(energy, ratio, marker='o', linestyle='None', color='purple', label='Data / Graph Ratio')

    ax1.set_ylabel("Probability")
    ax1.legend()
    #ax1.set_ylim(0, 0.1)
    ax1.set_xlim(0.25, 4)
    ax1.grid(True)

    ax2.set_title('Ratio')
    ax2.set_xlabel('Energy (GeV)')
    ax2.set_ylabel('Difference')
    ax2.grid(True)

    plt.tight_layout()

    # Save plots 
    label_clean = label.replace(" ", "_").replace("=", "").replace("/", "")
    output_path = f"Diffplots_NOvA2020Asimov_NOvAbaseline_nue_{label_clean}_TEST.jpg"
    plt.savefig(output_path, format="jpg", dpi=300)
    plt.close()





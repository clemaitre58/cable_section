import numpy as np


norm_cable_section = [1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300]

def select_sec(du_100, du_max) :

    for i in range(du_100.size) :
        if du_100[i] >= du_max :
            section = norm_cable_section[i-1]

    return section



def compute_sec_tri(du_max, length, Ib, alu_cuivre, cos_phi) :

    norm_cable_section_array = np.array(norm_cable_section)
    sin_phi = np.sin(np.arccos(cos_phi))
    if alu_cuivre == 'ALU' :
        R = 36 / norm_cable_section
    else :
        R = 22.5 / norm_cable_section_array

    X = 0.08

    dU = np.sqrt(3) * Ib * length * (R * cos_phi + X * sin_phi)
    du_100 = dU / 400 * 100

    section = select_sec(du_100, du_max)
    return section



if __name__ == "__main__" :
    section = compute_sec_tri(2, 0.02, 100, 'CUIVRE', 0.85)

    print("section minimale : ", section)
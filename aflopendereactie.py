import matplotlib.pyplot as plt
import math

#startwaarden
Sn2_conc = 0.4
Sn4_conc = 0
H2O2_conc = 0.4
OH_conc = 0
k = 0.8

time = 0
time_max = 15
dt = 0.02

#sets om waarden in te zetten
Sn2_conc_set = []
Sn4_conc_set = []
H2O2_conc_set = []
OH_conc_set = []

time_set = []

#startwaarden invullen
Sn2_conc_set.append(Sn2_conc)
Sn4_conc_set.append(Sn4_conc)
H2O2_conc_set.append(H2O2_conc)
OH_conc_set.append(OH_conc)

time_set.append(time)

#nieuwe waarden berekenen en invullen
while time <= time_max:

#alle veranderingen gelijk stellen aan 0
    d_Sn2 = 0
    d_Sn4 = 0
    d_H2O2 = 0
    d_OH = 0

#reactiesnelheid berekenen
    rate = k * Sn2_conc * H2O2_conc

#veranderingen door verloop berekenen
    d_Sn2 -= rate * dt
    d_Sn4 += rate * dt
    d_H2O2 -= rate * dt
    d_OH += rate * dt * 2

#nieuwe waarden berekenen
    Sn2_conc += d_Sn2
    Sn4_conc += d_Sn4
    H2O2_conc += d_H2O2
    OH_conc += d_OH

    time += dt

#nieuwe waarden invullen in sets
    Sn2_conc_set.append(Sn2_conc)
    Sn4_conc_set.append(Sn4_conc)
    H2O2_conc_set.append(H2O2_conc)
    OH_conc_set.append(OH_conc)

    time_set.append(time)

#grafiek maken
plt.plot(time_set, Sn4_conc_set)
plt.xlabel("tijd")
plt.ylabel("Concentratie Sn4+")
plt.grid(True)
plt.xlim(0, time_max)
plt.ylim(0, 0.5)
plt.show()

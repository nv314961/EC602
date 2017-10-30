# Copyright 2017 Nick VanDeusen nv314961@bu.edu

# Estimated number of atoms in the Earth
atomCount = 1*(10**50)

# The major components of Earth (%)
nitrogen = 0.78
oxygen = 0.21
water = 0.01

# Electron counts
n_electrons = 7 # number of electrons in a nitrogen atom
o_electrons = 8 # number of electrons in an oxygen atom
w_electrons = 8 # number of electrons in an h2o atom

# Estimated "bits"
bits = atomCount*(nitrogen*n_electrons + oxygen*o_electrons + water*w_electrons)

# Convert bits to terabytes
Tbytes = bits/(8*(10**12))

# Calc upper and lower bounds pr results
upper = Tbytes + Tbytes/2
lower = Tbytes - Tbytes/2
print(Tbytes)
print(lower)
print(upper)
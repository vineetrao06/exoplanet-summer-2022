# From https://www.hs.uni-hamburg.de/DE/Ins/Per/Czesla/PyA/PyA/pyaslDoc/aslDoc/keplerOrbit.html
# For educational purposes

from __future__ import print_function, division
from PyAstronomy import pyasl

# Instantiate the solver
ks = pyasl.MarkleyKESolver()

# Solves Kepler's Equation for a set
# of mean anomaly and eccentricity.
# Uses the algorithm presented by
# Markley 1995.
M = 0.75
e = 0.3
print("Eccentric anomaly: ", ks.getE(M, e))

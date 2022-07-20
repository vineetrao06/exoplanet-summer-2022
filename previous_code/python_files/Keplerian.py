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
# ==================================================================
from __future__ import print_function, division
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pylab as plt

# Instantiate a Keplerian elliptical orbit with
# semi-major axis of 1.3 length units,
# a period of 2 time units, eccentricity of 0.5,
# longitude of ascending node of 70 degrees, an inclination
# of 10 deg, and a periapsis argument of 110 deg.
ke = pyasl.KeplerEllipse(1.3, 2., e=0.5, Omega=70., i=10.0, w=110.0)

# Get a time axis
t = np.linspace(0, 1.9, 200)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = ke.xyzPos(t)
print("Shape of output array: ", pos.shape)

# x, y, and z coordinates for 50th time point
print("x, y, z for 50th point: ", pos[50, ::])

# Calculate orbit radius as a function of the
radius = ke.radius(t)

# Calculate velocity on orbit
vel = ke.xyzVel(t)

# Find the nodes of the orbit (Observer at -z)
ascn, descn = ke.xyzNodes_LOSZ()

# Plot x and y coordinates of the orbit
plt.subplot(2,1,1)
plt.title("Periapsis (red diamond), Asc. node (green circle), desc. node (red circle)")
plt.xlabel("East ->")
plt.ylabel("North ->")
plt.plot([0], [0], 'k+', markersize=9)
plt.plot(pos[::,1], pos[::,0], 'bp')
# Point of periapsis
plt.plot([pos[0,1]], [pos[0,0]], 'rd')
# Nodes of the orbit
plt.plot([ascn[1]], [ascn[0]], 'go', markersize=10)
plt.plot([descn[1]], [descn[0]], 'ro', markersize=10)
# Plot RV
plt.subplot(2,1,2)
plt.xlabel("Time")
plt.ylabel("Radial velocity [length/time]")
plt.plot(t, vel[::,2], 'r.-')
plt.show()

import math
​
​
orbper = input('pl_orbper:')
orbsmax = input('pl_orbsmax:')
star = input('st_mass:')
​
#resolving the top of the formula
upper = 4*((float(math.pi))**2)*(((float(orbsmax))*1.496*(10**11))**3)
​
#resolving bottom of formula
lower = ((float(orbper)*86400)**2)*6.67408*(10**(-11))
​
prelim = float(upper)/float(lower)
​
#subtracting by star mass to get planet mass
mass = float(prelim)-(float(star)*1.989*(10**30))

print(mass)
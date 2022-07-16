# Beginning

import numpy as np

import pandas as pd

import matplotlib

import matplotlib.pyplot as plt



np.set_printoptions(threshold=np.nan)

pd.options.display.max_seq_items = 320



# This file was produced by the NASA Exoplanet Archive  http://exoplanetarchive.ipac.caltech.edu

# Wed Sep 26 15:41:09 2018

#

# COLUMN fpl_bmasse:     Planet Mass or M*sin(i) [Earth mass]

# COLUMN fpl_bmasseerr1: Planet Mass or M*sin(i) Upper Unc. [Earth mass]

# COLUMN fpl_bmasseerr2: Planet Mass or M*sin(i) Lower Unc. [Earth mass]

# COLUMN fpl_bmasselim:  Planet Mass or M*sin(i) [Earth mass] Limit Flag

# COLUMN fpl_rade:       Planet Radius [Earth radii]

# COLUMN fpl_radeerr1:   Planet Radius Upper Unc. [Earth radii]

# COLUMN fpl_radeerr2:   Planet Radius Lower Unc. [Earth radii]

# COLUMN fpl_radelim:    Planet Radius [Earth radii] Limit Flag

# COLUMN fpl_dens:       Planet Density [g/cm**3]

# COLUMN fpl_denserr1:   Planet Density Upper Unc. [g/cm**3]

# COLUMN fpl_denserr2:   Planet Density Lower Unc. [g/cm**3]

# COLUMN fpl_denslim:    Planet Density [g/cm**3] Limit Flag

# COLUMN fst_mass:       Stellar Mass [Solar mass]

# COLUMN fst_masserr1:   Stellar Mass Upper Unc. [Solar mass]

# COLUMN fst_masserr2:   Stellar Mass Lower Unc. [Solar mass]

# COLUMN fst_masslim:    Stellar Mass [Solar mass] Limit Flag

# COLUMN fst_rad:        Stellar Radius [Solar radii]

# COLUMN fst_raderr1:    Stellar Radius Upper Unc. [Solar radii]

# COLUMN fst_raderr2:    Stellar Radius Lower Unc. [Solar radii]

# COLUMN fst_radlim:     Stellar Radius [Solar radii] Limit Flag

#

data=pd.read_csv('Nasa.Mass.Radius.Density.csv', low_memory='False')#('exoplanets.csv', low_memory='False') 



fig=plt.gcf()



fig.set_size_inches(14.4,9.6)



plt.title('Exoplanet density', fontsize=16)



#plt.gcf().set_facecolor('green') 



plt.ylabel('g/cm3', color='#000000', fontsize=16)



plt.xlabel('Earth Radii', color='#000000', fontsize=16)



plt.axis([0.2, 30, 0.1, 10]) # [xmin, xmax, ymin, ymax]



plt.grid(which='major', axis='both', color='black', linestyle='-') # axis='x' or 'y'. 



plt.minorticks_on() 



plt.grid(which='minor', axis='both', color='#AAAAAA', linestyle='dotted')



ax=plt.gca()



ax.set_xscale('log')



ax.set_yscale('log')



a=np.ones(500) # array of 5 floats

radius_list=np.ndarray.tolist(a)



for count in range(500):

    radius_list[count]=count*(0.1)

density_list = 100*np.ones(500)



upper_ratio=1.05

lower_ratio=0.95

count=0

mark_color=['#000000','#000000','#000000','#000000','#000000','#000000','#000000','#000000']

for x in range(0,len(data),1):

    if True:#data.loc[x,'TRANSIT']==1 and data.loc[x,'EOD']==1:

        mass=data.loc[x,'fpl_bmasse']#317.828*

        radius=data.loc[x,'fpl_rade']#11.21* 

        if (mass>0) and (radius>0):

            type=0

            count+=1

            density = 5.51*mass/(radius**3)

            if radius < 0.9:

                correct_density=(3.6-3.34*1.45)*(0.5**3)*(radius**-3) + 3.34*1.45 

                ratio = density/correct_density 

                if ratiolower_ratio:

                    type=1 

            elif radius < 1.5:

                correct_density=(4.8-3.34*2)*(0.9**3)*(radius**-3) + 3.34*2 

                ratio = density/correct_density 

                if ratiolower_ratio:

                    type=2

            elif radius < 4:

                correct_density=(6.1-1.15)*(1.48**3)*(radius**-3) + 1.15 

                ratio = density/correct_density 

                if ratiolower_ratio:

                    type=3

            elif radius < 6.2:

                correct_density=(1.4-(0.782))*(4.11**3)*(radius**-3) + 0.782 

                ratio = density/correct_density 

                if ratiolower_ratio:

                    type=4

            elif density < 1.6:

                correct_density=(1.5-0.0708)*(10.5**3)*(radius**-3) + 0.0708 

                ratio = density/correct_density 

                if ratiolower_ratio:

                    type=6

                elif density<correct_density:                    correct_density=0.005*radius**3-0.0942857*radius**2+0.613571*(radius) - 0.337714                    ratio = density/correct_density                     if ratiolower_ratio:

                       type=5

                    else:

                        correct_density=0.00333*radius**3-0.0632143*radius**2+0.375595*radius + 0.0517143

                        ratio = density/correct_density 

                        if ratiolower_ratio:

                           type=7

                else:

                    type=0

            plt.plot(radius, data.loc[x,'fpl_dens'], marker='.', color=mark_color[type], markerfacecolor='#000000', markersize=2, fillstyle='full') 

print ("Loop finished")

print (count)



plt.text(15,0.085,"NASA exoplanet archive", fontsize=12, ) 



plt.savefig('Exoplanet.Density.png', dpi=100) # must come before the show command. Width in pixels = dpi * 6.4



plt.show() 





https://forums.craigslist.org/?ID=294464295

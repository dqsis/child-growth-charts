# Graphical assessment of a child's development 
# according to the World Health Organization growth standards 

# Repository & documentation:
# http://github.com/dqsis/child-growth-charts
# -------------------------------------


# Import libraries
import os
from sys import exit

import numpy as np
import matplotlib.pyplot as plt


# I/O files path
path = 'data/'


# Read child's data (user input)
chdata = 'child_data.csv'


# Gender (male or female)
childfile = open(os.path.join(path,chdata))
genderline = childfile.readline()

# Age, weight, height, head circumference
charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skiprows=2)

# ---
# Not required! Missing data ignored by plotting! 
# Remove rows with missing data | code snippet source: http://bit.ly/ZLKBCA 
# charray = charray[~np.isnan(charray).any(axis=1)]
# ---

if genderline[7] == 'f':
    # read girls' (0-2) WHO charts
    # Read age vs weight WHO data
    awdata = 'g_age_weight.csv'
    awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
    # Read age vs length WHO data
    aldata = 'g_age_length.csv'
    alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
    # Read age vs head circumference WHO data
    ahdata = 'g_age_headc.csv'
    aharray = np.loadtxt(os.path.join(path,ahdata), delimiter=',', skiprows=1)
    # Read lenght vs weight WHO data
    lwdata = 'g_length_weight.csv'
    lwarray = np.loadtxt(os.path.join(path,lwdata), delimiter=',', skiprows=1)
else:
    print('no data available for boys yet')
    exit()
   
    
# Plots
plt.figure()


# Age vs weight
plt.subplot(2,2,1)
plt.plot(\
awarray[:,0],awarray[:,1],'r--',\
awarray[:,0],awarray[:,2],'r--',\
awarray[:,0],awarray[:,3],'r--',\
awarray[:,0],awarray[:,4],'r--',\
awarray[:,0],awarray[:,5],'k-',\
awarray[:,0],awarray[:,6],'r--',\
awarray[:,0],awarray[:,7],'r--',\
awarray[:,0],awarray[:,8],'r--',\
awarray[:,0],awarray[:,9],'r--',\
charray[:,0],charray[:,1],'bo')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('weight [kg]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3)) 

plt.text(awarray[13,0], awarray[13,1],'2%',fontsize=6)
plt.text(awarray[14,0], awarray[14,2],'5%',fontsize=6)
plt.text(awarray[15,0], awarray[15,3],'10%',fontsize=6)
plt.text(awarray[16,0], awarray[16,4],'25%',fontsize=6)
plt.text(awarray[17,0], awarray[17,5],'50%',fontsize=6)
plt.text(awarray[18,0], awarray[18,6],'75%',fontsize=6)
plt.text(awarray[19,0], awarray[19,7],'90%',fontsize=6)
plt.text(awarray[20,0], awarray[20,8],'95%',fontsize=6)
plt.text(awarray[21,0], awarray[21,9],'98%',fontsize=6)


# Age vs length
plt.subplot(2,2,2)
plt.plot(\
alarray[:,0],alarray[:,1],'r--',\
alarray[:,0],alarray[:,2],'r--',\
alarray[:,0],alarray[:,3],'r--',\
alarray[:,0],alarray[:,4],'r--',\
alarray[:,0],alarray[:,5],'k-',\
alarray[:,0],alarray[:,6],'r--',\
alarray[:,0],alarray[:,7],'r--',\
alarray[:,0],alarray[:,8],'r--',\
alarray[:,0],alarray[:,9],'r--',\
charray[:,0],charray[:,2],'bo')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('length [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3))


# Age vs head circumference
plt.subplot(2,2,3)
plt.plot(\
aharray[:,0],aharray[:,1],'r--',\
aharray[:,0],aharray[:,2],'r--',\
aharray[:,0],aharray[:,3],'r--',\
aharray[:,0],aharray[:,4],'r--',\
aharray[:,0],aharray[:,5],'k-',\
aharray[:,0],aharray[:,6],'r--',\
aharray[:,0],aharray[:,7],'r--',\
aharray[:,0],aharray[:,8],'r--',\
aharray[:,0],aharray[:,9],'r--',\
charray[:,0],charray[:,3],'bo')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('head circumference [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3)) 


# Length vs weight
plt.subplot(2,2,4)
plt.plot(\
lwarray[:,0],lwarray[:,1],'r--',\
lwarray[:,0],lwarray[:,2],'r--',\
lwarray[:,0],lwarray[:,3],'r--',\
lwarray[:,0],lwarray[:,4],'r--',\
lwarray[:,0],lwarray[:,5],'k-',\
lwarray[:,0],lwarray[:,6],'r--',\
lwarray[:,0],lwarray[:,7],'r--',\
lwarray[:,0],lwarray[:,8],'r--',\
lwarray[:,0],lwarray[:,9],'r--',\
charray[:,2],charray[:,1],'bo')

plt.grid(True)
plt.xlabel('lenght [cm]')
plt.ylabel('weight [kg]')
plt.xlim([45,110])
plt.xticks(np.arange(45,111,10)) 

# Adjust distance between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs
plt.show()

plt.savefig(os.path.join(path,'growth.pdf'))
plt.savefig(os.path.join(path,'growth.png'))

# END +++

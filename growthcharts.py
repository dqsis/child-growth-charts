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
from io import BytesIO
import io

# I/O files path
path = 'data/'


# Read child's data (user input)
chdata = 'child_data.csv'


# Gender (male or female)
childfile = open(os.path.join(path,chdata))
genderline = childfile.readline()

# Age, weight, height, head circumference
charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', dtype = None, skip_header=2)

# ---
# Not required! Missing data ignored by plotting!
# Remove rows with missing data | code snippet source: http://bit.ly/ZLKBCA
# charray = charray[~np.isnan(charray).any(axis=1)]
# ---
#Ended up with bruteforce! please let me know good solution without removing entire row.
chawarrayX = []
chalarrayX = []
chaharrayX = []
chlwarrayX = []
chawarrayY = []
chalarrayY = []
chaharrayY = []
chlwarrayY = []
# sublist[0] : Age
# sublist[1] : Weight
# sublist[2] : Length
#sublist[3] : Headc
for sublist in charray :
    if(~np.isnan(sublist[1])):
        chawarrayX.append(sublist[0])
        chawarrayY.append(sublist[1])
    if(~np.isnan(sublist[2])):
        chalarrayX.append(sublist[0])
        chalarrayY.append(sublist[2])
    if(~np.isnan(sublist[3])):
        chaharrayX.append(sublist[0])
        chaharrayY.append(sublist[3])
    if(~np.isnan(sublist[2]) and ~np.isnan(sublist[1])):
        temp = [sublist[2],sublist[1]]
        chlwarrayX.append(sublist[2])
        chlwarrayY.append(sublist[1])

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
    # read boys' (0-2) WHO charts
    # Read age vs weight WHO data
    awdata = 'b_age_weight.csv'
    awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
    # Read age vs length WHO data
    aldata = 'b_age_length.csv'
    alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
    # Read age vs head circumference WHO data
    ahdata = 'b_age_headc.csv'
    aharray = np.loadtxt(os.path.join(path,ahdata), delimiter=',', skiprows=1)
    # Read lenght vs weight WHO data
    lwdata = 'b_length_weight.csv'
    lwarray = np.loadtxt(os.path.join(path,lwdata), delimiter=',', skiprows=1)


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
chawarrayX,chawarrayY,'b-*')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('weight [kg]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3))

plt.text(awarray[13,0], awarray[13,1],'2%',fontsize=7)
plt.text(awarray[14,0], awarray[14,2],'5%',fontsize=7)
plt.text(awarray[15,0], awarray[15,3],'10%',fontsize=7)
plt.text(awarray[16,0], awarray[16,4],'25%',fontsize=7)
plt.text(awarray[17,0], awarray[17,5],'50%',fontsize=7)
plt.text(awarray[18,0], awarray[18,6],'75%',fontsize=7)
plt.text(awarray[19,0], awarray[19,7],'90%',fontsize=7)
plt.text(awarray[20,0], awarray[20,8],'95%',fontsize=7)
plt.text(awarray[21,0], awarray[21,9],'98%',fontsize=7)


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
chalarrayX,chalarrayY,'b-*')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('length [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3))

plt.text(alarray[13,0], alarray[13,1],'2%',fontsize=7)
plt.text(alarray[14,0], alarray[14,2],'5%',fontsize=7)
plt.text(alarray[15,0], alarray[15,3],'10%',fontsize=7)
plt.text(alarray[16,0], alarray[16,4],'25%',fontsize=7)
plt.text(alarray[17,0], alarray[17,5],'50%',fontsize=7)
plt.text(alarray[18,0], alarray[18,6],'75%',fontsize=7)
plt.text(alarray[19,0], alarray[19,7],'90%',fontsize=7)
plt.text(alarray[20,0], alarray[20,8],'95%',fontsize=7)
plt.text(alarray[21,0], alarray[21,9],'98%',fontsize=7)

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
chaharrayX,chaharrayY,'b-*')

plt.grid(True)
plt.xlabel('age [months]')
plt.ylabel('head circumference [cm]')
plt.xlim([0,24])
plt.xticks(np.arange(0,25,3))

plt.text(aharray[13,0], aharray[13,1],'2%',fontsize=7)
plt.text(aharray[14,0], aharray[14,2],'5%',fontsize=7)
plt.text(aharray[15,0], aharray[15,3],'10%',fontsize=7)
plt.text(aharray[16,0], aharray[16,4],'25%',fontsize=7)
plt.text(aharray[17,0], aharray[17,5],'50%',fontsize=7)
plt.text(aharray[18,0], aharray[18,6],'75%',fontsize=7)
plt.text(aharray[19,0], aharray[19,7],'90%',fontsize=7)
plt.text(aharray[20,0], aharray[20,8],'95%',fontsize=7)
plt.text(aharray[21,0], aharray[21,9],'98%',fontsize=7)


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
chlwarrayX,chlwarrayY,'b-*')

plt.grid(True)
plt.xlabel('lenght [cm]')
plt.ylabel('weight [kg]')
plt.xlim([45,110])
plt.xticks(np.arange(45,111,10))

plt.text(lwarray[73,0], lwarray[73,1],'2%',fontsize=7)
plt.text(lwarray[80,0], lwarray[80,2],'5%',fontsize=7)
plt.text(lwarray[87,0], lwarray[87,3],'10%',fontsize=7)
plt.text(lwarray[94,0], lwarray[94,4],'25%',fontsize=7)
plt.text(lwarray[101,0], lwarray[101,5],'50%',fontsize=7)
plt.text(lwarray[108,0], lwarray[108,6],'75%',fontsize=7)
plt.text(lwarray[115,0], lwarray[115,7],'90%',fontsize=7)
plt.text(lwarray[122,0], lwarray[122,8],'95%',fontsize=7)
plt.text(lwarray[125,0], lwarray[125,9],'98%',fontsize=7)

# Adjust distance between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Show & save graphs
fig1 = plt.gcf()
plt.show()
plt.draw()

fig1.set_size_inches(16, 9)
fig1.savefig(os.path.join(path,'growth.pdf'), dpi=100)
fig1.savefig(os.path.join(path,'growth.png'), dpi=100)

# END +++

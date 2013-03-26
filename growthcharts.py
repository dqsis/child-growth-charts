# growthcharts.py

# START +++

# import libraries
import numpy as np
import os
import matplotlib.pyplot as plt

# i/o files path
path = 'data/'

# read child's data (user input)
chdata = 'child_data.csv'
charray = np.genfromtxt(os.path.join(path,chdata), delimiter=',', skiprows=1)
# remove rows with missing data | code snippet source: http://bit.ly/ZLKBCA 
charray = charray[~np.isnan(charray).any(axis=1)]

# Read age vs weight WHO data
awdata = 'age_weight.csv'
awarray = np.loadtxt(os.path.join(path,awdata), delimiter=',', skiprows=1)
# Read age vs length WHO data
aldata = 'age_length.csv'
alarray = np.loadtxt(os.path.join(path,aldata), delimiter=',', skiprows=1)
# Read age vs head circumference WHO data
ahdata = 'age_headc.csv'
aharray = np.loadtxt(os.path.join(path,ahdata), delimiter=',', skiprows=1)
# Read lenght vs weight WHO data
lwdata = 'length_weight.csv'
lwarray = np.loadtxt(os.path.join(path,lwdata), delimiter=',', skiprows=1)

# plots
plt.figure()

# age vs weight
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

# age vs length
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

# age vs head circumference
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

# length vs weight
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

# adjust distance between subplots
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# show graphs
plt.show()

# save figures to .pdf and .png files
plt.savefig(os.path.join(path,'growth.pdf'))
plt.savefig(os.path.join(path,'growth.png'))

# END +++

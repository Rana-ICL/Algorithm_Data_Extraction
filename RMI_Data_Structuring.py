
"""
Algorithm for extracting crucial information of Richtmyer-Meshkov Instabilites
e.g. amplitude, neck, stream, span
@author: Matar Fluid Group at Imperial College London 
         Developed within the PhD. project "Richtmyer-Meshkov Instabilities in Newtonian and non-Newtonian Flows"
         PhD. candidate Usman Rana Mohammad, Dr. Thomas Abadie, Prof. Omar Matar         
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import math


# Data structuring part

# Read the data
data = pd.read_csv("New024.txt")
data=data.sort_values(by=['y'])
#yuni=data["y"]
#y_array=yuni.unique()
#y_len=len(y_array)
#RMI_sort=pd.DataFrame()

# Sort the data in ascending order [y]

#for x in range(0,y_len,1):
 #   y_inc=y_array[x]
  #  c=data[(data["y"]==y_inc)]
   # csort=c.sort_values(by=['x'])
    #RMI_sort=RMI_sort.append(csort,ignore_index=True)         

# Save the structed data to a .csv file
#RMI_sort.to_csv('structuredData.csv')


# Define the interface
Interface=data[(0.48<= data["alpha.air"]) & (data["alpha.air"]<=0.52)]

# Post processing algorithm to find the size of RMI structures e.g. amplitude, neck, stream , span
# Algorithm type: brute force search




# visualize the current RMI shape
pltidata=Interface
pltdata = pltidata.sort_values(by=['y'])

pltyvalues = np.array(pltdata['y'])
pltxvalues = np.array(pltdata['x'])
plt.figure()
plt.plot(pltxvalues,pltyvalues,linestyle='',markersize=0.5,marker='*')
plt.show()




# Compute the amplitude
# Find the minimum and maximum x values with the Interface
yn_min=1.0
Interface_half=Interface[(yn_min<= Interface["y"])]
x_loca_min=Interface_half["x"].min()
x_loca_max=Interface_half["x"].max()
amplitude=(x_loca_max-x_loca_min)
amp_max=Interface_half[(Interface_half["x"]==x_loca_max)]
amp_min=Interface_half[(Interface_half["x"]==x_loca_min)]
amp_max_last= amp_max.iloc[[-1]]
amp_min_last=amp_min.iloc[[-1]]
amp_max_x=amp_max_last["x"]
amp_max_y=amp_max_last["y"]
amp_min_x=amp_min_last["x"]
amp_min_y=amp_min_last["y"]
print(amp_max_x)
print(amp_min_x)
amplitude=amp_max_x-amp_min_x
print(amplitude)
#amphalf=amplitude/2
#print(amphalf)


# check if the RMI has reached the multivalue time 



# Compute the neck

# Define the boundaries
yn_max=1.75
yn_min=1.0
Interface_ynlimit=Interface[(yn_min<= Interface["y"]) & (Interface["y"]<=yn_max)]
xn_max=17
xn_min=15.4
Interface_xnlimit=Interface_ynlimit[(xn_min<= Interface_ynlimit["x"]) & (Interface_ynlimit["x"]<=xn_max)]
nyloc=Interface_xnlimit["y"].min()

pltneck=Interface_xnlimit[Interface_xnlimit["y"]==nyloc]
neck_dat=pltneck.iloc[[-1]]
neck_x=neck_dat["x"]
neck_y=neck_dat["y"]
print("neck",((neck_y-1)*2)/2)


# Compute the span
# Define the boundaries
ys_min=float(amp_min_y)
Interface_yslimit=Interface[(ys_min<= Interface["y"])]
xs_max=float(neck_x)
xs_min=float(amp_min_x)
Interface_xslimit=Interface_yslimit[(xs_min<= Interface_yslimit["x"]) & (Interface_yslimit["x"]<=xs_max)]
syloc=Interface_xslimit["y"].max()
#print(syloc)
pltspan=Interface_xslimit[Interface_xslimit["y"]==syloc]
#print(pltspan)
span_dat=pltspan.iloc[[-1]]
span_x=span_dat["x"]
#print(span_x)
span_y=span_dat["y"]
#print(span_y)
print("span",((span_y-1)*2)/2)


# Compute the stream

#Define the boundaries 
yst_max=float(span_y)
xst_max=float(neck_x)
yst_min=float(neck_y)
xst_min=float(span_x)


Interface_xstlimit=Interface[(float(xst_min)<= Interface["x"]) & (Interface["x"]<=float(xst_max))]
Interface_ystlimit=Interface_xstlimit[(float(yst_min)<= Interface_xstlimit["y"]) & (Interface_xstlimit["y"]<=float(yst_max))]
datst=Interface_ystlimit.sort_values(by=['y'])
yunist=datst["y"]
y_arrayst=yunist.unique()
y_lenst=len(y_arrayst)
y_st1=y_arrayst[0]
val1=Interface_ystlimit[(Interface_ystlimit["y"]==y_st1)]
stcheck1=val1["x"].min()

for st in range(1,y_lenst,1):
    yind=y_arrayst[st]
    st+=1
    stlimit=Interface_ystlimit[(Interface_ystlimit["y"]==yind)]
    stcheck=stlimit["x"].max()
    stxcheck=float(stcheck)
    if stcheck1>stxcheck:
        stcheck1=float(stcheck)
        stlim2=stlimit
    elif stxcheck>stcheck1:
        break
        
stlim2_last=stlim2.iloc[[-1]]
stlimx=float(stlim2_last["x"])
stlimy=float(stlim2_last["y"])


InterFaceStreamx=Interface[(xst_min<=Interface["x"]) &(Interface["x"]<=xst_max)]
InterFaceStreamy=InterFaceStreamx[(1.05<=InterFaceStreamx["y"]) &(InterFaceStreamx["y"]<=yst_max)]
sthigh=InterFaceStreamy["x"].max()
stream_dat=InterFaceStreamy[(InterFaceStreamy["x"]==float(sthigh))]
stream_xy=stream_dat.iloc[[-1]]
stream_x=float(stream_xy["x"])
stream_y=float(stream_xy["y"])
print("stream",(stream_x-amp_min_x)/2)


# plot the sorted Data
idata=Interface
ixdata = idata.sort_values(by=['y'])

yvalues = np.array(ixdata['y'])
xvalues = np.array(ixdata['x'])
plt.figure()
plt.plot(xvalues,yvalues,linestyle='',markersize=0.5,marker='*')
plt.scatter(amp_max_x,amp_max_y,c='purple')
plt.scatter(amp_min_x,amp_min_y,c='r')
plt.scatter(neck_x,neck_y,c='y')
plt.scatter(span_x,span_y,c='b')
plt.scatter(stream_x,stream_y,c='black')
##plt.scatter(stlimx,stlimy)
#plt.scatter(44.44,1.123,c="black")
plt.show()



    





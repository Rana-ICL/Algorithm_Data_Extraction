#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Created on Fri Jun 11 13:31:07 2021
Algorithm for extracting crucial information of Richtmyer-Meshkov Instabilites
e.g. amplitude, neck, stream, span
@author: Matar Fluid Group at Imperial College London 
         Developed within the PhD. project "Richtmyer-Meshkov Instabilities in Newtonian and non-Newtonian Flows"
         PhD. candidate Usman Rana Mohammad, Dr. Thomas Abadie, Prof. Omar Matar         
"""


# Data structuring part

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')


# Structre the data at the lowest y location
data = pd.read_csv("6.1e-5.txt") 

data.head()
#print(data.shape)
yuni=data["y"]
yshape=yuni.unique()
#print(yshape)
#print(yshape.shape)
deltalow=0
deltahigh=0
ygrid = 4.000e-06
deltay = 4.000e-06
a=data[data["y"]<1e-10]
a_sort=a.sort_values(by=['x'])
RMI_Inter=pd.DataFrame()
RMI_Inter=a_sort
alphaair = []
alphaair2d=[]
alphaair2d = np.zeros([501,5001])
xarray= np.zeros([501,5001])
yarray= np.zeros([501,5001])
alphaair2d[0,:] = np.array(a_sort["alpha.air"])

xarray[0,:] = np.array(a_sort["x"])
yarray[0,:] = np.array(a_sort["y"])



# Structure the data starting from the second lowest y location

for x in range(1,501,1):
    c=data[(data["y"]<ygrid+deltay/2.) & (data["y"]>ygrid-deltay/2.)] 
    csort=c.sort_values(by=['x'])
    alphaair=csort["alpha.air"]
    ygrid += deltay
    RMI_Inter=RMI_Inter.append(csort,ignore_index=True)
    
    # 2D array for visualization
    
    alphaair2d[x,:] = np.array(alphaair)
    xarray[x,:] = np.array(csort["x"]) 
    yarray[x,:] = np.array(csort["y"]) 

# Save the structed data to a .csv file
RMI_Inter.to_csv('structuredData.csv')



# Plot the Richtmyer-Meshkov Instabilities in a 2D contour plot
#pts = {{0.16835999999999998, 0.0291}};
#Epilog -> { PointSize[0.05], Green, Point[#] & /@ pts, Black, 
 #  Text["-1.6875", #] & /@ pts}]

plt.figure()
plt.contour(xarray, yarray, alphaair2d,linewidths=0.7,cmap='RdGy');
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.scatter(0.006972,0.001176,c='r')
plt.scatter(0.00678,0.001328,c='black')
plt.show()

# Post processing algorithm to find the size of RMI structures e.g. amplitude, neck, stream , span
# Algorithm type: brute force search



# Compute the amplitude

# Find the location of the interface and the coressponding x,y values in the array
Interface=RMI_Inter[(0.4<= RMI_Inter["alpha.air"]) & (RMI_Inter["alpha.air"]<=0.5)]
#print(Interface)
# Find the minimum and maximum x values with the Interface
x_loca_min=Interface["x"].min()
x_loca_max=Interface["x"].max()

# Compute the amplitude
amplitude=x_loca_max-x_loca_min
#print("check")
#print(amplitude)
#print("amplitude:",amplitude)





# Compute the neck

# Start from the highest y location
ygrid_neck = 0.002
center=0.001
deltay_neck =4.000e-06
# Start x value (with the highest y value, where alpha.air is between 0.1 and 0.9)
x_start_neck=0.007772

# The neck is located, where x starts decreasing! 
for x in range(1,501,1):
    neck_data=Interface[(Interface["y"]<ygrid_neck+deltay_neck/2.) & (Interface["y"]>ygrid_neck-deltay_neck/2.) &(Interface["y"]>center)]
    ygrid_neck -= deltay_neck
    xhit_neck=neck_data["x"].max()
    #print(neck_data)
    #print(neck_data["x"].max())
    #print(xhit_neck-x_start_neck)
    #print(neck_data[(neck_data["x"]==0.006972)])
    
    if abs(xhit_neck-x_start_neck)>0.0003:
        #print(neck_data[(neck_data["x"]==x_start_neck)])
        print(x_start_neck)
        break
    elif xhit_neck<x_start_neck or xhit_neck==x_start_neck:
        x_start_neck=xhit_neck
    
    
    
    
    #if abs(xhit_neck-x_start_neck)>0.009:
        #print(x_start_neck)
     #   break
    #elif xhit_neck<x_start_neck or xhit_neck==x_start_neck :
     #   x_start_neck=xhit_neck
     
        
        
        
        #break      
    #else:
     #   x_start_neck=xhit_neck
      #  print(xhit_neck,x_start_neck)
     #   x_start_neck=xhit_neck
      #  print(neck_data)
    #elif xhit_neck>x_start_neck:
     #   print("decreasing",x_start_neck)
      #  print("Neck Value:",neck_data)
       # break
   
    #if xhit_neck<x_start_neck or xhit_neck==x_start_neck:
     #   x_start_neck=xhit_neck
      #  print(neck_data)
    #elif xhit_neck>x_start_neck:
     #   print("decreasing",x_start_neck)
      #  print("Neck Value:",neck_data)
       # break
        
        
# Compute the span        
            
# Find the first x value in the y column, where alpha.air !=0   
ygrid_span = 0.001
deltay_span = 4.000e-06
x_start_span=0.006548
for x in range(1,501,1):
    span_data=Interface[(Interface["y"]<ygrid_span+deltay_span/2.) & (Interface["y"]>ygrid_span-deltay_span/2.)]
    ygrid_span += deltay_span
    #print(span_data)
    #print(span_data[(span_data["x"]==0.00678)])
    xhit_span=span_data["x"].min()
    if xhit_span-x_start_span>0.00008:
        #print(x_start_span)
        break
    elif xhit_span>x_start_span or xhit_span==x_start_span  :
        x_start_span=xhit_span
        #print(x_start_span)
        

    
    
    
# Compute the stream

# Find the first x value in the y column (start with the highest y value) with 0.2<alpha.air<0.8    
ygrid_stream = 0.03
deltay_stream = 6.000e-05
x_start_stream=0.15
x_check_val=0
x_check_2=0
y_valold=0
for x in range(1,501,1):
    stream_data=Interface[(Interface["y"]<ygrid_stream+deltay_stream/2.) & (Interface["y"]>ygrid_stream-deltay_stream/2.)]
    ygrid_stream -= deltay_stream
    
    # check for the second hit for the interface in the y column
    x_delta=stream_data["x"].max()-stream_data["x"].min()
    if x_delta>1e-3 and stream_data["y"].max()>0.02484:
        #print(stream_data)
        for y in range(0,(len(stream_data["x"])-1),1):
            #print(stream_data["x"].iloc[y])
            #print(stream_data["x"].iloc[y]-stream_data["x"].iloc[y+1])
            x_delta_n=(stream_data["x"].iloc[y]-stream_data["x"].iloc[y+1])
            n_abs=abs(x_delta_n)
            if n_abs>x_check_val:
                x_check_val=n_abs
                yloc=y
        x_holder=0
        if stream_data["x"].iloc[y]>stream_data["x"].iloc[x_holder]:
            x_holder=y
            #print(stream_data)
                  #  print(x_check_val,y,stream_data["x"].iloc[y])
                #if stream_data["x"].iloc[yloc]>= stream_data["x"].iloc[y_valold]:
                 #   y_valold=yloc
            
                  #  print(stream_data["x"].iloc[y_valold])
                    
            

    
    #if stream_data["x"].iloc[y_val]>stream_data["x"].iloc[y_valold]:
     #   y_valold=y_val
    #    print(y_val)

                    
            
    #if xsort[xsort["x"].iloc[-2]]>x_start_stream:
     #   x_start_stream=xsort[xsort["x"].iloc[-2]]
    #else:
     #   print(x_start_stream)
      #  break
    
    #print(xsort[xsort["x"].iloc[-2]])
        


# In[123]:


"""
Created on Fri Jun 11 13:31:07 2021
Algorithm for extracting crucial information of Richtmyer-Meshkov Instabilites
e.g. amplitude, neck, stream, span
@author: Matar Fluid Group at Imperial College London 
         Developed within the PhD. project "Richtmyer-Meshkov Instabilities in Newtonian and non-Newtonian Flows"
         PhD. candidate Usman Rana Mohammad, Dr. Thomas Abadie, Prof. Omar Matar         
"""


# Data structuring part

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')


# Structre the data at the lowest y location
data = pd.read_csv("0.txt") 

data.head()
#print(data.shape)
yuni=data["y"]
yshape=yuni.unique()
#print(yshape)
#print(yshape.shape)
deltalow=0
deltahigh=0
ygrid = 4.000e-06
deltay = 4.000e-06
a=data[data["y"]<1e-10]
a_sort=a.sort_values(by=['x'])
RMI_Inter=pd.DataFrame()
RMI_Inter=a_sort
alphaair = []
alphaair2d=[]
alphaair2d = np.zeros([501,5001])
xarray= np.zeros([501,5001])
yarray= np.zeros([501,5001])
alphaair2d[0,:] = np.array(a_sort["alpha.air"])

xarray[0,:] = np.array(a_sort["x"])
yarray[0,:] = np.array(a_sort["y"])



# Structure the data starting from the second lowest y location

for x in range(1,501,1):
    c=data[(data["y"]<ygrid+deltay/2.) & (data["y"]>ygrid-deltay/2.)] 
    csort=c.sort_values(by=['x'])
    alphaair=csort["alpha.air"]
    ygrid += deltay
    RMI_Inter=RMI_Inter.append(csort,ignore_index=True)
    
    # 2D array for visualization
    
    alphaair2d[x,:] = np.array(alphaair)
    xarray[x,:] = np.array(csort["x"]) 
    yarray[x,:] = np.array(csort["y"]) 

# Save the structed data to a .csv file
RMI_Inter.to_csv('structuredData.csv')



# Plot the Richtmyer-Meshkov Instabilities in a 2D contour plot
#pts = {{0.16835999999999998, 0.0291}};
#Epilog -> { PointSize[0.05], Green, Point[#] & /@ pts, Black, 
 #  Text["-1.6875", #] & /@ pts}]

plt.figure()
plt.contour(xarray, yarray, alphaair2d,linewidths=0.7,cmap='RdGy');
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.scatter(0.006972,0.001176,c='r')
plt.scatter(0.00102,0.001000,c='black')
plt.show()

# Post processing algorithm to find the size of RMI structures e.g. amplitude, neck, stream , span
# Algorithm type: brute force search



# Compute the amplitude

# Find the location of the interface and the coressponding x,y values in the array
Interface=RMI_Inter[(0.4<= RMI_Inter["alpha.air"]) & (RMI_Inter["alpha.air"]<=0.5)]
#print(Interface)
# Find the minimum and maximum x values with the Interface
x_loca_min=Interface["x"].min()
x_loca_max=Interface["x"].max()

# Compute the amplitude
amplitude=x_loca_max-x_loca_min
#print("check")

print(Interface[(Interface["x"]==x_loca_min)])
#print("amplitude:",amplitude)





# Compute the neck

# Start from the highest y location
ygrid_neck = 0.002
center=0.001
deltay_neck =4.000e-06
# Start x value (with the highest y value, where alpha.air is between 0.1 and 0.9)
x_start_neck=0.007772

# The neck is located, where x starts decreasing! 
for x in range(1,501,1):
    neck_data=Interface[(Interface["y"]<ygrid_neck+deltay_neck/2.) & (Interface["y"]>ygrid_neck-deltay_neck/2.) &(Interface["y"]>center)]
    ygrid_neck -= deltay_neck
    xhit_neck=neck_data["x"].max()
    #print(neck_data)
    #print(neck_data["x"].max())
    #print(xhit_neck-x_start_neck)
    #print(neck_data[(neck_data["x"]==0.006972)])
    
    if abs(xhit_neck-x_start_neck)>0.0003:
        #print(neck_data[(neck_data["x"]==x_start_neck)])
        print(x_start_neck)
        break
    elif xhit_neck<x_start_neck or xhit_neck==x_start_neck:
        x_start_neck=xhit_neck
    
    
    
    
    #if abs(xhit_neck-x_start_neck)>0.009:
        #print(x_start_neck)
     #   break
    #elif xhit_neck<x_start_neck or xhit_neck==x_start_neck :
     #   x_start_neck=xhit_neck
     
        
        
        
        #break      
    #else:
     #   x_start_neck=xhit_neck
      #  print(xhit_neck,x_start_neck)
     #   x_start_neck=xhit_neck
      #  print(neck_data)
    #elif xhit_neck>x_start_neck:
     #   print("decreasing",x_start_neck)
      #  print("Neck Value:",neck_data)
       # break
   
    #if xhit_neck<x_start_neck or xhit_neck==x_start_neck:
     #   x_start_neck=xhit_neck
      #  print(neck_data)
    #elif xhit_neck>x_start_neck:
     #   print("decreasing",x_start_neck)
      #  print("Neck Value:",neck_data)
       # break
        
        
# Compute the span        
            
# Find the first x value in the y column, where alpha.air !=0   
ygrid_span = 0.001
deltay_span = 4.000e-06
x_start_span=0.006548
for x in range(1,501,1):
    span_data=Interface[(Interface["y"]<ygrid_span+deltay_span/2.) & (Interface["y"]>ygrid_span-deltay_span/2.)]
    ygrid_span += deltay_span
    #print(span_data)
    #print(span_data[(span_data["x"]==0.00678)])
    xhit_span=span_data["x"].min()
    if xhit_span-x_start_span>0.00008:
        #print(x_start_span)
        break
    elif xhit_span>x_start_span or xhit_span==x_start_span  :
        x_start_span=xhit_span
        #print(x_start_span)
        

    
    
    
# Compute the stream

# Find the first x value in the y column (start with the highest y value) with 0.2<alpha.air<0.8    
ygrid_stream = 0.03
deltay_stream = 6.000e-05
x_start_stream=0.15
x_check_val=0
x_check_2=0
y_valold=0
for x in range(1,501,1):
    stream_data=Interface[(Interface["y"]<ygrid_stream+deltay_stream/2.) & (Interface["y"]>ygrid_stream-deltay_stream/2.)]
    ygrid_stream -= deltay_stream
    
    # check for the second hit for the interface in the y column
    x_delta=stream_data["x"].max()-stream_data["x"].min()
    if x_delta>1e-3 and stream_data["y"].max()>0.02484:
        #print(stream_data)
        for y in range(0,(len(stream_data["x"])-1),1):
            #print(stream_data["x"].iloc[y])
            #print(stream_data["x"].iloc[y]-stream_data["x"].iloc[y+1])
            x_delta_n=(stream_data["x"].iloc[y]-stream_data["x"].iloc[y+1])
            n_abs=abs(x_delta_n)
            if n_abs>x_check_val:
                x_check_val=n_abs
                yloc=y
        x_holder=0
        if stream_data["x"].iloc[y]>stream_data["x"].iloc[x_holder]:
            x_holder=y
            #print(stream_data)
                  #  print(x_check_val,y,stream_data["x"].iloc[y])
                #if stream_data["x"].iloc[yloc]>= stream_data["x"].iloc[y_valold]:
                 #   y_valold=yloc
            
                  #  print(stream_data["x"].iloc[y_valold])
                    
            

    
    #if stream_data["x"].iloc[y_val]>stream_data["x"].iloc[y_valold]:
     #   y_valold=y_val
    #    print(y_val)

                    
            
    #if xsort[xsort["x"].iloc[-2]]>x_start_stream:
     #   x_start_stream=xsort[xsort["x"].iloc[-2]]
    #else:
     #   print(x_start_stream)
      #  break
    
    #print(xsort[xsort["x"].iloc[-2]])


# In[113]:


((((0.001328-0.001)))*2)/2e-3


# In[3]:


span_tm43=[0.268,0.39199999999999996,0.4959999999999999,0.528,0.536]
neck_tm43=[0.22400000000000003,0.12800000000000009,0.07200000000000001,0.05600000000000006,0.05199999999999996]
t_tm43=[(4.3e-5/4.3e-5),(8.4e-5/4.3e-5),(0.0001285/4.3e-5),(0.0001475/4.3e-5),(0.000155/4.3e-5)]


# In[4]:


span_tm31=[0.265,0.32799999999999996,0.4159999999999999,0.44800000000000006,0.48400000000000004,0.528,0.536]
neck_tm31=[0.265,0.17599999999999993,0.11599999999999999,0.10000000000000005,0.0759999999999999,0.05600000000000006,0.05199999999999996]
t_tm31=[(3.1e-5/3.1e-5),(6.1e-5/3.1e-5),(9.3e-5/3.1e-5),(0.000104/3.1e-5),(0.000122/3.1e-5),(0.0001475/3.1e-5),(0.000155/3.1e-5)]


# In[81]:


span_tm31


# In[33]:


((0.0020240000000000015/2)-(0.00012399999999999998/2))*((2*3.14)/2e-3)


# In[34]:


#tm=3.1e-5


# In[35]:


#t=[2.5e-6/tm]
#amp=[0.037680000000000234]
#del amp[-1]
#del t[-1]


# In[98]:


#amp.append(2.9830000000000023)


# In[ ]:


t.append((0.0001505/tm))


# In[ ]:


print(amp,t)


# In[ ]:


print(len(amp),len(t))


# In[ ]:


(0.000155/3.1e-5)


# In[ ]:


plt.plot(t,amp)


# In[ ]:


index = amp.index(0.0008160000000000008)


# In[ ]:


print(index)


# In[6]:


experidata=pd.read_csv("neckData.csv") 


# In[7]:


exptime=experidata["t"]
expamp=experidata["n"]


# In[ ]:


print(exptime*3.1e-5)


# In[9]:


plt.plot(t_tm31, neck_tm31, 'r',label ="simulation") # plotting t, a separately 
#plt.plot(t_tm43, neck_tm43, 'black',label ="simulation with tm_{4.3e-5}")
plt.scatter(exptime,expamp,c='black',label ="experiment")
plt.plot(t_tm43, neck_tm43, 'black',label ="simulation") # plotting t, a separately 
plt.xlabel("t/tm [-]",size=13)
plt.ylabel(" W$_{neck}$/$\lambda$ [-]",size=13)
plt.title("RMI Neck",size=14)
plt.grid()
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#plt.savefig('RMIAmpliGrowth1.png')
plt.show()
#plt.savefig('RMIAmpliGrowth.png')


# In[ ]:


0.000113/3.1e-5


# In[ ]:


print()


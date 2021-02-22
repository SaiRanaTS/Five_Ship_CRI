import math
import numpy
from fractions import Fraction
import numpy as np
from matplotlib import pyplot as plt
import sys
# sys.path.append('../scripts/')
from pylab import *
import CRI_FunExe
import CRI_Functions

import Plot_Chart


# This is the V.1.2 of the CRI Risk Model for Ship by Sai
# This Execution contains two modules: CRI_FunExe and CRI_Functions


###################################################################################################
# :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:Ship Define:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
###################################################################################################
class Ship_Data:
    number_of_ships = 0

    def __init__(self, Xpos, Ypos, v, ang, l):
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.v = v
        self.ang = ang
        self.l = l
        Ship_Data.number_of_ships += 1

''
###################################################################################################
print('Welcome to V.1.3 of the CRI Risk Model for Ship by Sai ')
print('This is a simple Multi Ship model for initial assessment and evaluation')
print('For this model we need to have 1. X position of Ship, 2. Y position of Ship, 3. Velocity of Ship, 4. Direction Angle of the Ship and 4. Length of the Ship')
print(
    '###############################################################################################################################################################')

osx = 1
osy = 2
osv = 10
osa = 60
osl = 100


t1sx = 3
t1sy = 2
t1sv = 12
t1sa = 3
t1sl = 100

t2sx = 10
t2sy = 3
t2sv = 10
t2sa = 320
t2sl = 100


t3sx = 8
t3sy = 5
t3sv = 10
t3sa = 290
t3sl = 100

t4sx = 6
t4sy = 3
t4sv = 10
t4sa = 140
t4sl = 100

t5sx = 2
t5sy = 3
t5sv = 15
t5sa = 90
t5sl = 100
# print('The number of Target Ships are : ', S_No) # Mutli Ship Under construction

###################################################################################################


#Own_Ship = Ship_Data(osx, osy, osv, osa, osl)
#Trg1_Ship = Ship_Data(t1sx, t1sy, t1sv, t1sa, t1sl)
#Trg2_Ship = Ship_Data(t2sx, t2sy, t2sv, t2sa, t2sl)

###################################################################################################

#chart = Plot_Chart.Plot(Own_Ship.Xpos, Own_Ship.Ypos, Trg1_Ship.Xpos,Trg2_Ship.Xpos, Trg1_Ship.Ypos,Trg2_Ship.Ypos,Own_Ship.ang, Trg1_Ship.ang,Trg2_Ship.ang)
#chart.show()
###################################################################################################
###################################################################################################
#Location Append
###################################################################################################

osxl=[]
osyl=[]
t1sxl=[]
t1syl=[]

t2sxl=[]
t2syl=[]

t3sxl=[]
t3syl=[]


t4sxl=[]
t4syl=[]


t5sxl=[]
t5syl=[]

###################################################################################################
#########################################################################################
#-------------------------------------Trajectory----------------------------------------#
#########################################################################################

steps = 5

t = 0.2

tstp=[0.0,0.2,0.4,0.6,0.8]

for i in range(steps):
    osx = round(osx + (osv*t*(math.cos(math.radians(osa)))),2)
    osy = round(osy + (osv*t*(math.sin(math.radians(osa)))),2)

    t1sx = round(t1sx + (t1sv*t*(math.sin(math.radians(t1sa)))),2)
    t1sy = round(t1sy + (t1sv*t*(math.cos(math.radians(t1sa)))),2)

    t2sx = round(t2sx + (t2sv*t*(math.sin(math.radians(t2sa)))),2)
    t2sy = round(t2sy + (t2sv*t*(math.cos(math.radians(t2sa)))),2)

    t3sx = round(t3sx + (t3sv*t*(math.sin(math.radians(t3sa)))),2)
    t3sy = round(t3sy + (t3sv*t*(math.cos(math.radians(t3sa)))),2)

    t4sx = round(t4sx + (t4sv*t*(math.sin(math.radians(t4sa)))),2)
    t4sy = round(t4sy + (t4sv*t*(math.cos(math.radians(t4sa)))),2)

    t5sx = round(t5sx + (t5sv*t*(math.sin(math.radians(t5sa)))),2)
    t5sy = round(t5sy + (t5sv*t*(math.cos(math.radians(t5sa)))),2)

    osxl.append(osx)
    osyl.append(osy)

    t1sxl.append(t1sx)
    t1syl.append(t1sy)

    t2sxl.append(t2sx)
    t2syl.append(t2sy)

    t3sxl.append(t3sx)
    t3syl.append(t3sy)

    t4sxl.append(t4sx)
    t4syl.append(t4sy)

    t5sxl.append(t5sx)
    t5syl.append(t5sy)

print(osxl)
print(osyl)

sine_dego = math.sin(math.radians(65))
cos_dego = math.cos(math.radians(65))
z0 = 11 * sine_dego
p0 = 11 * cos_dego

sine_degt1 = math.sin(math.radians(t1sa))
cos_degt1 = math.cos(math.radians(t1sa))
z1 = 10 * sine_degt1
p1 = 10 * cos_degt1

sine_degt2 = math.sin(math.radians(t2sa))
cos_degt2 = math.cos(math.radians(t2sa))
z2 = 10 * sine_degt2
p2 = 10 * cos_degt2

sine_degt3 = math.sin(math.radians(t3sa))
cos_degt3 = math.cos(math.radians(t3sa))
z3 = 10 * sine_degt3
p3 = 10 * cos_degt3

sine_degt4 = math.sin(math.radians(t4sa))
cos_degt4 = math.cos(math.radians(t4sa))
z4 = 10 * sine_degt4
p4 = 10 * cos_degt4


sine_degt5 = math.sin(math.radians(t5sa))
cos_degt5 = math.cos(math.radians(t5sa))
z5 = 10 * sine_degt5
p5 = 10 * cos_degt5


# Q=plt.quiver(osxl, osyl, z0, p0, color = 'blue', pivot = 'middle')
# plt.quiverkey(Q,0.75,1.06,1, "Own Ship",labelpos="E")
# plt.plot(osxl,osyl, linestyle='dashed', color = 'blue',label='OS Path' )
# for i in range(steps):
#     dta1 = "OS: P"+ str(i+1)
#     plt.text((osxl[i]+0.5), osyl[i],dta1)


X=plt.quiver(osxl, osyl , z0, p0, color = 'blue', pivot = 'middle')
plt.quiverkey(X,0.75,1.06,1, "Own Ship",labelpos="E")
plt.plot(osxl,osyl, linestyle='dashed',label='OS Path')
for i in range(steps):
    dta2 = "OS: P"+ str(i+1)
    plt.text((osxl[i]+0.5), osyl[i],dta2)




#
# P=plt.quiver(t1sxl, t1syl , z1, p1, color = 'red', pivot = 'middle')
# plt.quiverkey(P,0.75,1.06,1, "Target ship",labelpos="E")
# plt.plot(t1sxl,t1syl, linestyle='dashed',label='TS1 Path')
# for i in range(steps):
#     dta2 = "TS1: P"+ str(i+1)
#     plt.text((t1sxl[i]+0.5), t1syl[i],dta2)


# R=plt.quiver(t2sxl, t2syl , z2, p2, color = 'red', pivot = 'middle')
# plt.quiverkey(R,0.75,1.06,1, "Target ship",labelpos="E")
# plt.plot(t2sxl,t2syl, linestyle='dashed',label='TS2 Path')
# for i in range(steps):
#     dta3 = "TS2: P"+ str(i+1)
#     plt.text((t2sxl[i]+0.5), t2syl[i],dta3)


#

# S=plt.quiver(t3sxl, t3syl , z3, p3, color = 'red', pivot = 'middle')
# plt.quiverkey(S,0.75,1.06,1, "Target ship",labelpos="E")
# plt.plot(t3sxl,t3syl, linestyle='dashed',label='TS3 Path')
# for i in range(steps):
#     dta4 = "TS3: P"+ str(i+1)
#     plt.text((t3sxl[i]+0.5), t3syl[i],dta4)
#
#
# T=plt.quiver(t4sxl, t4syl , z4, p4, color = 'red', pivot = 'middle')
# plt.quiverkey(T,0.75,1.06,1, "Target ship",labelpos="E")
# plt.plot(t4sxl,t4syl, linestyle='dashed',label='TS4 Path')
# for i in range(steps):
#     dta5 = "TS4: P"+ str(i+1)
#     plt.text((t4sxl[i]+0.5), t4syl[i],dta5)

#
U=plt.quiver(t5sxl, t5syl , z5, p5, color = 'red', pivot = 'middle')
plt.quiverkey(U,0.75,1.06,1, "Target ship",labelpos="E")
plt.plot(t5sxl,t5syl, linestyle='dashed',label='TS5 Path')
for i in range(steps):
    dta6 = "TS5: P"+ str(i+1)
    plt.text((t5sxl[i]+0.5), t5syl[i],dta6)

plt.title("The Ship Position Plot")
plt.ylabel("The Distance in Y Direction (NM)")
plt.xlabel("The Distance in X Direction (NM)")

plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.grid()
plt.show()

#
# ###################################################################################################
# #:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-: CRI Target Ship 1 - Execution Call :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
# ###################################################################################################
#
# print('Own Ship Pos:')
# print("X pos : ",osxl)
# print("Y pos : ",osyl)
#
# print('------------------------------')
#
# print('Target Ship 1  Pos:')
# print("X pos : ",t1sxl)
# print("Y pos : ",t1syl)
#
# print('-------------------------------')
#
# print('Target Ship 2  Pos:')
# print("X pos : ",t2sxl)
# print("Y pos : ",t2syl)
#
# print('-------------------------------')
#
# print('Target Ship 3  Pos:')
# print("X pos : ",t3sxl)
# print("Y pos : ",t3syl)
#
# print('-------------------------------')
#
# print('Target Ship 4  Pos:')
# print("X pos : ",t4sxl)
# print("Y pos : ",t4syl)
#
# print('-------------------------------')
#
# print('Target Ship 5  Pos:')
# print("X pos : ",t5sxl)
# print("Y pos : ",t5syl)
#
# print('-------------------------------')
#
# print('######################################################################')
# print('######################################################################')
# print('*******************The CRI Index wrt Target Ship 1 *******************')
#
# tr1cri=[]
#
# for i in range(5):
#     CRI_1=CRI_FunExe.CRI_call(osv, t1sv, osxl[i], osyl[i], t1sxl[i], t1syl[i], osa, t1sa)
#     tr1cri.append(CRI_1)
#
# print('CRI index for Target Ship 1 : ', tr1cri)
#
# plt.title("CRI index vs Time Plot for Own Ship wrt Target Ship 1")
# plt.plot(tstp,tr1cri)
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.show()
#
#
# print('----------------------------------------------------------------------')
#
# print('######################################################################')
# print('######################################################################')
# print('*******************The CRI Index wrt Target Ship 2 *******************')
#
# tr2cri=[]
#
# for i in range(5):
#     CRI_2=CRI_FunExe.CRI_call(osv, t2sv, osxl[i], osyl[i], t2sxl[i], t2syl[i], osa, t2sa)
#     tr2cri.append(CRI_2)
#
# print('CRI index for Target Ship 2 : ', tr2cri)
# plt.title("CRI index vs Time Plot for Own Ship wrt Target Ship 2")
# plt.plot(tstp,tr2cri)
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.show()
#
#
# print('----------------------------------------------------------------------')
#
# print('######################################################################')
# print('######################################################################')
# print('*******************The CRI Index wrt Target Ship 3 *******************')
#
# tr3cri=[]
#
# for i in range(5):
#     CRI_3=CRI_FunExe.CRI_call(osv, t3sv, osxl[i], osyl[i], t3sxl[i], t3syl[i], osa, t3sa)
#     tr3cri.append(CRI_3)
#
# print('CRI index for Target Ship 3 : ', tr3cri)
# plt.title("CRI index vs Time Plot for Own Ship wrt Target Ship 3")
# plt.plot(tstp,tr3cri)
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.show()
#
#
# print('----------------------------------------------------------------------')
#
# print('######################################################################')
# print('######################################################################')
# print('*******************The CRI Index wrt Target Ship 4 *******************')
#
# tr4cri=[]
#
# for i in range(5):
#     CRI_4=CRI_FunExe.CRI_call(osv, t4sv, osxl[i], osyl[i], t4sxl[i], t4syl[i], osa, t4sa)
#     tr4cri.append(CRI_4)
#
# print('CRI index for Target Ship 4 : ', tr4cri)
# plt.title("CRI index vs Time Plot for Own Ship wrt Target Ship 4")
# plt.plot(tstp,tr4cri)
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.show()
#
#
# print('----------------------------------------------------------------------')
#
# print('######################################################################')
# print('######################################################################')
# print('*******************The CRI Index wrt Target Ship 5 *******************')
#
# tr5cri=[]
#
# for i in range(5):
#     CRI_5=CRI_FunExe.CRI_call(osv, t5sv, osxl[i], osyl[i], t5sxl[i], t5syl[i], osa, t5sa)
#     tr5cri.append(CRI_5)
#
# print('CRI index for Target Ship 5 : ', tr5cri)
# plt.title("CRI index vs Time Plot for Own Ship wrt Target Ship 5")
# plt.plot(tstp,tr5cri)
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.show()
#
#
# print('----------------------------------------------------------------------')
#
# print('----------------------------------------------------------------------')
#
#
# plt.title("CRI index vs Time Plot for Own Ship wrt all Target Ships")
#
# plt.plot(tstp,tr1cri,label='TS1 CRI')
# plt.plot(tstp,tr2cri,label='TS2 CRI')
# plt.plot(tstp,tr3cri,label='TS3 CRI')
# plt.plot(tstp,tr4cri,label='TS4 CRI')
# plt.plot(tstp,tr5cri,label='TS5 CRI')
# plt.xlabel('Time (hr)')
# plt.ylabel('CRI')
# plt.legend(bbox_to_anchor=(1.1, 1.05))
# plt.grid()
# plt.show()

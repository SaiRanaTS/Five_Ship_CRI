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


###################################################################################################
print('Welcome to V.1.3 of the CRI Risk Model for Ship by Sai ')
print('This is a simple Multi Ship model for initial assessment and evaluation')
print('For this model we need to have 1. X position of Ship, 2. Y position of Ship, 3. Velocity of Ship, 4. Direction Angle of the Ship and 4. Length of the Ship')
print(
    '###############################################################################################################################################################')
osx = float(input('Enter the X Coordinate of Own Ship : '))
osy = float(input('Enter the Y Coordinate of Own Ship : '))
osv = float(input('Enter the Speed of Own Ship (Knots): '))
osa = float(input('Enter the angle of Own Ship (Deg)  : '))
osl = float(input('Enter the length of Own Ship (Mtr) : '))

print('\nEnter the details for Target Ship 1\n')
print('---------------------------------------------')

t1sx = float(input('Enter the X Coordinate of Target Ship : '))
t1sy = float(input('Enter the Y Coordinate of Target Ship : '))
t1sv = float(input('Enter the Speed of Target Ship (Knots): '))
t1sa = float(input('Enter the angle of Target Ship (Deg)  : '))
t1sl = float(input('Enter the length of Target Ship (Mtr) : '))

print('\nEnter the details for Target Ship 2\n')
print('---------------------------------------------')

t2sx = float(input('Enter the X Coordinate of Target Ship : '))
t2sy = float(input('Enter the Y Coordinate of Target Ship : '))
t2sv = float(input('Enter the Speed of Target Ship (Knots): '))
t2sa = float(input('Enter the angle of Target Ship (Deg)  : '))
t2sl = float(input('Enter the length of Target Ship (Mtr) : '))

# print('The number of Target Ships are : ', S_No) # Mutli Ship Under construction


###################################################################################################


Own_Ship = Ship_Data(osx, osy, osv, osa, osl)
Trg1_Ship = Ship_Data(t1sx, t1sy, t1sv, t1sa, t1sl)
Trg2_Ship = Ship_Data(t2sx, t2sy, t2sv, t2sa, t2sl)

###################################################################################################

chart = Plot_Chart.Plot(Own_Ship.Xpos, Own_Ship.Ypos, Trg1_Ship.Xpos,Trg2_Ship.Xpos, Trg1_Ship.Ypos,Trg2_Ship.Ypos,Own_Ship.ang, Trg1_Ship.ang,Trg2_Ship.ang)
chart.show()

###################################################################################################
#:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-: CRI Target Ship 1 - Execution Call :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
###################################################################################################

CRI1 = CRI_FunExe.CRI_call(Own_Ship.v, Trg1_Ship.v, Own_Ship.Xpos, Own_Ship.Ypos, Trg1_Ship.Xpos, Trg1_Ship.Ypos,
                          Own_Ship.ang, Trg1_Ship.ang)
print('######################################################################')
print('######################################################################')
print('*******************The CRI Index wrt Target Ship 1 *******************')

print('CRI index for Target Ship 1 : ', CRI1)

print('----------------------------------------------------------------------')

###################################################################################################
#:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-: CRI Target Ship 2 - Execution Call :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
###################################################################################################

CRI2 = CRI_FunExe.CRI_call(Own_Ship.v, Trg2_Ship.v, Own_Ship.Xpos, Own_Ship.Ypos, Trg2_Ship.Xpos, Trg2_Ship.Ypos,
                          Own_Ship.ang, Trg2_Ship.ang)
print('######################################################################')
print('######################################################################')
print('*******************The CRI Index wrt Target Ship 2 *******************')

print('CRI index for Target Ship 2 : ', CRI2)

print('----------------------------------------------------------------------')

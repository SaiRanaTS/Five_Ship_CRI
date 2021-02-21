#Plot Pos of the Ships
import math
from pylab import *
from matplotlib import pyplot as plt

def Plot(Own_Ship_Xpos,Own_Ship_Ypos,Trg1_Ship_Xpos,Trg2_Ship_Xpos,Trg1_Ship_Ypos,Trg2_Ship_Ypos,Own_Ship_ang,Trg1_Ship_ang,Trg2_Ship_ang):
    own_posDx = Own_Ship_Xpos #
    own_posDy = Own_Ship_Ypos #
    Own_DircX = 0
    Own_DircY = 90


    Tar1_posDx = Trg1_Ship_Xpos #
    Tar1_posDy = Trg1_Ship_Ypos #
    Tar1_DircX = 0
    Tar1_dircY = 120


    Tar2_posDx = Trg2_Ship_Xpos #
    Tar2_posDy = Trg2_Ship_Ypos #
    Tar2_DircX = 0
    Tar2_dircY = 20


    ang1 = int(Own_Ship_ang)
    ang2 = int(Trg1_Ship_ang)
    ang3 = int(Trg2_Ship_ang)

    xmin = -150
    xmax = 150
    ymin = -150
    ymax = 150

    sine_dego = math.sin(math.radians(ang1))
    cos_dego = math.cos(math.radians(ang1))
    u = 10 * sine_dego
    v = 10 * cos_dego

    sine_degt = math.sin(math.radians(ang2))
    cos_degt = math.cos(math.radians(ang2))
    z1 = 10 * sine_degt
    p1 = 10 * cos_degt

    sine_degt = math.sin(math.radians(ang3))
    cos_degt = math.cos(math.radians(ang3))
    z2 = 10 * sine_degt
    p2 = 10 * cos_degt

    plt.axis('equal')

    Q=plt.quiver(own_posDx, own_posDy, u, v, color = 'blue', pivot = 'middle')
    plt.quiverkey(Q,0.75,1.02,1, "Own Ship",labelpos="E")
    plt.text(own_posDx, own_posDy, "Own Ship")



    P=plt.quiver(Tar1_posDx, Tar1_posDy , z1, p1, color = 'red', pivot = 'middle')
    plt.quiverkey(P,0.75,1.06,1, "Target ship",labelpos="E")
    plt.text(Tar1_posDx, Tar1_posDy, "Target Ship 1")

    R=plt.quiver(Tar2_posDx, Tar2_posDy , z2, p2, color = 'red', pivot = 'middle')
    plt.text(Tar2_posDx, Tar2_posDy, "Target Ship 2")

    plt.title("Ship Positions")
    plt.show()

    return plt
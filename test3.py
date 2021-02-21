import math
from matplotlib import pyplot as plt



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

t2sx = 4
t2sy = 1
t2sv = 10
t2sa = 120
t2sl = 100


t3sx = 5
t3sy = 2
t3sv = 10
t3sa = 100
t3sl = 100

t4sx = 5
t4sy = 2
t4sv = 10
t4sa = 140
t4sl = 100

t5sx = 3
t5sy = 1
t5sv = 10
t5sa = 60
t5sl = 100


#########################################################################################
#-------------------------------------Trajectory----------------------------------------#
#########################################################################################

steps = 5

t = 0.2

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

sine_dego = math.sin(math.radians(osa))
cos_dego = math.cos(math.radians(osa))
u = 10 * sine_dego
v = 10 * cos_dego

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


Q=plt.quiver(osxl, osyl, u, v, color = 'blue', pivot = 'middle')
plt.quiverkey(Q,0.75,1.02,1, "Own Ship",labelpos="E")
plt.plot(osxl,osyl, linestyle='dashed', color = 'blue',label='OS Path' )
n = [1,2,3,4,5]
for i in range(steps):
    dta1 = "OS: P"+ str(i+1)
    plt.text((osxl[i]+0.5), osyl[i],dta1)



P=plt.quiver(t1sxl, t1syl , z1, p1, color = 'red', pivot = 'middle')
plt.quiverkey(P,0.75,1.06,1, "Target ship",labelpos="E")
plt.plot(t1sxl,t1syl, linestyle='dashed',label='TS1 Path')
for i in range(steps):
    dta2 = "TS1: P"+ str(i+1)
    plt.text((t1sxl[i]+0.5), t1syl[i],dta2)


R=plt.quiver(t2sxl, t2syl , z2, p2, color = 'red', pivot = 'middle')
plt.quiverkey(R,0.75,1.06,1, "Target ship",labelpos="E")
plt.plot(t2sxl,t2syl, linestyle='dashed',label='TS2 Path')
for i in range(steps):
    dta3 = "TS2: P"+ str(i+1)
    plt.text((t2sxl[i]+0.5), t2syl[i],dta3)




S=plt.quiver(t3sxl, t3syl , z3, p3, color = 'red', pivot = 'middle')
plt.quiverkey(S,0.75,1.06,1, "Target ship",labelpos="E")
plt.plot(t3sxl,t3syl, linestyle='dashed',label='TS3 Path')
for i in range(steps):
    dta4 = "TS3: P"+ str(i+1)
    plt.text((t3sxl[i]+0.5), t3syl[i],dta4)


T=plt.quiver(t4sxl, t4syl , z4, p4, color = 'red', pivot = 'middle')
plt.quiverkey(T,0.75,1.06,1, "Target ship",labelpos="E")
plt.plot(t4sxl,t4syl, linestyle='dashed',label='TS4 Path')
for i in range(steps):
    dta5 = "TS4: P"+ str(i+1)
    plt.text((t4sxl[i]+0.5), t4syl[i],dta5)


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











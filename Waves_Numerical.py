import numpy as np
import matplotlib.pyplot as plt
import math
zs=1000
z0=-500
from funcs import *
#Question 1:
zs=1000

# n=0
# for th in np.linspace(0.53,0.75,20):
#     #if not abs(math.tan(phi*math.pi/180))>10**6:
#         rho, xn, yn, zn = rays3d(th, 0, zs, n)
#         ax.plot(xn,yn,zn)
#         alpha=(180/math.pi)*math.atan( (xn[len(xn)-1]-xn[len(xn)-2])/(zn[len(zn)-1]-zn[len(zn)-2]) )+th
#         analiticalalpha=180/math.pi*(2/(zs*math.sin(th/(180/math.pi))))
#         print('theta: ' , th ,'alpha: ', alpha , 'error: ' ,(abs(analiticalalpha-alpha)*100/alpha))
#         n = n + 1
# plt.show()



#Question 2:

# zs=1000
#
# n=0
# for th in np.linspace(1,2,10):
#     for phi in range(0,360,15):
#         if not abs(math.tan(phi*math.pi/180))>10**6:
#             rho, xn, yn, zn = rays3d(th, phi, zs, n)
#             ax.plot(xn,yn,zn)
#             n = n + 1
# plt.show()






#Qustion 3
#
# zs=1000
#
# distances=[]
# n=0
# for th in np.linspace(1,2.2,70):
#     for phi in range(0,360,3):
#
#         if not abs(math.tan(phi*math.pi/180))>10**6:
#             rho,xn, yn, zn = rays3d(th, phi, zs, n,2)
#             # if the distance from the watchman (when the distance from z axis is minimal) smaller than 1,
#             for i in range(0,700):
#                 rho[i]=100
#             distances.append(zn[rho.index(min(rho))]-z0)
#             if zn[rho.index(min(rho))]<z0+1 and zn[rho.index(min(rho))]>z0-1:
#                 print("haha")
#                 #plot this ray
#                 plt.plot(xn,zn)
#             print(min(distances))
#             n=n+1
# plt.show()






 #Question 4

# z0=-600
# zs=1000
# distances=[]
# n=0
# rhos=[]
# x = []
# y = []
# for th in np.linspace(0.8,2.2,20):
#     for phi in range(0,360,5):
#         if not abs(math.tan(phi*math.pi/180))>10**6:
#             rho,xn, yn, zn = rays3d(th, phi, zs, n,2)
#             # if the distance from the watchman (when the distance from z axis is minimal) smaller than 1,
#             for i in range(0,700):
#                 rho[i]=100
#             distances.append(zn[rho.index(min(rho))]-z0)
#
#             if zn[rho.index(min(rho))]<z0+1 and zn[rho.index(min(rho))]>z0-1:
#                 #plot this ray
#                 print(min(distances))
#                 abs_z=[abs(i) for i in zn]
#                 x.append(xn[abs_z.index(min(abs_z))])
#                 y.append(yn[abs_z.index(min(abs_z))])
#                 rhos.append(min(rho))
#                 plt.scatter(x,y)
#             n=n+1
# print("the average radius is: " , sum(rhos)/len(rhos))
# plt.show()





#two masses:

#
# #1
# zs=1000
# z0=-1300
# n=0
# for th in np.linspace(2,4,4):
#     for phi in range(0,360,45):
#         if not abs(math.tan(phi*math.pi/180))>10**6: #if it's not diverging
#             rho, xn, yn, zn = rays3d(th, phi, zs, n,3,2)
#             ax.plot(xn,yn,zn)
#             n = n + 1
# plt.show()
#


#
#2
zs=1000
z0=-1300
distances=[]
n=0
rhos=[]
xsd=[]
ysd=[]
for th in np.linspace(1.7,2.04,300):
    for phi in range(0,360,45):
        if not abs(math.tan(phi*math.pi/180))>10**6:
            rho,xn, yn, zn = rays3d(th, phi, zs, n,2,2)
            # if the distance from the watchman (when the distance from z axis is minimal) smaller than 1,
            for i in range(0,700):
                rho[i]=10**6
            distances.append(zn[rho.index(min(rho))]-z0)
            print(min(distances))
            if min(distances)<-10:
                break
            if zn[rho.index(min(rho))]<z0+10 and zn[rho.index(min(rho))]>z0-10:
                #plot this ray

                abs_z=[abs(i) for i in zn]
                xsd.append(xn[abs_z.index(min(abs_z))])
                ysd.append(yn[abs_z.index(min(abs_z))])
                rhos.append(min(rho))

            n=n+1


print("x: " , xsd)
print("y: ", ysd)


plt.scatter(xsd,ysd)
print("the average radius is: " , sum(rhos)/len(rhos))
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import math


fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

def rays3d(th,phi,zs,n,d=3,m=1):
    global fig
    global ax
    import numpy as np
    import matplotlib.pyplot as plt
    import math


    pox2=[]
    poy2=[]
    poz2=[]
    rhos=[]

    z=zs
    x=0
    y=0

    s=0
    th=th*math.pi/180
    phi=phi*math.pi/180
    dr=0.01
    dz=-dr*math.cos(th)
    dx=dr*math.sin(th)*math.cos(phi)
    dy=dr*math.sin(th)*math.sin(phi)

    if m==2:
        while s < 3000:
            ds = (dx ** 2 + dy ** 2 + dz ** 2) ** (1 / 2)
            r = (x** 2 + y ** 2 + z ** 2) ** (1 / 2)
            r_1 = ((x-20) ** 2 + y ** 2 + z ** 2) ** (1 / 2)
            r_2 = ((x + 20) ** 2 + y ** 2 + z ** 2) ** (1 / 2)
            rplusdr = ((x + dx) ** 2 + (y + dy) ** 2 + (z + dz) ** 2) ** (1 / 2)
            nr = 1 + 1/r_1 + 1/r_2

            dx = (ds ** 2) * (1 / nr) * (-x / (r ** 3) + (1 / (r ** 2) * (rplusdr - r) / ds) * dx / ds) + dx
            dz = (ds ** 2) * (1 / nr) * (-z / (r ** 3) + (1 / (r ** 2) * (rplusdr - r) / ds) * dz / ds) + dz
            dy = (ds ** 2) * (1 / nr) * (-y / (r ** 3) + (1 / (r ** 2) * (rplusdr - r) / ds) * dz / ds) + dy

            x = x + dx
            y = y + dy
            z = z + dz
            rho = (x ** 2 + y ** 2) ** (1 / 2)
            pox2.append(x)
            poy2.append(y)
            poz2.append(z)
            rhos.append(rho)
            s += ds

    else:
        while s<1600:
            ds=(dx**2 + dy**2 + dz**2)**(1/2)
            r=(x**2+y**2+z**2)**(1/2)
            rplusdr=((x+dx)**2+(y+dy)**2+(z+dz)**2)**(1/2)
            nr = (1 + r)/r
            D_one_devide_nr=1/(r+1)-r/(r+1)**2

            dx=(ds**2)*(1/nr)*(-x/(r**3)+( 1/(r**2) * (rplusdr - r)/ds)*dx/ds )+dx
            dz=(ds**2)*(1/nr)*(-z/(r**3)+( 1/(r**2) * (rplusdr - r)/ds)*dz/ds )+dz
            dy=(ds**2)*(1/nr)*(-y/(r**3)+( 1/(r**2) * (rplusdr - r)/ds)*dz/ds )+dy

            x=x+dx
            y=y+dy
            z=z+dz
            rho = (x ** 2 + y ** 2) ** (1 / 2)
            pox2.append(x)
            poy2.append(y)
            poz2.append(z)
            rhos.append(rho)
            s+=ds


    global xn
    global yn
    global zn
    # global fig


    xn = 'x'+str(n)
    yn = 'y'+str(n)
    zn = 'z'+str(n)


    xn = pox2
    yn = poy2
    zn = poz2
    rho= rhos

    if d==3:
        if m==1:
            ax.plot(0, 0, 0, '*')
        if m==2:
            ax.plot(-20, 0, 0, '*')
            ax.plot(20, 0, 0, '*')
    if d==2:
        plt.plot(0,0,'*')
    return rho,xn,yn,zn



















#
#
#
# def rays2d(th,zs,z0):
#     import numpy as np
#     import matplotlib.pyplot as plt
#     import math
#
#     pox2=[]
#     poz2=[]
#
#
#
#     z=zs
#     x=0.1
#     pox=np.array([])
#     poz=np.array([])
#     s=0
#
#     dz=-0.1
#     dx=-dz*math.tan(th*math.pi/180) #one degree with the negative z axes
#
#     while s<3000:
#         ds=(dx**2 + dz**2)**(1/2)
#         r=(x**2+z**2)**(1/2)
#         rplusdr=((x+dx)**2+(z+dz)**2)**(1/2)
#         nr = (1 + r)/r
#         Donedevidenr=1/(r+1)-r/(r+1)**2
#
#         dx=(ds**2)*(1/nr)*(-x/(r**3)+( 1/(r**2) * (rplusdr - r)/ds)*dx/ds )+dx
#         dz=(ds**2)*(1/nr)*(-z/(r**3)+( 1/(r**2) * (rplusdr - r)/ds)*dz/ds )+dz
#
#
#         x=x+dx
#         z=z+dz
#
#         # pox=np.append(pox,float(x))
#         # poz=np.append(poz,float(z))
#         pox2.append(x)
#         poz2.append(z)
#         s+=ds
#
#     plt.plot(pox2,poz2)
#
#

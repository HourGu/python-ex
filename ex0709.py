﻿import math
def move(x,y,step,angle):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


from line import MidpointLine

line = MidpointLine()


def Reactangle(value=100, x=0, y=0):
    for i in range(value):
        line.midpoint(0 + x, 2*(i + y), value + x, 2 * (i + y))

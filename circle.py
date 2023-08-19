from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class MidpointCircle:
    def __init__(self):
        self.__midpoint_points = []


    def convert_to_other_zone(self, x1, y1, zone):
        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def midpoint_circle_algorithm(self, radius, center_x=0.0, center_y=0.0, y=0):
        glBegin(GL_POINTS)

        d = 1 - radius

        x = radius
        glVertex2f(x + center_x, y + center_y)

        for i in range(8):
            x_other, y_other = self.convert_to_other_zone(x, y, i)
            glVertex2f(x_other + center_x, y_other + center_y)

        while x > y:
            if d < 0:
                y = y + 1
                d = d + 2 * y + 3
            else:
                x = x - 1
                y = y + 1
                d = d + 2 * y - 2 * x + 5

            self.__midpoint_points.append((x, y))

            glVertex2f(x + center_x, y + center_y)

            for i in range(8):
                x_other, y_other = self.convert_to_other_zone(x, y, i)
                self.__midpoint_points.append((x_other, y_other))
                glVertex2f(x_other + center_x, y_other + center_y)

        glEnd()

    def filled_circle(self, radius, center_x=0, center_y=0):
        for i in range(radius):
            self.midpoint_circle_algorithm(i, center_x, center_y)


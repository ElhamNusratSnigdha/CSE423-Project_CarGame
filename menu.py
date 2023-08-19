from circle import MidpointCircle
from line import MidpointLine
from digits import Digits



from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


line = MidpointLine()
circle = MidpointCircle()


class Menu:
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0,
                 pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.pixel_size = pixel_size

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor3f(0, 0, 0)

        self.text()

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def game_over_text(self, x=0, y=0):
        for i in range(10, 50, 1):
            self.g(adjust=0, x=i + x, y=i + y)
            self.a(adjust=150, x=i + x, y=i + y)
            self.m(adjust=300, x=i + x, y=i + y)
            self.e(adjust=450, x=i + x, y=i + y)
            self.o(adjust=750, x=i + x, y=i + y)
            self.v(adjust=900, x=i + x, y=i + y)
            self.e(adjust=1050, x=i + x, y=i + y)
            self.r(adjust=1200, x=i + x, y=i + y)

    def score_text(self, x=0, y=0):
        for i in range(10, 40, 1):
            self.s(adjust=0, x=i + x, y=i + y)
            self.c(adjust=150, x=i + x, y=i + y)
            self.o(adjust=300, x=i + x, y=i + y)
            self.r(adjust=450, x=i + x, y=i + y)
            self.e(adjust=600, x=i + x, y=i + y)

    def text(self):
        for i in range(0, 10, 2):
            circle.midpoint_circle_algorithm(700 - i, 0, 0)

        for i in range(0, 100, 10):
            circle.midpoint_circle_algorithm(700 - i, 0, 0)

        left_x1, left_y1 = -700, -900
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, 900)

        for i in range(10):
            line.midpoint(left_x1 + offset + i, left_y1, left_x1 + offset + i + i * 10, 900)
            line.midpoint(-left_x1 - offset - i, left_y1, -left_x1 - offset - i - i * 10, 900)

        score_text = Digits()
        digit_position = 900
        SCORE = 00

        for i in range(5, 20, 10):
            score_text.draw_digit(f"{SCORE}", offset_x=i, offset_y=i, digit_position_x=digit_position)



    def a(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150) 
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  

    def g(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70) 
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  

    def m(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  

        line.midpoint(x + 45 + adjust, y + 10 + 80, x + 70 + adjust, y + 60 + 80)
        line.midpoint(x + 40 + adjust, y + 10 + 80, x + 10 + adjust, y + 60 + 80)

    def e(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150) 
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0) 
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  

    def o(self,  x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150) 
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150) 
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  

    def v(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  

        line.midpoint(x + 45 + adjust, y + 0, x + 80 + adjust, y + 60) 
        line.midpoint(x + 35 + adjust, y + 0, x + 0 + adjust, y + 60)  

    def r(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 80, x + 80 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  

        line.midpoint(x + 80 + adjust, y + 0, x + 10 + adjust, y + 60)  


    def s(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 80 + adjust, y + 0, x + 80 + adjust, y + 70)  
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0)  
        line.midpoint(x + 10 + adjust, y + 70, x + 70 + adjust, y + 70)  

    def c(self, x=0, y=0, adjust=0):
        line.midpoint(x + 0 + adjust, y + 0, x + 0 + adjust, y + 70)  
        line.midpoint(x + 0 + adjust, y + 80, x + 0 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 150, x + 70 + adjust, y + 150)  
        line.midpoint(x + 10 + adjust, y + 0, x + 70 + adjust, y + 0) 


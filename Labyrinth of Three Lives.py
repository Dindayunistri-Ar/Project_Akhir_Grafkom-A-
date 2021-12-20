from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import OpenGL.GLUT as gl

# Koordinat x dan y untuk posisi kotak
pos_x = 0
pos_y = 0

# nyawa
nyawa = 3

# Mode untuk mengganti tampilan interface
mode = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-150, 1700.0, -150, 1700.0)


def kotak():
    global pos_x, pos_y, nyawa

    if nyawa > 0:
        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        # Kiri Atas
        glVertex2f(0 + pos_x, 100 + pos_y)
        # Kanan Atas
        glVertex2f(50 + pos_x, 100 + pos_y)
        # Kanan Bawah
        glVertex2f(50 + pos_x, 50 + pos_y)
        # Kiri Bawah
        glVertex2f(0 + pos_x, 50 + pos_y)
        glEnd()

    else:
        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        # Kiri Atas
        glVertex2f(0, 100)
        # Kanan Atas
        glVertex2f(50, 100)
        # Kanan Bawah
        glVertex2f(50, 50)
        # Kiri Bawah
        glVertex2f(0, 50)
        glEnd()


def maze():
    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 0)
    glVertex2f(0, 50)
    glVertex2f(100, 50)
    glVertex2f(100, 150)
    glVertex2f(450, 150)
    glVertex2f(450, 100)
    glVertex2f(150, 100)
    glVertex2f(150, 50)
    glVertex2f(500, 50)
    glVertex2f(500, 300)
    glVertex2f(450, 300)
    glVertex2f(450, 200)
    glVertex2f(200, 200)
    glVertex2f(200, 250)
    glVertex2f(400, 250)
    glVertex2f(400, 350)
    glVertex2f(550, 350)
    glVertex2f(550, 150)
    glVertex2f(800, 150)
    glVertex2f(800, 250)
    glVertex2f(1100, 250)
    glVertex2f(1100, 350)
    glVertex2f(1350, 350)
    glVertex2f(1350, 300)
    glVertex2f(1150, 300)
    glVertex2f(1150, 200)
    glVertex2f(950, 200)
    glVertex2f(950, 100)
    glVertex2f(900, 100)
    glVertex2f(900, 200)
    glVertex2f(850, 200)
    glVertex2f(850, 100)
    glVertex2f(550, 100)
    glVertex2f(550, 50)
    glVertex2f(1000, 50)
    glVertex2f(1000, 150)
    glVertex2f(1150, 150)
    glVertex2f(1150, 100)
    glVertex2f(1050, 100)
    glVertex2f(1050, 50)
    glVertex2f(1200, 50)
    glVertex2f(1200, 150)
    glVertex2f(1450, 150)
    glVertex2f(1450, 100)
    glVertex2f(1250, 100)
    glVertex2f(1250, 50)
    glVertex2f(1500, 50)
    glVertex2f(1500, 300)
    glVertex2f(1450, 300)
    glVertex2f(1450, 200)
    glVertex2f(1200, 200)
    glVertex2f(1200, 250)
    glVertex2f(1400, 250)
    glVertex2f(1400, 450)
    glVertex2f(1450, 450)
    glVertex2f(1450, 350)
    glVertex2f(1500, 350)
    glVertex2f(1500, 600)
    glVertex2f(1450, 600)
    glVertex2f(1450, 500)
    glVertex2f(1400, 500)
    glVertex2f(1400, 650)
    glVertex2f(1500, 650)
    glVertex2f(1500, 1000)
    glVertex2f(1400, 1000)
    glVertex2f(1400, 1100)
    glVertex2f(1350, 1100)
    glVertex2f(1350, 900)
    glVertex2f(1150, 900)
    glVertex2f(1150, 750)
    glVertex2f(1250, 750)
    glVertex2f(1250, 700)
    glVertex2f(900, 700)
    glVertex2f(900, 900)
    glVertex2f(850, 900)
    glVertex2f(850, 700)
    glVertex2f(800, 700)
    glVertex2f(800, 1000)
    glVertex2f(550, 1000)
    glVertex2f(550, 950)
    glVertex2f(650, 950)
    glVertex2f(650, 900)
    glVertex2f(500, 900)
    glVertex2f(500, 1050)
    glVertex2f(600, 1050)
    glVertex2f(600, 1350)
    glVertex2f(750, 1350)
    glVertex2f(750, 1300)
    glVertex2f(650, 1300)
    glVertex2f(650, 1050)
    glVertex2f(800, 1050)
    glVertex2f(800, 1150)
    glVertex2f(850, 1150)
    glVertex2f(850, 950)
    glVertex2f(950, 950)
    glVertex2f(950, 750)
    glVertex2f(1100, 750)
    glVertex2f(1100, 1250)
    glVertex2f(1150, 1250)
    glVertex2f(1150, 950)
    glVertex2f(1300, 950)
    glVertex2f(1300, 1150)
    glVertex2f(1450, 1150)
    glVertex2f(1450, 1050)
    glVertex2f(1500, 1050)
    glVertex2f(1500, 1450)
    glVertex2f(1550, 1450)
    glVertex2f(1550, 0)
    glVertex2f(0, 0)

    glEnd()


def maze1():
    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 100)
    glVertex2f(50, 100)
    glVertex2f(50, 200)
    glVertex2f(150, 200)
    glVertex2f(150, 300)
    glVertex2f(350, 300)
    glVertex2f(350, 350)
    glVertex2f(100, 350)
    glVertex2f(100, 250)
    glVertex2f(50, 250)
    glVertex2f(50, 600)
    glVertex2f(100, 600)
    glVertex2f(100, 400)
    glVertex2f(450, 400)
    glVertex2f(450, 500)
    glVertex2f(700, 500)
    glVertex2f(700, 250)
    glVertex2f(650, 250)
    glVertex2f(650, 450)
    glVertex2f(500, 450)
    glVertex2f(500, 400)
    glVertex2f(600, 400)
    glVertex2f(600, 200)
    glVertex2f(750, 200)
    glVertex2f(750, 300)
    glVertex2f(1050, 300)
    glVertex2f(1050, 350)
    glVertex2f(950, 350)
    glVertex2f(950, 550)
    glVertex2f(900, 550)
    glVertex2f(900, 350)
    glVertex2f(750, 350)
    glVertex2f(750, 550)
    glVertex2f(650, 550)
    glVertex2f(650, 750)
    glVertex2f(450, 750)
    glVertex2f(450, 1100)
    glVertex2f(550, 1100)
    glVertex2f(550, 1250)
    glVertex2f(450, 1250)
    glVertex2f(450, 1450)
    glVertex2f(400, 1450)
    glVertex2f(400, 1250)
    glVertex2f(250, 1250)
    glVertex2f(250, 1450)
    glVertex2f(100, 1450)
    glVertex2f(100, 1400)
    glVertex2f(200, 1400)
    glVertex2f(200, 1200)
    glVertex2f(500, 1200)
    glVertex2f(500, 1150)
    glVertex2f(400, 1150)
    glVertex2f(400, 950)
    glVertex2f(250, 950)
    glVertex2f(250, 1100)
    glVertex2f(300, 1100)
    glVertex2f(300, 1000)
    glVertex2f(350, 1000)
    glVertex2f(350, 1150)
    glVertex2f(200, 1150)
    glVertex2f(200, 900)
    glVertex2f(400, 900)
    glVertex2f(400, 700)
    glVertex2f(600, 700)
    glVertex2f(600, 550)
    glVertex2f(200, 550)
    glVertex2f(200, 500)
    glVertex2f(400, 500)
    glVertex2f(400, 450)
    glVertex2f(150, 450)
    glVertex2f(150, 650)
    glVertex2f(50, 650)
    glVertex2f(50, 800)
    glVertex2f(100, 800)
    glVertex2f(100, 700)
    glVertex2f(200, 700)
    glVertex2f(200, 600)
    glVertex2f(250, 600)
    glVertex2f(250, 800)
    glVertex2f(300, 800)
    glVertex2f(300, 600)
    glVertex2f(550, 600)
    glVertex2f(550, 650)
    glVertex2f(350, 650)
    glVertex2f(350, 850)
    glVertex2f(200, 850)
    glVertex2f(200, 750)
    glVertex2f(150, 750)
    glVertex2f(150, 850)
    glVertex2f(50, 850)
    glVertex2f(50, 900)
    glVertex2f(150, 900)
    glVertex2f(150, 950)
    glVertex2f(50, 950)
    glVertex2f(50, 1200)
    glVertex2f(100, 1200)
    glVertex2f(100, 1000)
    glVertex2f(150, 1000)
    glVertex2f(150, 1250)
    glVertex2f(50, 1250)
    glVertex2f(50, 1300)
    glVertex2f(150, 1300)
    glVertex2f(150, 1350)
    glVertex2f(50, 1350)
    glVertex2f(50, 1450)
    glVertex2f(0, 1450)
    #

    glEnd()


def maze1_1():
    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(50, 1500)
    glVertex2f(300, 1500)
    glVertex2f(300, 1300)
    glVertex2f(350, 1300)
    glVertex2f(350, 1500)
    glVertex2f(600, 1500)
    glVertex2f(600, 1450)
    glVertex2f(500, 1450)
    glVertex2f(500, 1300)
    glVertex2f(550, 1300)
    glVertex2f(550, 1400)
    glVertex2f(800, 1400)
    glVertex2f(800, 1250)
    glVertex2f(700, 1250)
    glVertex2f(700, 1100)
    glVertex2f(750, 1100)
    glVertex2f(750, 1200)
    glVertex2f(900, 1200)
    glVertex2f(900, 1000)
    glVertex2f(1000, 1000)
    glVertex2f(1000, 800)
    glVertex2f(1050, 800)
    glVertex2f(1050, 1300)
    glVertex2f(1200, 1300)
    glVertex2f(1200, 1000)
    glVertex2f(1250, 1000)
    glVertex2f(1250, 1200)
    glVertex2f(1450, 1200)
    glVertex2f(1450, 1450)
    glVertex2f(1300, 1450)
    glVertex2f(1300, 1400)
    glVertex2f(1400, 1400)
    glVertex2f(1400, 1250)
    glVertex2f(1250, 1250)
    glVertex2f(1250, 1300)
    glVertex2f(1350, 1300)
    glVertex2f(1350, 1350)
    glVertex2f(950, 1350)
    glVertex2f(950, 1450)
    glVertex2f(900, 1450)
    glVertex2f(900, 1300)
    glVertex2f(1000, 1300)
    glVertex2f(1000, 1050)
    glVertex2f(950, 1050)
    glVertex2f(950, 1250)
    glVertex2f(850, 1250)
    glVertex2f(850, 1450)
    glVertex2f(650, 1450)
    glVertex2f(650, 1500)
    glVertex2f(1200, 1500)
    glVertex2f(1200, 1450)
    glVertex2f(1000, 1450)
    glVertex2f(1000, 1400)
    glVertex2f(1250, 1400)
    glVertex2f(1250, 1500)
    glVertex2f(1550, 1500)
    glVertex2f(1550, 1550)
    glVertex2f(0, 1550)
    glVertex2f(0, 1500)
    glEnd()


def maze2():
    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1300, 400)
    glVertex2f(1300, 800)
    glVertex2f(1200, 800)
    glVertex2f(1200, 850)
    glVertex2f(1400, 850)
    glVertex2f(1400, 950)
    glVertex2f(1450, 950)
    glVertex2f(1450, 700)
    glVertex2f(1400, 700)
    glVertex2f(1400, 800)
    glVertex2f(1350, 800)
    glVertex2f(1350, 400)

    glEnd()


def maze3():
    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1200, 400)
    glVertex2f(1200, 600)
    glVertex2f(1150, 600)
    glVertex2f(1150, 500)
    glVertex2f(1050, 500)
    glVertex2f(1050, 450)
    glVertex2f(1150, 450)
    glVertex2f(1150, 400)
    glVertex2f(1000, 400)
    glVertex2f(1000, 550)
    glVertex2f(1100, 550)
    glVertex2f(1100, 600)
    glVertex2f(850, 600)
    glVertex2f(850, 400)
    glVertex2f(850, 400)
    glVertex2f(800, 400)
    glVertex2f(800, 600)
    glVertex2f(700, 600)
    glVertex2f(700, 800)
    glVertex2f(500, 800)
    glVertex2f(500, 850)
    glVertex2f(700, 850)
    glVertex2f(700, 950)
    glVertex2f(750, 950)
    glVertex2f(750, 650)
    glVertex2f(1250, 650)
    glVertex2f(1250, 400)

    glEnd()


def start():

    # M berwarna
    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(102, 1000)
    glVertex2f(102, 1500)
    glVertex2f(198, 1500)
    glVertex2f(198, 1000)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(198, 1405)
    glVertex2f(198, 1500)
    glVertex2f(394, 1500)
    glVertex2f(394, 1405)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(305, 1205)
    glVertex2f(305, 1407)
    glVertex2f(394, 1407)
    glVertex2f(394, 1205)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(394, 1205)
    glVertex2f(394, 1300)
    glVertex2f(600, 1300)
    glVertex2f(600, 1205)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(405, 1100)
    glVertex2f(405, 1205)
    glVertex2f(496, 1205)
    glVertex2f(496, 1100)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(505, 1205)
    glVertex2f(505, 1407)
    glVertex2f(600, 1407)
    glVertex2f(600, 1205)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(505, 1405)
    glVertex2f(505, 1500)
    glVertex2f(700, 1500)
    glVertex2f(700, 1405)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(696, 1000)
    glVertex2f(696, 1500)
    glVertex2f(796, 1500)
    glVertex2f(796, 1000)
    glEnd()

    # A warna
    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1002, 1400)
    glVertex2f(1002, 1500)
    glVertex2f(1398, 1500)
    glVertex2f(1398, 1400)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1002, 1300)
    glVertex2f(1002, 1404)
    glVertex2f(1100, 1404)
    glVertex2f(1100, 1300)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(897, 1000)
    glVertex2f(897, 1404)
    glVertex2f(1002, 1404)
    glVertex2f(1002, 1000)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1300, 1300)
    glVertex2f(1300, 1404)
    glVertex2f(1398, 1404)
    glVertex2f(1398, 1300)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1398, 1000)
    glVertex2f(1398, 1404)
    glVertex2f(1500, 1404)
    glVertex2f(1500, 1000)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1398, 997)
    glVertex2f(1398, 1100)
    glVertex2f(1202, 1100)
    glVertex2f(1202, 997)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(1300, 1100)
    glVertex2f(1300, 1200)
    glVertex2f(1100, 1200)
    glVertex2f(1100, 1100)
    glEnd()

    # Z berwarna
    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(800, 900)
    glVertex2f(800, 800)
    glVertex2f(100, 800)
    glVertex2f(100, 900)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(700, 600)
    glVertex2f(700, 800)
    glVertex2f(600, 800)
    glVertex2f(600, 600)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(600, 500)
    glVertex2f(600, 700)
    glVertex2f(500, 700)
    glVertex2f(500, 500)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(500, 500)
    glVertex2f(500, 600)
    glVertex2f(400, 600)
    glVertex2f(400, 500)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(500, 400)
    glVertex2f(500, 500)
    glVertex2f(300, 500)
    glVertex2f(300, 400)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(300, 300)
    glVertex2f(300, 500)
    glVertex2f(200, 500)
    glVertex2f(200, 300)
    glEnd()

    glColor3ub(235, 232, 52)
    glBegin(GL_QUADS)
    glVertex2f(100, 200)
    glVertex2f(100, 300)
    glVertex2f(800, 300)
    glVertex2f(800, 200)
    glEnd()

    # E warna
    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(900, 206)
    glVertex2f(900, 900)
    glVertex2f(1000, 900)
    glVertex2f(1000, 206)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1000, 800)
    glVertex2f(1000, 900)
    glVertex2f(1500, 900)
    glVertex2f(1500, 800)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1100, 700)
    glVertex2f(1100, 800)
    glVertex2f(1206, 800)
    glVertex2f(1206, 700)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1000, 406)
    glVertex2f(1000, 600)
    glVertex2f(1100, 600)
    glVertex2f(1100, 406)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1000, 506)
    glVertex2f(1000, 600)
    glVertex2f(1500, 600)
    glVertex2f(1500, 506)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1500, 406)
    glVertex2f(1500, 506)
    glVertex2f(1400, 506)
    glVertex2f(1400, 406)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1400, 600)
    glVertex2f(1400, 700)
    glVertex2f(1300, 700)
    glVertex2f(1300, 600)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1000, 206)
    glVertex2f(1000, 300)
    glVertex2f(1500, 300)
    glVertex2f(1500, 206)
    glEnd()

    glColor3ub(240, 10, 29)
    glBegin(GL_QUADS)
    glVertex2f(1200, 300)
    glVertex2f(1200, 400)
    glVertex2f(1300, 400)
    glVertex2f(1300, 300)
    glEnd()

    # M
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 1000)
    glVertex2f(100, 1500)
    glVertex2f(400, 1500)
    glVertex2f(400, 1300)
    glVertex2f(500, 1300)
    glVertex2f(500, 1500)
    glVertex2f(800, 1500)
    glVertex2f(800, 1000)
    glVertex2f(700, 1000)
    glVertex2f(700, 1400)
    glVertex2f(600, 1400)
    glVertex2f(600, 1200)
    glVertex2f(500, 1200)
    glVertex2f(500, 1100)
    glVertex2f(400, 1100)
    glVertex2f(400, 1200)
    glVertex2f(300, 1200)
    glVertex2f(300, 1400)
    glVertex2f(200, 1400)
    glVertex2f(200, 1000)
    glEnd()

    # A
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(900, 1000)
    glVertex2f(900, 1400)
    glVertex2f(1000, 1400)
    glVertex2f(1000, 1500)
    glVertex2f(1400, 1500)
    glVertex2f(1400, 1400)
    glVertex2f(1500, 1400)
    glVertex2f(1500, 1000)
    glVertex2f(1200, 1000)
    glVertex2f(1200, 1100)
    glVertex2f(1100, 1100)
    glVertex2f(1100, 1200)
    glVertex2f(1300, 1200)
    glVertex2f(1300, 1100)
    glVertex2f(1400, 1100)
    glVertex2f(1400, 1300)
    glVertex2f(1300, 1300)
    glVertex2f(1300, 1400)
    glVertex2f(1100, 1400)
    glVertex2f(1100, 1300)
    glVertex2f(1000, 1300)
    glVertex2f(1000, 1000)
    glEnd()

    # Z
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 900)
    glVertex2f(800, 900)
    glVertex2f(800, 800)
    glVertex2f(700, 800)
    glVertex2f(700, 600)
    glVertex2f(600, 600)
    glVertex2f(600, 500)
    glVertex2f(500, 500)
    glVertex2f(500, 400)
    glVertex2f(300, 400)
    glVertex2f(300, 300)
    glVertex2f(800, 300)
    glVertex2f(800, 200)
    glVertex2f(100, 200)
    glVertex2f(100, 300)
    glVertex2f(200, 300)
    glVertex2f(200, 500)
    glVertex2f(400, 500)
    glVertex2f(400, 600)
    glVertex2f(500, 600)
    glVertex2f(500, 700)
    glVertex2f(600, 700)
    glVertex2f(600, 800)
    glVertex2f(100, 800)
    glEnd()

    # e
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(900, 900)
    glVertex2f(1500, 900)
    glVertex2f(1500, 800)
    glVertex2f(1200, 800)
    glVertex2f(1200, 700)
    glVertex2f(1100, 700)
    glVertex2f(1100, 800)
    glVertex2f(1000, 800)
    glVertex2f(1000, 600)
    glVertex2f(1300, 600)
    glVertex2f(1300, 700)
    glVertex2f(1400, 700)
    glVertex2f(1400, 600)
    glVertex2f(1500, 600)
    glVertex2f(1500, 400)
    glVertex2f(1400, 400)
    glVertex2f(1400, 500)
    glVertex2f(1100, 500)
    glVertex2f(1100, 400)
    glVertex2f(1000, 400)
    glVertex2f(1000, 300)
    glVertex2f(1200, 300)
    glVertex2f(1200, 400)
    glVertex2f(1300, 400)
    glVertex2f(1300, 300)
    glVertex2f(1500, 300)
    glVertex2f(1500, 200)
    glVertex2f(900, 200)
    glEnd()


def menu():

    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 1150)
    glVertex2f(100, 1500)
    glVertex2f(250, 1500)
    glVertex2f(250, 1350)
    glVertex2f(300, 1350)
    glVertex2f(300, 1500)
    glVertex2f(450, 1500)
    glVertex2f(450, 1150)
    glVertex2f(400, 1150)
    glVertex2f(400, 1450)
    glVertex2f(350, 1450)
    glVertex2f(350, 1300)
    glVertex2f(300, 1300)
    glVertex2f(300, 1250)
    glVertex2f(250, 1250)
    glVertex2f(250, 1300)
    glVertex2f(200, 1300)
    glVertex2f(200, 1450)
    glVertex2f(150, 1450)
    glVertex2f(150, 1150)
    glEnd()

    # A
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(500, 1150)
    glVertex2f(500, 1450)
    glVertex2f(550, 1450)
    glVertex2f(550, 1500)
    glVertex2f(750, 1500)
    glVertex2f(750, 1450)
    glVertex2f(800, 1450)
    glVertex2f(800, 1150)
    glVertex2f(650, 1150)
    glVertex2f(650, 1300)
    glVertex2f(600, 1300)
    glVertex2f(600, 1350)
    glVertex2f(700, 1350)
    glVertex2f(700, 1200)
    glVertex2f(750, 1200)
    glVertex2f(750, 1400)
    glVertex2f(700, 1400)
    glVertex2f(700, 1450)
    glVertex2f(700, 1450)
    glVertex2f(600, 1450)
    glVertex2f(600, 1400)
    glVertex2f(550, 1400)
    glVertex2f(550, 1250)
    glVertex2f(600, 1250)
    glVertex2f(600, 1200)
    glVertex2f(550, 1200)
    glVertex2f(550, 1150)
    glEnd()

    # Z
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(850, 1500)
    glVertex2f(1150, 1500)
    glVertex2f(1150, 1450)
    glVertex2f(1100, 1450)
    glVertex2f(1100, 1350)
    glVertex2f(1050, 1350)
    glVertex2f(1050, 1300)
    glVertex2f(1000, 1300)
    glVertex2f(1000, 1250)
    glVertex2f(1000, 1250)
    glVertex2f(950, 1250)
    glVertex2f(950, 1200)
    glVertex2f(1150, 1200)
    glVertex2f(1150, 1150)
    glVertex2f(850, 1150)
    glVertex2f(850, 1200)
    glVertex2f(900, 1200)
    glVertex2f(900, 1300)
    glVertex2f(950, 1300)
    glVertex2f(950, 1350)
    glVertex2f(1000, 1350)
    glVertex2f(1000, 1400)
    glVertex2f(1050, 1400)
    glVertex2f(1050, 1450)
    glVertex2f(850, 1450)
    glEnd()

    # E
    glColor3ub(235, 232, 52)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1200, 1500)
    glVertex2f(1500, 1500)
    glVertex2f(1500, 1450)
    glVertex2f(1450, 1450)
    glVertex2f(1450, 1400)
    glVertex2f(1400, 1400)
    glVertex2f(1400, 1450)
    glVertex2f(1250, 1450)
    glVertex2f(1250, 1350)
    glVertex2f(1300, 1350)
    glVertex2f(1350, 1350)
    glVertex2f(1500, 1350)
    glVertex2f(1500, 1300)
    glVertex2f(1350, 1300)
    glVertex2f(1350, 1250)
    glVertex2f(1300, 1250)
    glVertex2f(1300, 1300)
    glVertex2f(1250, 1300)
    glVertex2f(1250, 1200)
    glVertex2f(1400, 1200)
    glVertex2f(1400, 1250)
    glVertex2f(1450, 1250)
    glVertex2f(1450, 1200)
    glVertex2f(1500, 1200)
    glVertex2f(1500, 1150)
    glVertex2f(1200, 1150)
    glEnd()

    # Play kotak

    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(600, 800)
    glVertex2f(1000, 800)
    glVertex2f(1000, 600)
    glVertex2f(600, 600)
    glEnd()

    # Play segitiga
    glColor3ub(235, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(740, 760)
    glVertex2f(880, 700)
    glVertex2f(740, 640)
    glEnd()


def shape_nyawa(scene_nyawa):
    global text, mode

    if scene_nyawa == 3:
        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1150, 1670)
        glVertex2f(1235, 1670)
        glVertex2f(1235, 1600)
        glVertex2f(1150, 1600)
        glEnd()

        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1300, 1670)
        glVertex2f(1400, 1670)
        glVertex2f(1400, 1600)
        glVertex2f(1300, 1600)
        glEnd()

        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1450, 1670)
        glVertex2f(1550, 1670)
        glVertex2f(1550, 1600)
        glVertex2f(1450, 1600)

        glEnd()

    elif scene_nyawa == 2:

        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1300, 1670)
        glVertex2f(1400, 1670)
        glVertex2f(1400, 1600)
        glVertex2f(1300, 1600)
        glEnd()

        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1450, 1670)
        glVertex2f(1550, 1670)
        glVertex2f(1550, 1600)
        glVertex2f(1450, 1600)

        glEnd()

    elif scene_nyawa == 1:

        glColor3ub(255, 255, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1450, 1670)
        glVertex2f(1550, 1670)
        glVertex2f(1550, 1600)
        glVertex2f(1450, 1600)

        glEnd()

    elif scene_nyawa == 0:
        mode = 3


def drawBitmapText(string, x, y, z):
    global text
    if text == False:
        glRasterPos3f(x, y, z)
        for karakter in string:
            glColor3ub(255, 255, 255)
            glutBitmapCharacter(gl.GLUT_BITMAP_TIMES_ROMAN_24, ord(karakter))


def on_click(button, state, x, y):
    global mode, nyawa, pos_x, pos_y
    if mode == 0:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            mode = 1
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    elif mode == 1:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if (x >= 220 and x <= 340) and (y >= 241 and y <= 295):
                mode = 2
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    elif mode == 2:
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            mode = 2
            pos_x = 0
            pos_y = 0
            nyawa = 3
    elif mode == 3 or mode == 4:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            if (x >= 333 and x <= 402) and (y >= 275 and y <= 303):
                mode = 2
                pos_x = 0
                pos_y = 0
                nyawa = 3
            print("Klik Kiri ditekan ", "(", x, ",", y, ")")
    print(f'nyawa {nyawa} | mode {mode}')


def display():
    global mode, nyawa, pos_x, pos_y, text, nyawa, over
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glPopMatrix()
    if mode == 0:
        start()
    elif mode == 1:
        menu()
    elif mode == 2:
        kotak()
        maze()
        maze1()
        maze1_1()
        maze2()
        maze3()
        shape_nyawa(nyawa)
        if pos_x == 1550 and pos_y == 1400 or pos_x == -50 and pos_y == 1400 or pos_x == 850 and pos_y == 800:
            mode = 4

    elif mode == 3:
        kotak()
        maze()
        maze1()
        maze1_1()
        maze2()
        maze3()
        shape_nyawa(nyawa)

        text = False
        glColor3ub(10, 2, 2)
        glBegin(GL_POLYGON)
        glVertex2f(300, 1300)
        glVertex2f(1300, 1300)
        glVertex2f(1300, 550)
        glVertex2f(300, 550)
        glEnd()

        drawBitmapText(' ', 950, 600, 0)
        drawBitmapText("Ulangi", 980, 600, 0)
        drawBitmapText("GAME OVER !!!", 500, 970, 0)

    elif mode == 4:
        kotak()
        maze()
        maze1()
        maze1_1()
        maze2()
        maze3()
        shape_nyawa(nyawa)

        if mode == 4 and (pos_x == 1550 and pos_y == 1400 or pos_x == -50 and pos_y == 1400 or pos_x == 850 and pos_y == 800):
            text = False

            glColor3ub(10, 2, 2)
            glBegin(GL_POLYGON)
            glVertex2f(300, 1300)
            glVertex2f(1300, 1300)
            glVertex2f(1300, 550)
            glVertex2f(300, 550)
            glEnd()

            drawBitmapText(' ', 950, 600, 0)
            drawBitmapText("^-^ ", 700, 700, 0)
            drawBitmapText("YOU WIN !!!", 550, 970, 0)
            drawBitmapText("Ulangi", 980, 600, 0)
    glFlush()


def input_keyboard(key, x, y):
    global pos_x, pos_y, nyawa

    if mode == 2:
        if key == GLUT_KEY_UP:
            if pos_x == 0 and pos_y == 0 or pos_x == 50 and pos_y == 100 or pos_x == 100 and pos_y == 100 or pos_x == 200 and pos_y == 100 or pos_x == 250 and pos_y == 100 or pos_x == 300 and pos_y == 100 or pos_x == 350 and pos_y == 100 or pos_x == 400 and pos_y == 100 or pos_x == 450 and pos_y == 200 or pos_x == 400 and pos_y == 0 or pos_x == 350 and pos_y == 0 or pos_x == 300 and pos_y == 0 or pos_x == 250 and pos_y == 0 or pos_x == 200 and pos_y == 0 or pos_x == 150 and pos_y == 0 or pos_x == 150 and pos_y == 200 or pos_x == 200 and pos_y == 200 or pos_x == 250 and pos_y == 200 or pos_x == 300 and pos_y == 200 or pos_x == 350 and pos_y == 300 or pos_x == 300 and pos_y == 300 or pos_x == 250 and pos_y == 300 or pos_x == 200 and pos_y == 300 or pos_x == 150 and pos_y == 300 or pos_x == 100 and pos_y == 300 or pos_x == 50 and pos_y == 500 or pos_x == 400 and pos_y == 300 or pos_x == 500 and pos_y == 300 or pos_x == 550 and pos_y == 300 or pos_x == 600 and pos_y == 100 or pos_x == 650 and pos_y == 100 or pos_x == 700 and pos_y == 100 or pos_x == 750 and pos_y == 200 or pos_x == 800 and pos_y == 200 or pos_x == 850 and pos_y == 200 or pos_x == 900 and pos_y == 200 or pos_x == 950 and pos_y == 200 or pos_x == 1000 and pos_y == 200 or pos_x == 1050 and pos_y == 300 or pos_x == 1100 and pos_y == 300 or pos_x == 1100 and pos_y == 400 or pos_x == 1050 and pos_y == 400 or pos_x == 1150 and pos_y == 500 or pos_x == 1200 and pos_y == 300 or pos_x == 1200 and pos_y == 600 or pos_x == 1150 and pos_y == 600 or pos_x == 1100 and pos_y == 600 or pos_x == 1050 and pos_y == 600 or pos_x == 1000 and pos_y == 600 or pos_x == 950 and pos_y == 600 or pos_x == 900 and pos_y == 600 or pos_x == 850 and pos_y == 800 or pos_x == 800 and pos_y == 600 or pos_x == 750 and pos_y == 900 or pos_x == 700 and pos_y == 900 or pos_x == 650 and pos_y == 900 or pos_x == 600 and pos_y == 900 or pos_x == 550 and pos_y == 900 or pos_x == 600 and pos_y == 800 or pos_x == 550 and pos_y == 800 or pos_x == 500 and pos_y == 800 or pos_x == 450 and pos_y == 1000 or pos_x == 500 and pos_y == 1000 or pos_x == 500 and pos_y == 1200 or pos_x == 550 and pos_y == 1400 or pos_x == 500 and pos_y == 1400 or pos_x == 450 and pos_y == 1400 or pos_x == 400 and pos_y == 1400 or pos_x == 350 and pos_y == 1400 or pos_x == 300 and pos_y == 1200 or pos_x == 250 and pos_y == 1400 or pos_x == 200 and pos_y == 1400 or pos_x == 150 and pos_y == 1400 or pos_x == 100 and pos_y == 1400 or pos_x == 50 and pos_y == 1400 or pos_x == 100 and pos_y == 1300 or pos_x == 150 and pos_y == 1300 or pos_x == 100 and pos_y == 1200 or pos_x == 50 and pos_y == 1200 or pos_x == 200 and pos_y == 1100 or pos_x == 250 and pos_y == 1100 or pos_x == 300 and pos_y == 1100 or pos_x == 350 and pos_y == 1100 or pos_x == 400 and pos_y == 1100 or pos_x == 450 and pos_y == 1100 or pos_x == 300 and pos_y == 900 or pos_x == 250 and pos_y == 1000 or pos_x == 100 and pos_y == 900 or pos_x == 50 and pos_y == 1100 or pos_x == 100 and pos_y == 800 or pos_x == 50 and pos_y == 800 or pos_x == 200 and pos_y == 800 or pos_x == 250 and pos_y == 800 or pos_x == 300 and pos_y == 800 or pos_x == 350 and pos_y == 800 or pos_x == 400 and pos_y == 600 or pos_x == 450 and pos_y == 600 or pos_x == 500 and pos_y == 600 or pos_x == 550 and pos_y == 600 or pos_x == 500 and pos_y == 500 or pos_x == 450 and pos_y == 500 or pos_x == 400 and pos_y == 500 or pos_x == 350 and pos_y == 500 or pos_x == 300 and pos_y == 500 or pos_x == 250 and pos_y == 700 or pos_x == 200 and pos_y == 500 or pos_x == 150 and pos_y == 600 or pos_x == 100 and pos_y == 600 or pos_x == 50 and pos_y == 700 or pos_x == 200 and pos_y == 400 or pos_x == 250 and pos_y == 400 or pos_x == 300 and pos_y == 400 or pos_x == 350 and pos_y == 400 or pos_x == 550 and pos_y == 1300 or pos_x == 600 and pos_y == 1300 or pos_x == 650 and pos_y == 1300 or pos_x == 700 and pos_y == 1300 or pos_x == 750 and pos_y == 1300 or pos_x == 700 and pos_y == 1200 or pos_x == 650 and pos_y == 1200 or pos_x == 700 and pos_y == 1000 or pos_x == 750 and pos_y == 1100 or pos_x == 800 and pos_y == 1100 or pos_x == 850 and pos_y == 1100 or pos_x == 900 and pos_y == 900 or pos_x == 950 and pos_y == 900 or pos_x == 1000 and pos_y == 700 or pos_x == 10500 and pos_y == 1200 or pos_x == 1100 and pos_y == 1200 or pos_x == 1150 and pos_y == 1200 or pos_x == 1200 and pos_y == 900 or pos_x == 1250 and pos_y == 1100 or pos_x == 1300 and pos_y == 1100 or pos_x == 1350 and pos_y == 1100 or pos_x == 1400 and pos_y == 1100 or pos_x == 950 and pos_y == 1200 or pos_x == 900 and pos_y == 1200 or pos_x == 650 and pos_y == 1400 or pos_x == 700 and pos_y == 1400 or pos_x == 750 and pos_y == 1400 or pos_x == 800 and pos_y == 1400 or pos_x == 850 and pos_y == 1400 or pos_x == 900 and pos_y == 1400 or pos_x == 950 and pos_y == 1400 or pos_x == 1000 and pos_y == 1400 or pos_x == 1050 and pos_y == 1400 or pos_x == 1100 and pos_y == 1400 or pos_x == 1150 and pos_y == 1400 or pos_x == 1000 and pos_y == 1300 or pos_x == 1050 and pos_y == 1300 or pos_x == 1100 and pos_y == 1300 or pos_x == 1150 and pos_y == 1300 or pos_x == 1200 and pos_y == 1300 or pos_x == 1300 and pos_y == 1300 or pos_x == 1350 and pos_y == 1300 or pos_x == 1300 and pos_y == 1200 or pos_x == 1250 and pos_y == 1200 or pos_x == 1250 and pos_y == 1400 or pos_x == 1300 and pos_y == 1400 or pos_x == 1350 and pos_y == 1400 or pos_x == 1400 and pos_y == 1400 or pos_x == 1450 and pos_y == 1400 or pos_x == 1500 and pos_y == 1400 or pos_x == 1000 and pos_y == 300 or pos_x == 1050 and pos_y == 500 or pos_x == 1000 and pos_y == 500 or pos_x == 950 and pos_y == 500 or pos_x == 900 and pos_y == 500 or pos_x == 850 and pos_y == 500 or pos_x == 800 and pos_y == 300 or pos_x == 750 and pos_y == 500 or pos_x == 700 and pos_y == 500 or pos_x == 650 and pos_y == 700 or pos_x == 600 and pos_y == 700 or pos_x == 550 and pos_y == 700 or pos_x == 500 and pos_y == 700 or pos_x == 1250 and pos_y == 700 or pos_x == 1200 and pos_y == 700 or pos_x == 1150 and pos_y == 800 or pos_x == 1200 and pos_y == 800 or pos_x == 1250 and pos_y == 800 or pos_x == 1300 and pos_y == 800 or pos_x == 1350 and pos_y == 1000 or pos_x == 1400 and pos_y == 900 or pos_x == 1450 and pos_y == 900 or pos_x == 1400 and pos_y == 600 or pos_x == 1350 and pos_y == 700 or pos_x == 1300 and pos_y == 300 or pos_x == 1400 and pos_y == 400 or pos_x == 1450 and pos_y == 500 or pos_x == 1300 and pos_y == 200 or pos_x == 1250 and pos_y == 200 or pos_x == 1200 and pos_y == 200 or pos_x == 1150 and pos_y == 200 or pos_x == 550 and pos_y == 0 or pos_x == 600 and pos_y == 0 or pos_x == 650 and pos_y == 0 or pos_x == 700 and pos_y == 0 or pos_x == 750 and pos_y == 0 or pos_x == 800 and pos_y == 0 or pos_x == 850 and pos_y == 100 or pos_x == 900 and pos_y == 0 or pos_x == 950 and pos_y == 100 or pos_x == 1000 and pos_y == 100 or pos_x == 1050 and pos_y == 100 or pos_x == 1100 and pos_y == 100 or pos_x == 1050 and pos_y == 0 or pos_x == 1100 and pos_y == 0 or pos_x == 1200 and pos_y == 100 or pos_x == 1250 and pos_y == 100 or pos_x == 1300 and pos_y == 100 or pos_x == 1350 and pos_y == 100 or pos_x == 1400 and pos_y == 100 or pos_x == 1450 and pos_y == 200 or pos_x == 1400 and pos_y == 0 or pos_x == 1350 and pos_y == 0 or pos_x == 1300 and pos_y == 0 or pos_x == 1250 and pos_y == 0 or pos_x == 450 and pos_y == 400 or pos_x == 500 and pos_y == 400 or pos_x == 550 and pos_y == 400 or pos_x == 600 and pos_y == 400 or pos_x == 650 and pos_y == 400 or pos_x == 1050 and pos_y == 1200:
                print('Menabrak Dinding!')
                nyawa -= 1
                print('Nyawa anda sisa :', nyawa)
                if nyawa == 0:
                    print('\nGAME OVER!\n')
            elif pos_x == 1550 and pos_y == 1400:
                print('You Win!')
            else:
                pos_y += 50
                print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
        elif key == GLUT_KEY_DOWN:
            if pos_x == 0 and pos_y == 0 or pos_x == 50 and pos_y == 0 or pos_x == 100 and pos_y == 100 or pos_x == 150 and pos_y == 100 or pos_x == 200 and pos_y == 100 or pos_x == 250 and pos_y == 100 or pos_x == 300 and pos_y == 100 or pos_x == 350 and pos_y == 100 or pos_x == 400 and pos_y == 100 or pos_x == 450 and pos_y == 0 or pos_x == 400 and pos_y == 0 or pos_x == 350 and pos_y == 0 or pos_x == 300 and pos_y == 0 or pos_x == 250 and pos_y == 0 or pos_x == 200 and pos_y == 0 or pos_x == 150 and pos_y == 0 or pos_x == 200 and pos_y == 200 or pos_x == 250 and pos_y == 200 or pos_x == 300 and pos_y == 200 or pos_x == 350 and pos_y == 200 or pos_x == 300 and pos_y == 300 or pos_x == 250 and pos_y == 300 or pos_x == 200 and pos_y == 300 or pos_x == 150 and pos_y == 300 or pos_x == 100 and pos_y == 300 or pos_x == 50 and pos_y == 200 or pos_x == 400 and pos_y == 300 or pos_x == 450 and pos_y == 300 or pos_x == 500 and pos_y == 300 or pos_x == 500 and pos_y == 400 or pos_x == 550 and pos_y == 400 or pos_x == 600 and pos_y == 400 or pos_x == 650 and pos_y == 200 or pos_x == 550 and pos_y == 100 or pos_x == 600 and pos_y == 100 or pos_x == 650 and pos_y == 100 or pos_x == 700 and pos_y == 100 or pos_x == 750 and pos_y == 100 or pos_x == 800 and pos_y == 200 or pos_x == 850 and pos_y == 200 or pos_x == 900 and pos_y == 200 or pos_x == 950 and pos_y == 200 or pos_x == 1000 and pos_y == 200 or pos_x == 1050 and pos_y == 200 or pos_x == 1000 and pos_y == 300 or pos_x == 950 and pos_y == 300 or pos_x == 1050 and pos_y == 500 or pos_x == 1000 and pos_y == 500 or pos_x == 900 and pos_y == 500 or pos_x == 850 and pos_y == 300 or pos_x == 800 and pos_y == 300 or pos_x == 750 and pos_y == 300 or pos_x == 700 and pos_y == 500 or pos_x == 650 and pos_y == 500 or pos_x == 600 and pos_y == 700 or pos_x == 550 and pos_y == 700 or pos_x == 500 and pos_y == 700 or pos_x == 450 and pos_y == 700 or pos_x == 500 and pos_y == 1000 or pos_x == 550 and pos_y == 1000 or pos_x == 500 and pos_y == 1200 or pos_x == 450 and pos_y == 1200 or pos_x == 550 and pos_y == 1400 or pos_x == 500 and pos_y == 1400 or pos_x == 400 and pos_y == 1400 or pos_x == 350 and pos_y == 1200 or pos_x == 300 and pos_y == 1200 or pos_x == 250 and pos_y == 1200 or pos_x == 200 and pos_y == 1400 or pos_x == 150 and pos_y == 1400 or pos_x == 100 and pos_y == 1400 or pos_x == 50 and pos_y == 1300 or pos_x == 100 and pos_y == 1300 or pos_x == 100 and pos_y == 1200 or pos_x == 50 and pos_y == 1200 or pos_x == 200 and pos_y == 1100 or pos_x == 250 and pos_y == 1100 or pos_x == 300 and pos_y == 1100 or pos_x == 400 and pos_y == 1100 or pos_x == 450 and pos_y == 1100 or pos_x == 350 and pos_y == 900 or pos_x == 300 and pos_y == 900 or pos_x == 250 and pos_y == 900 or pos_x == 100 and pos_y == 900 or pos_x == 50 and pos_y == 900 or pos_x == 100 and pos_y == 800 or pos_x == 50 and pos_y == 800 or pos_x == 150 and pos_y == 700 or pos_x == 200 and pos_y == 800 or pos_x == 250 and pos_y == 800 or pos_x == 300 and pos_y == 800 or pos_x == 350 and pos_y == 600 or pos_x == 400 and pos_y == 600 or pos_x == 450 and pos_y == 600 or pos_x == 500 and pos_y == 600 or pos_x == 550 and pos_y == 500 or pos_x == 500 and pos_y == 500 or pos_x == 450 and pos_y == 500 or pos_x == 400 and pos_y == 500 or pos_x == 350 and pos_y == 500 or pos_x == 300 and pos_y == 500 or pos_x == 250 and pos_y == 500 or pos_x == 200 and pos_y == 500 or pos_x == 100 and pos_y == 600 or pos_x == 50 and pos_y == 600 or pos_x == 150 and pos_y == 400 or pos_x == 200 and pos_y == 400 or pos_x == 250 and pos_y == 400 or pos_x == 300 and pos_y == 400 or pos_x == 350 and pos_y == 400 or pos_x == 500 and pos_y == 800 or pos_x == 550 and pos_y == 800 or pos_x == 600 and pos_y == 800 or pos_x == 650 and pos_y == 800 or pos_x == 550 and pos_y == 900 or pos_x == 600 and pos_y == 900 or pos_x == 700 and pos_y == 900 or pos_x == 750 and pos_y == 600 or pos_x == 800 and pos_y == 600 or pos_x == 850 and pos_y == 600 or pos_x == 900 and pos_y == 600 or pos_x == 950 and pos_y == 600 or pos_x == 1000 and pos_y == 600 or pos_x == 1050 and pos_y == 600 or pos_x == 1100 and pos_y == 600 or pos_x == 1150 and pos_y == 600 or pos_x == 1200 and pos_y == 600 or pos_x == 1250 and pos_y == 300 or pos_x == 1200 and pos_y == 300 or pos_x == 1150 and pos_y == 300 or pos_x == 1100 and pos_y == 300 or pos_x == 1100 and pos_y == 400 or pos_x == 1050 and pos_y == 400 or pos_x == 1300 and pos_y == 300 or pos_x == 1350 and pos_y == 200 or pos_x == 1300 and pos_y == 200 or pos_x == 1250 and pos_y == 200 or pos_x == 1200 and pos_y == 200 or pos_x == 550 and pos_y == 0 or pos_x == 600 and pos_y == 0 or pos_x == 650 and pos_y == 0 or pos_x == 700 and pos_y == 0 or pos_x == 750 and pos_y == 0 or pos_x == 800 and pos_y == 0 or pos_x == 850 and pos_y == 0 or pos_x == 900 and pos_y == 0 or pos_x == 950 and pos_y == 0 or pos_x == 1000 and pos_y == 100 or pos_x == 1050 and pos_y == 100 or pos_x == 1100 and pos_y == 100 or pos_x == 1050 and pos_y == 0 or pos_x == 1100 and pos_y == 0 or pos_x == 1150 and pos_y == 0 or pos_x == 1200 and pos_y == 100 or pos_x == 1250 and pos_y == 100 or pos_x == 1300 and pos_y == 100 or pos_x == 1350 and pos_y == 100 or pos_x == 1400 and pos_y == 100 or pos_x == 1450 and pos_y == 0 or pos_x == 1400 and pos_y == 0 or pos_x == 1350 and pos_y == 0 or pos_x == 1300 and pos_y == 0 or pos_x == 1250 and pos_y == 0 or pos_x == 1400 and pos_y == 400 or pos_x == 1450 and pos_y == 300 or pos_x == 1400 and pos_y == 600 or pos_x == 1450 and pos_y == 600 or pos_x == 1400 and pos_y == 900 or pos_x == 1350 and pos_y == 800 or pos_x == 1250 and pos_y == 800 or pos_x == 1200 and pos_y == 800 or pos_x == 1150 and pos_y == 700 or pos_x == 1200 and pos_y == 700 or pos_x == 600 and pos_y == 1300 or pos_x == 650 and pos_y == 1300 or pos_x == 700 and pos_y == 1300 or pos_x == 750 and pos_y == 1200 or pos_x == 700 and pos_y == 1200 or pos_x == 650 and pos_y == 1000 or pos_x == 700 and pos_y == 1000 or pos_x == 750 and pos_y == 1000 or pos_x == 800 and pos_y == 1100 or pos_x == 850 and pos_y == 900 or pos_x == 900 and pos_y == 900 or pos_x == 950 and pos_y == 700 or pos_x == 1000 and pos_y == 700 or pos_x == 1050 and pos_y == 700 or pos_x == 1100 and pos_y == 1200 or pos_x == 1150 and pos_y == 900 or pos_x == 1200 and pos_y == 900 or pos_x == 1250 and pos_y == 900 or pos_x == 1300 and pos_y == 1100 or pos_x == 1350 and pos_y == 1100 or pos_x == 1400 and pos_y == 1100 or pos_x == 1450 and pos_y == 1000 or pos_x == 950 and pos_y == 1000 or pos_x == 900 and pos_y == 1200 or pos_x == 850 and pos_y == 1200 or pos_x == 650 and pos_y == 1400 or pos_x == 700 and pos_y == 1400 or pos_x == 750 and pos_y == 1400 or pos_x == 800 and pos_y == 1400 or pos_x == 900 and pos_y == 1400 or pos_x == 1000 and pos_y == 1400 or pos_x == 1050 and pos_y == 1400 or pos_x == 1100 and pos_y == 1400 or pos_x == 1150 and pos_y == 1400 or pos_x == 950 and pos_y == 1300 or pos_x == 1000 and pos_y == 1300 or pos_x == 1050 and pos_y == 1300 or pos_x == 1100 and pos_y == 1300 or pos_x == 1150 and pos_y == 1300 or pos_x == 1200 and pos_y == 1300 or pos_x == 1250 and pos_y == 1300 or pos_x == 1300 and pos_y == 1300 or pos_x == 1350 and pos_y == 1200 or pos_x == 1300 and pos_y == 1200 or pos_x == 1250 and pos_y == 1200 or pos_x == 1300 and pos_y == 800 or pos_x == 1300 and pos_y == 1400 or pos_x == 1350 and pos_y == 1400 or pos_x == 1400 and pos_y == 1400 or pos_x == 1500 and pos_y == 1400:
                print('Menabrak Dinding!')
                nyawa -= 1
                print('Nyawa anda sisa :', nyawa)
                if nyawa == 0:
                    print('\nGAME OVER!\n')
            elif pos_x == 1550 and pos_y == 1400:
                print('You Win!')
            else:
                pos_y -= 50
                print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)

        elif key == GLUT_KEY_RIGHT:
            if pos_x == 50 and pos_y == 0 or pos_x == 50 and pos_y == 50 or pos_x == 450 and pos_y == 200 or pos_x == 450 and pos_y == 150 or pos_x == 450 and pos_y == 100 or pos_x == 450 and pos_y == 50 or pos_x == 450 and pos_y == 0 or pos_x == 150 and pos_y == 150 or pos_x == 350 and pos_y == 200 or pos_x == 350 and pos_y == 250 or pos_x == 50 and pos_y == 500 or pos_x == 50 and pos_y == 450 or pos_x == 50 and pos_y == 400 or pos_x == 50 and pos_y == 350 or pos_x == 50 and pos_y == 250 or pos_x == 50 and pos_y == 200 or pos_x == 450 and pos_y == 350 or pos_x == 650 and pos_y == 400 or pos_x == 650 and pos_y == 350 or pos_x == 650 and pos_y == 300 or pos_x == 650 and pos_y == 250 or pos_x == 650 and pos_y == 200 or pos_x == 550 and pos_y == 300 or pos_x == 550 and pos_y == 250 or pos_x == 550 and pos_y == 200 or pos_x == 550 and pos_y == 150 or pos_x == 750 and pos_y == 100 or pos_x == 750 and pos_y == 150 or pos_x == 1050 and pos_y == 200 or pos_x == 1050 and pos_y == 250 or pos_x == 950 and pos_y == 350 or pos_x == 950 and pos_y == 400 or pos_x == 950 and pos_y == 450 or pos_x == 1050 and pos_y == 500 or pos_x == 850 and pos_y == 450 or pos_x == 850 and pos_y == 400 or pos_x == 850 and pos_y == 350 or pos_x == 850 and pos_y == 300 or pos_x == 750 and pos_y == 350 or pos_x == 750 and pos_y == 400 or pos_x == 750 and pos_y == 450 or pos_x == 750 and pos_y == 500 or pos_x == 650 and pos_y == 550 or pos_x == 650 and pos_y == 600 or pos_x == 650 and pos_y == 650 or pos_x == 650 and pos_y == 700 or pos_x == 450 and pos_y == 750 or pos_x == 450 and pos_y == 850 or pos_x == 450 and pos_y == 900 or pos_x == 450 and pos_y == 950 or pos_x == 550 and pos_y == 1000 or pos_x == 550 and pos_y == 1050 or pos_x == 550 and pos_y == 1100 or pos_x == 550 and pos_y == 1150 or pos_x == 550 and pos_y == 1200 or pos_x == 550 and pos_y == 1250 or pos_x == 450 and pos_y == 1250 or pos_x == 450 and pos_y == 1300 or pos_x == 450 and pos_y == 1350 or pos_x == 550 and pos_y == 1400 or pos_x == 350 and pos_y == 1350 or pos_x == 350 and pos_y == 1300 or pos_x == 350 and pos_y == 1250 or pos_x == 350 and pos_y == 1200 or pos_x == 250 and pos_y == 1250 or pos_x == 250 and pos_y == 1300 or pos_x == 250 and pos_y == 1350 or pos_x == 250 and pos_y == 1400 or pos_x == 50 and pos_y == 1350 or pos_x == 150 and pos_y == 1300 or pos_x == 150 and pos_y == 1250 or pos_x == 150 and pos_y == 120 or pos_x == 150 and pos_y == 1150 or pos_x == 450 and pos_y == 1100 or pos_x == 350 and pos_y == 1050 or pos_x == 350 and pos_y == 1000 or pos_x == 350 and pos_y == 950 or pos_x == 350 and pos_y == 900 or pos_x == 250 and pos_y == 950 or pos_x == 250 and pos_y == 1000 or pos_x == 150 and pos_y == 1050 or pos_x == 150 and pos_y == 1000 or pos_x == 150 and pos_y == 950 or pos_x == 150 and pos_y == 900 or pos_x == 150 and pos_y == 850 or pos_x == 150 and pos_y == 750 or pos_x == 150 and pos_y == 700 or pos_x == 50 and pos_y == 1100 or pos_x == 50 and pos_y == 1050 or pos_x == 50 and pos_y == 1000 or pos_x == 50 and pos_y == 950 or pos_x == 150 and pos_y == 1200 or pos_x == 350 and pos_y == 800 or pos_x == 350 and pos_y == 750 or pos_x == 350 and pos_y == 700 or pos_x == 350 and pos_y == 650 or pos_x == 550 and pos_y == 600 or pos_x == 550 and pos_y == 550 or pos_x == 550 and pos_y == 500 or pos_x == 250 and pos_y == 700 or pos_x == 250 and pos_y == 650 or pos_x == 250 and pos_y == 600 or pos_x == 250 and pos_y == 550 or pos_x == 50 and pos_y == 700 or pos_x == 50 and pos_y == 650 or pos_x == 150 and pos_y == 600 or pos_x == 150 and pos_y == 550 or pos_x == 150 and pos_y == 450 or pos_x == 350 and pos_y == 400 or pos_x == 650 and pos_y == 800 or pos_x == 650 and pos_y == 850 or pos_x == 750 and pos_y == 900 or pos_x == 750 and pos_y == 850 or pos_x == 750 and pos_y == 800 or pos_x == 750 and pos_y == 750 or pos_x == 750 and pos_y == 700 or pos_x == 750 and pos_y == 650 or pos_x == 850 and pos_y == 800 or pos_x == 850 and pos_y == 750 or pos_x == 850 and pos_y == 700 or pos_x == 850 and pos_y == 650 or pos_x == 1250 and pos_y == 700 or pos_x == 1250 and pos_y == 650 or pos_x == 1250 and pos_y == 600 or pos_x == 1250 and pos_y == 550 or pos_x == 1250 and pos_y == 500 or pos_x == 1250 and pos_y == 450 or pos_x == 1250 and pos_y == 400 or pos_x == 1250 and pos_y == 350 or pos_x == 1150 and pos_y == 500 or pos_x == 1150 and pos_y == 450 or pos_x == 1150 and pos_y == 400 or pos_x == 1150 and pos_y == 350 or pos_x == 850 and pos_y == 100 or pos_x == 850 and pos_y == 50 or pos_x == 950 and pos_y == 0 or pos_x == 950 and pos_y == 50 or pos_x == 1150 and pos_y == 50 or pos_x == 1150 and pos_y == 0 or pos_x == 1450 and pos_y == 200 or pos_x == 1450 and pos_y == 150 or pos_x == 1450 and pos_y == 100 or pos_x == 1450 and pos_y == 50 or pos_x == 1450 and pos_y == 0 or pos_x == 1150 and pos_y == 150 or pos_x == 1350 and pos_y == 200 or pos_x == 1350 and pos_y == 250 or pos_x == 1350 and pos_y == 300 or pos_x == 1350 and pos_y == 350 or pos_x == 1450 and pos_y == 500 or pos_x == 1450 and pos_y == 450 or pos_x == 1450 and pos_y == 400 or pos_x == 1450 and pos_y == 350 or pos_x == 1450 and pos_y == 300 or pos_x == 1350 and pos_y == 450 or pos_x == 1350 and pos_y == 500 or pos_x == 1350 and pos_y == 550 or pos_x == 1350 and pos_y == 650 or pos_x == 1350 and pos_y == 700 or pos_x == 1450 and pos_y == 600 or pos_x == 1450 and pos_y == 650 or pos_x == 1450 and pos_y == 700 or pos_x == 1450 and pos_y == 750 or pos_x == 1450 and pos_y == 800 or pos_x == 1450 and pos_y == 850 or pos_x == 1450 and pos_y == 900 or pos_x == 1350 and pos_y == 1000 or pos_x == 1350 and pos_y == 950 or pos_x == 1350 and pos_y == 850 or pos_x == 1350 and pos_y == 800 or pos_x == 1150 and pos_y == 750 or pos_x == 750 and pos_y == 1300 or pos_x == 750 and pos_y == 1250 or pos_x == 750 and pos_y == 120 or pos_x == 650 and pos_y == 1150 or pos_x == 650 and pos_y == 1100 or pos_x == 650 and pos_y == 1050 or pos_x == 750 and pos_y == 1000 or pos_x == 750 and pos_y == 1050 or pos_x == 850 and pos_y == 1100 or pos_x == 850 and pos_y == 1050 or pos_x == 850 and pos_y == 1000 or pos_x == 850 and pos_y == 950 or pos_x == 950 and pos_y == 900 or pos_x == 950 and pos_y == 850 or pos_x == 950 and pos_y == 750 or pos_x == 1050 and pos_y == 700 or pos_x == 1050 and pos_y == 750 or pos_x == 1050 and pos_y == 800 or pos_x == 1050 and pos_y == 850 or pos_x == 1050 and pos_y == 900 or pos_x == 1050 and pos_y == 950 or pos_x == 1050 and pos_y == 1000 or pos_x == 1050 and pos_y == 1050 or pos_x == 1050 and pos_y == 110 or pos_x == 1050 and pos_y == 1150 or pos_x == 1150 and pos_y == 1200 or pos_x == 1150 and pos_y == 1150 or pos_x == 1150 and pos_y == 1100 or pos_x == 1150 and pos_y == 1050 or pos_x == 1150 and pos_y == 1000 or pos_x == 1150 and pos_y == 950 or pos_x == 1250 and pos_y == 900 or pos_x == 1250 and pos_y == 950 or pos_x == 1250 and pos_y == 1000 or pos_x == 1250 and pos_y == 1050 or pos_x == 1450 and pos_y == 1000 or pos_x == 1450 and pos_y == 1050 or pos_x == 1450 and pos_y == 1100 or pos_x == 1450 and pos_y == 1150 or pos_x == 1450 and pos_y == 1200 or pos_x == 1450 and pos_y == 1250 or pos_x == 1450 and pos_y == 1300 or pos_x == 1450 and pos_y == 1350 or pos_x == 950 and pos_y == 1000 or pos_x == 950 and pos_y == 1050 or pos_x == 950 and pos_y == 1100 or pos_x == 950 and pos_y == 1150 or pos_x == 950 and pos_y == 1200 or pos_x == 850 and pos_y == 1250 or pos_x == 850 and pos_y == 1300 or pos_x == 850 and pos_y == 1350 or pos_x == 1150 and pos_y == 1400 or pos_x == 950 and pos_y == 1350 or pos_x == 1350 and pos_y == 1200 or pos_x == 1350 and pos_y == 1200 or pos_x == 1350 and pos_y == 1300 or pos_x == 1250 and pos_y == 1350 or pos_x == 750 and pos_y == 1200 or pos_x == 950 and pos_y == 800 or pos_x == 1050 and pos_y == 1100 or pos_x == 1350 and pos_y == 1250:
                print('Menabrak Dinding!')
                nyawa -= 1
                print('Nyawa anda sisa :', nyawa)
                if nyawa == 0:
                    print('\nGAME OVER!\n')
            elif pos_x == 1500 and pos_y == 1400:
                print('You Win!')
                pos_x += 50
            else:
                pos_x += 50
                print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
        elif key == GLUT_KEY_LEFT:
            if pos_x == 0 and pos_y == 0 or pos_x == 50 and pos_y == 50 or pos_x == 50 and pos_y == 100 or pos_x == 450 and pos_y == 200 or pos_x == 450 and pos_y == 150 or pos_x == 450 and pos_y == 50 or pos_x == 150 and pos_y == 0 or pos_x == 150 and pos_y == 150 or pos_x == 150 and pos_y == 200 or pos_x == 350 and pos_y == 250 or pos_x == 50 and pos_y == 500 or pos_x == 50 and pos_y == 450 or pos_x == 50 and pos_y == 400 or pos_x == 50 and pos_y == 350 or pos_x == 50 and pos_y == 300 or pos_x == 50 and pos_y == 250 or pos_x == 50 and pos_y == 200 or pos_x == 450 and pos_y == 350 or pos_x == 450 and pos_y == 400 or pos_x == 650 and pos_y == 350 or pos_x == 650 and pos_y == 300 or pos_x == 650 and pos_y == 250 or pos_x == 650 and pos_y == 200 or pos_x == 550 and pos_y == 250 or pos_x == 550 and pos_y == 200 or pos_x == 550 and pos_y == 150 or pos_x == 550 and pos_y == 100 or pos_x == 750 and pos_y == 150 or pos_x == 750 and pos_y == 200 or pos_x == 1050 and pos_y == 250 or pos_x == 1150 and pos_y == 500 or pos_x == 1150 and pos_y == 450 or pos_x == 1050 and pos_y == 400 or pos_x == 1150 and pos_y == 350 or pos_x == 550 and pos_y == 0 or pos_x == 850 and pos_y == 100 or pos_x == 850 and pos_y == 50 or pos_x == 950 and pos_y == 50 or pos_x == 950 and pos_y == 100 or pos_x == 1050 and pos_y == 0 or pos_x == 1150 and pos_y == 50 or pos_x == 1450 and pos_y == 200 or pos_x == 1450 and pos_y == 150 or pos_x == 1450 and pos_y == 50 or pos_x == 1250 and pos_y == 0 or pos_x == 1150 and pos_y == 150 or pos_x == 1150 and pos_y == 200 or pos_x == 1350 and pos_y == 250 or pos_x == 1350 and pos_y == 350 or pos_x == 1350 and pos_y == 400 or pos_x == 1450 and pos_y == 300 or pos_x == 1450 and pos_y == 350 or pos_x == 1450 and pos_y == 450 or pos_x == 1450 and pos_y == 500 or pos_x == 1350 and pos_y == 450 or pos_x == 1350 and pos_y == 500 or pos_x == 1350 and pos_y == 550 or pos_x == 1350 and pos_y == 600 or pos_x == 1350 and pos_y == 650 or pos_x == 1350 and pos_y == 700 or pos_x == 1450 and pos_y == 650 or pos_x == 1450 and pos_y == 700 or pos_x == 1450 and pos_y == 750 or pos_x == 1450 and pos_y == 800 or pos_x == 1450 and pos_y == 850 or pos_x == 1350 and pos_y == 1000 or pos_x == 1350 and pos_y == 950 or pos_x == 1350 and pos_y == 900 or pos_x == 1350 and pos_y == 850 or pos_x == 1150 and pos_y == 800 or pos_x == 1150 and pos_y == 750 or pos_x == 1150 and pos_y == 700 or pos_x == 1250 and pos_y == 650 or pos_x == 1250 and pos_y == 550 or pos_x == 1250 and pos_y == 500 or pos_x == 1250 and pos_y == 450 or pos_x == 1250 and pos_y == 400 or pos_x == 1250 and pos_y == 350 or pos_x == 850 and pos_y == 800 or pos_x == 850 and pos_y == 750 or pos_x == 850 and pos_y == 700 or pos_x == 850 and pos_y == 650 or pos_x == 750 and pos_y == 650 or pos_x == 750 and pos_y == 700 or pos_x == 750 and pos_y == 750 or pos_x == 750 and pos_y == 800 or pos_x == 750 and pos_y == 850 or pos_x == 550 and pos_y == 900 or pos_x == 650 and pos_y == 850 or pos_x == 950 and pos_y == 300 or pos_x == 950 and pos_y == 350 or pos_x == 950 and pos_y == 400 or pos_x == 950 and pos_y == 450 or pos_x == 850 and pos_y == 500 or pos_x == 850 and pos_y == 450 or pos_x == 850 and pos_y == 400 or pos_x == 850 and pos_y == 350 or pos_x == 750 and pos_y == 300 or pos_x == 750 and pos_y == 350 or pos_x == 750 and pos_y == 400 or pos_x == 750 and pos_y == 450 or pos_x == 650 and pos_y == 500 or pos_x == 650 and pos_y == 550 or pos_x == 650 and pos_y == 600 or pos_x == 650 and pos_y == 650 or pos_x == 450 and pos_y == 700 or pos_x == 450 and pos_y == 750 or pos_x == 450 and pos_y == 800 or pos_x == 450 and pos_y == 850 or pos_x == 450 and pos_y == 900 or pos_x == 450 and pos_y == 950 or pos_x == 450 and pos_y == 1000 or pos_x == 550 and pos_y == 1050 or pos_x == 550 and pos_y == 1100 or pos_x == 550 and pos_y == 1150 or pos_x == 450 and pos_y == 1200 or pos_x == 450 and pos_y == 1250 or pos_x == 450 and pos_y == 1300 or pos_x == 450 and pos_y == 1350 or pos_x == 350 and pos_y == 1400 or pos_x == 350 and pos_y == 1350 or pos_x == 350 and pos_y == 1300 or pos_x == 350 and pos_y == 1250 or pos_x == 250 and pos_y == 1200 or pos_x == 250 and pos_y == 1250 or pos_x == 250 and pos_y == 1300 or pos_x == 250 and pos_y == 1350 or pos_x == 50 and pos_y == 1350 or pos_x == 50 and pos_y == 1300 or pos_x == 150 and pos_y == 1250 or pos_x == 50 and pos_y == 1200 or pos_x == 150 and pos_y == 1150 or pos_x == 150 and pos_y == 1100 or pos_x == 350 and pos_y == 1050 or pos_x == 350 and pos_y == 1000 or pos_x == 350 and pos_y == 950 or pos_x == 250 and pos_y == 900 or pos_x == 250 and pos_y == 950 or pos_x == 250 and pos_y == 1000 or pos_x == 150 and pos_y == 1050 or pos_x == 150 and pos_y == 1000 or pos_x == 150 and pos_y == 950 or pos_x == 50 and pos_y == 1100 or pos_x == 50 and pos_y == 1050 or pos_x == 50 and pos_y == 1000 or pos_x == 50 and pos_y == 950 or pos_x == 50 and pos_y == 900 or pos_x == 150 and pos_y == 850 or pos_x == 50 and pos_y == 800 or pos_x == 150 and pos_y == 700 or pos_x == 150 and pos_y == 750 or pos_x == 350 and pos_y == 750 or pos_x == 350 and pos_y == 700 or pos_x == 350 and pos_y == 650 or pos_x == 350 and pos_y == 600 or pos_x == 550 and pos_y == 550 or pos_x == 250 and pos_y == 700 or pos_x == 250 and pos_y == 650 or pos_x == 250 and pos_y == 600 or pos_x == 250 and pos_y == 550 or pos_x == 50 and pos_y == 700 or pos_x == 50 and pos_y == 650 or pos_x == 50 and pos_y == 600 or pos_x == 150 and pos_y == 550 or pos_x == 150 and pos_y == 500 or pos_x == 150 and pos_y == 450 or pos_x == 150 and pos_y == 400 or pos_x == 550 and pos_y == 1250 or pos_x == 550 and pos_y == 1300 or pos_x == 750 and pos_y == 1250 or pos_x == 650 and pos_y == 1200 or pos_x == 650 and pos_y == 1150 or pos_x == 650 and pos_y == 1100 or pos_x == 650 and pos_y == 1050 or pos_x == 650 and pos_y == 1000 or pos_x == 750 and pos_y == 1050 or pos_x == 750 and pos_y == 1100 or pos_x == 850 and pos_y == 1050 or pos_x == 850 and pos_y == 1000 or pos_x == 850 and pos_y == 950 or pos_x == 850 and pos_y == 900 or pos_x == 950 and pos_y == 850 or pos_x == 950 and pos_y == 800 or pos_x == 950 and pos_y == 750 or pos_x == 950 and pos_y == 700 or pos_x == 1050 and pos_y == 750 or pos_x == 1050 and pos_y == 750 or pos_x == 1050 and pos_y == 800 or pos_x == 1050 and pos_y == 850 or pos_x == 1050 and pos_y == 900 or pos_x == 1050 and pos_y == 950 or pos_x == 1050 and pos_y == 1000 or pos_x == 1050 and pos_y == 1050 or pos_x == 1050 and pos_y == 1100 or pos_x == 1050 and pos_y == 1150 or pos_x == 1050 and pos_y == 1200 or pos_x == 1150 and pos_y == 1150 or pos_x == 1150 and pos_y == 1100 or pos_x == 1150 and pos_y == 1050 or pos_x == 1150 and pos_y == 1000 or pos_x == 1150 and pos_y == 950 or pos_x == 1150 and pos_y == 900 or pos_x == 1250 and pos_y == 950 or pos_x == 1250 and pos_y == 1000 or pos_x == 1250 and pos_y == 1050 or pos_x == 1250 and pos_y == 1100 or pos_x == 1450 and pos_y == 1000 or pos_x == 1450 and pos_y == 1000 or pos_x == 1450 and pos_y == 1050 or pos_x == 1450 and pos_y == 1150 or pos_x == 1450 and pos_y == 1200 or pos_x == 1450 and pos_y == 1250 or pos_x == 1450 and pos_y == 1300 or pos_x == 1450 and pos_y == 1350 or pos_x == 1250 and pos_y == 1400 or pos_x == 1250 and pos_y == 1350 or pos_x == 1350 and pos_y == 1250 or pos_x == 1250 and pos_y == 1200 or pos_x == 950 and pos_y == 1300 or pos_x == 950 and pos_y == 1350 or pos_x == 650 and pos_y == 1400 or pos_x == 850 and pos_y == 1350 or pos_x == 850 and pos_y == 1300 or pos_x == 850 and pos_y == 1250 or pos_x == 850 and pos_y == 1200 or pos_x == 950 and pos_y == 1150 or pos_x == 950 and pos_y == 1100 or pos_x == 950 and pos_y == 1050 or pos_x == 950 and pos_y == 1000 or pos_x == 750 and pos_y == 600:
                print('Menabrak Dinding!')
                nyawa -= 1
                print('Nyawa anda sisa :', nyawa)
            elif pos_x == 1550 and pos_y == 1400:
                print('You Win!')
            else:
                pos_x -= 50
                print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)


def update(value):
    glutPostRedisplay()
    glutTimerFunc(10, update, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(550, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Labyrinth of Three Lives")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(on_click)
    glutTimerFunc(50, update, 0)
    init()
    glutMainLoop()


main()

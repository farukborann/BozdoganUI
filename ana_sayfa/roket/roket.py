from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
from ana_sayfa.roket.objloader import *
import threading

class roket(QOpenGLWidget):
    def __init__(self, parent=None):
        super(roket, self).__init__(parent)
        self.timer = None
        self.n = 0
        self.obj = None
        self.rx, self.ry, self.rz = (0, 0, 0)
        self.tx, self.ty = (0, 0)
        self.zpos = 350

    def initializeGL(self):
        glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        self.obj = OBJ('./ana_sayfa/roket/rocket_model.obj', swapyz=True)
        self.obj.generate()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        width, height = self.width(), self.height()
        gluPerspective(90.0, width/float(height), 1, 1000.0)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)

    def update_values(self,veri):
        self.rx = float(veri.jiroskopx)  # yaw ekseni
        self.ry = float(veri.jiroskopy) # roll ekseni
        self.rz = float(veri.jiroskopz)  # pitch ekseni

        thread = threading.Thread(target=self.update)
        thread.start()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # RENDER OBJECT
        glTranslate(self.tx / 20., self.ty / 20., -self.zpos)
        glRotate(self.ry, 1, 0, 0)
        glRotate(self.rx, 0, 1, 0)
        glRotate(self.rz, 0, 0, 1)

        self.obj.render()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

import random
import os
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtCore import pyqtSlot, QTimer, QSocketNotifier, QAbstractTableModel, Qt, QVariant, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QFileDialog, QInputDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from PyQt5 import uic
#from sys import path
Ui_MainWindow = uic.loadUiType("qtcam.ui")[0]

import ximea as xi

class QtCam(QMainWindow):
    _window_title = "qtcam"
    _heartbeat = 100  # ms delay at which the plot/gui is refreshed, and the gamepad moves the stage

    def __init__(self, parent=None):
        super(QtCam, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(False)

        self.Canvas = FigureCanvas(self.fig)
        self.Canvas.setParent(self.ui.imgwidget)

        self.Canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Canvas.updateGeometry()

        l = QVBoxLayout(self.ui.imgwidget)
        l.addWidget(self.Canvas)

        self.timer = QTimer(self)
        #self.timer.timeout.connect(self.check_pad_analog)
        self.timer.start(100)

        # xi.handle_xi_error(1)
        print(xi.get_device_count())
        print(xi.get_device_info(0, 'device_name'))

        self.cam = xi.Xi_Camera(DevID=0)
        self.cam.set_debug_level("Warning")
        self.cam.set_param('exposure', 10000.0)
        # cam.set_param('limit_bandwidth',360)
        self.cam.set_param('aeag', 1)
        self.cam.set_param('exp_priority', 0)
        # cam.set_param('shutter_type',0)
        self.cam.set_binning(4)
        self.cam.set_param('width', 400)
        self.cam.set_param('height', 300)
        self.cam.set_param('offsetX', 50)
        self.cam.set_param('offsetY', 50)
        print(self.cam.get_param('framerate', float))


    @pyqtSlot()
    def imgButton_clicked(self):
        img = self.cam.get_image()
        print(img.shape)
        self.axes.implot(img)
        # self.axes.plot(self._wl, spec)
        self.Canvas.draw()




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = QtCam()
    main.show()
    sys.exit(app.exec_())
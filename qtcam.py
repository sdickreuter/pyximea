import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
import pyqtgraph as pg
from PyQt5 import uic

# from sys import path
Ui_MainWindow = uic.loadUiType("qtcam.ui")[0]

import ximea as xi


class QtCam(QMainWindow):
    _window_title = "qtcam"
    _heartbeat = 100  # ms delay at which the plot/gui is refreshed, and the gamepad moves the stage

    def __init__(self, parent=None):
        super(QtCam, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.gv = pg.GraphicsView()

        self.vb = pg.ViewBox()

        self.img = pg.ImageItem()
        self.vb.addItem(self.img)

        self.gv.setCentralWidget(self.vb)
        #self.ui.addWidget(self.gv)

        self.l = QVBoxLayout(self.ui.imgwidget)

        self.l.addWidget(self.gv)

        self.timer = QTimer(self)
        # self.timer.timeout.connect(self.check_pad_analog)
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
        self.cam.set_binning(1)
        #self.cam.set_param('width', 400)
        #self.cam.set_param('height', 300)
        #self.cam.set_param('offsetX', 50)
        #self.cam.set_param('offsetY', 50)
        self.cam.set_param('imgdataformat',2)
        print(self.cam.get_param('framerate', float))

    @pyqtSlot()
    def imgButton_clicked(self):
        img = self.cam.get_image()
        print(img.shape)
        self.img.setImage(img)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = QtCam()
    main.show()
    sys.exit(app.exec_())

import matplotlib

matplotlib.use("Qt5Agg")
import numpy as np
from PyQt5.QtCore import pyqtSlot, QTimer, QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout
import pyqtgraph as pg
from PyQt5 import uic
import time
# from sys import path
Ui_MainWindow = uic.loadUiType("qtcam.ui")[0]

import ximea as xi
#from . import ximea as xi

class CameraThread(QObject):
    ImageReadySignal = pyqtSignal(np.ndarray)
    exposure_us = 200000
    #mutex = QMutex()
    enabled = False

    def __init__(self, parent=None):
        if getattr(self.__class__, '_has_instance', False):
            RuntimeError('Cannot create another instance of Camera')
        self.__class__._has_instance = True
        self.isinitialized = False
        super(CameraThread, self).__init__(parent)
        self._cam = None
        try:
            self.abort = False
            self.thread = QThread()
            num_dev = xi.get_device_count()

            if num_dev > 0:
                print(xi.get_device_info(0, 'device_name'))

                self._cam = xi.Xi_Camera(DevID=0)
                self._cam.set_debug_level("Warning")
                self._cam.set_param('exposure', self.exposure_us)
                self._cam.set_param('aeag', 0)
                self._cam.set_param('exp_priority', 0)
                #self._cam.set_binning(2, skipping=False)
                self._cam.set_param('imgdataformat',6)
                #self._cam.set_param('buffers_queue_size',1)
                self._cam.get_image()

                self.thread.started.connect(self.process)
                self.thread.finished.connect(self.stop)
                self.moveToThread(self.thread)
                self.isinitialized = True
        except:
            (type, value, traceback) = sys.exc_info()
            sys.excepthook(type, value, traceback)

    def __del__(self):
        self.abort = True
        self.__class__.has_instance = False
        try:
            if not self._cam is None:
                self._cam.close()
            self.ImageReadySignal.disconnect()
        except TypeError as e:
            print(e)

    def set_exposure(self, us):
        self.exposure_us = us
        self._cam.set_param('exposure', us)

    def get_exposure(self):
        us = self._cam.get_param('exposure')
        return us

    def start(self):
        self.thread.start()

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    @pyqtSlot()
    def stop(self):
        self.abort = True

    def work(self):
        if self.enabled:
            self.ImageReadySignal.emit(self._cam.get_image())

    @pyqtSlot()
    def process(self):
        while not self.abort:
            try:
                t = self.exposure_us / 1e6
                if t > 0.1 :
                    time.sleep(t)
                else:
                    time.sleep(0.1)
                self.work()
            except:
                (type, value, traceback) = sys.exc_info()
                sys.excepthook(type, value, traceback)
        #self._cam.stop_aquisition()



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

        self.l = QGridLayout(self.ui.imgwidget)
        self.l.setSpacing(0)
        self.l.addWidget(self.gv)

        self.w = pg.HistogramLUTWidget()
        self.l.addWidget(self.w, 0, 1)
        self.w.setImageItem(self.img)
        #self.w.setDisabled(True)

        try:
            self.cam = CameraThread()
        except:
            print("Error initializing Camera")
        if self.cam.isinitialized:
            self.cam.set_exposure(200 * 1000)
            self.cam.ImageReadySignal.connect(self.update_camera)
            self.cam.start()
        else:
            self.cam = None
            # self.ui.left_tab.setEnabled(False)
            print("Could not initialize Camera")
            self.ui.Quit()


    @pyqtSlot()
    def imgButton_clicked(self):
        if self.cam.is_enabled():
            self.cam.disable()
        else:
            self.cam.enable()

    @pyqtSlot(np.ndarray)
    def update_camera(self, img):
        #plow, phigh = np.percentile(img, (1, 99))
        #img = exposure.rescale_intensity(img, in_range=(plow, phigh))
        self.img.setImage(img, autoLevels=True, autoDownsample=True)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main = QtCam()
    main.show()
    sys.exit(app.exec_())

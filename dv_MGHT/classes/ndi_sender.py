from __future__ import annotations
import numpy as np
import NDIlib as ndi
from PySide6 import QtCore, QtWidgets, QtGui

class NDISender():
    color_format = QtGui.QImage.Format_ARGB32
    fourCC = ndi.FOURCC_VIDEO_TYPE_BGRA

    def __init__(
        self,
        widget: QWidget,
        interval: int | None = None,
        framerate: int | None = None
    ):
        self._widget = widget
        self._widget.adjustSize()
        self._widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self._timer = QtCore.QTimer()
        self._interval: int # Interval between frame updates

        if interval != None:    # Respect a set interval if provided
            self._interval = interval
        elif framerate != None: # Check if framerate is declared instead
            self._interval = int( 1000 / framerate )
        else:                   # Default to 1 second otherwise
            self._interval = 1000

        if not ndi.initialize():
            raise RuntimeError("NDI failed to initialize.")

        self.settings = ndi.SendCreate()
        self.settings.ndi_name = "dv_MGHT Games Board"

        self.sender = ndi.send_create(self.settings)

        self._timer.timeout.connect(self.send_frame)

        self.send_frame()
        self._timer.start(self._interval)

    def send_frame(self) -> None:

        if self._widget.width() <= 0 or self._widget.height() <= 0:
            return

        image = QtGui.QImage(
            self._widget.width(),
            self._widget.height(),
            self.color_format
        )

        image.fill(QtCore.Qt.transparent)

        painter = QtGui.QPainter(image)
        #painter.begin(self._widget)
        painter.end()
        self._widget.render(image)

        ptr = np.array(image.bits(), dtype=np.uint8)
        ptr = ptr.reshape(image.height(), image.width(), 4)

        frame = ndi.VideoFrameV2()
        frame.FourCC = self.fourCC
        frame.data = ptr

        ndi.send_send_video_v2(
            self.sender,
            frame
        )
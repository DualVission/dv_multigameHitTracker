from __future__ import annotations

from PySide6.QtGui import QPainter, QColor, QPixmap, QImage
from PySide6.QtWidgets import QGraphicsEffect
from PySide6.QtCore import QPoint, Qt

class MultiplyEffect(QGraphicsEffect):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__color = QColor()
        self.__image = QImage()

    def color(self) -> QColor:
        return self.__color

    def setColor(self, other: QColor) -> None:
        self.__color = other

    def image(self) -> QImage:
        return self.__image

    def setImage(self, other: QImage) -> None:
        self.__image = other

    def draw(self, painter):
        offset = QPoint(0, 0)
        pixmap = self.sourcePixmap(Qt.LogicalCoordinates, offset)
        rect = pixmap.rect()
        img = self.image().convertToFormat(QImage.Format.Format_ARGB32_Premultiplied)

        p = QPainter(img)
        p.setCompositionMode(QPainter.CompositionMode_SourceIn)
        p.fillRect(img.rect(), self.color())
        p.end()

        #painter.drawPixmap(rect, pixmap)
        #painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
        painter.drawImage(rect, img)


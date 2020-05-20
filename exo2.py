from PySide2.QtWidgets import *
from random import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.layout = QHBoxLayout()
        self.PBar=QProgressBar()
        self.Slider=QSlider()
        self.layout.addWidget(self.PBar)
        self.layout.addWidget(self.Slider)

        self.Slider.valueChanged.connect(self.ChangementSlider)

        self.setLayout(self.layout)

    def ChangementSlider(self):
        val = self.Slider.value()
        self.PBar.setValue(val)


if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()

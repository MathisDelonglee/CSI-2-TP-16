from PySide2.QtWidgets import *
from random import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.QLabel = QLabel("CSI")
        self.button = QPushButton('Changer de cycle')
        self.layout.addWidget(self.QLabel)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.buttonCliqued)

        self.setLayout(self.layout)

    def buttonCliqued(self):
        l = ["CSI","CIR","BIOST","CENT","BIAST","EST"]
        a = randint(0,5)
        self.QLabel.setText(l[a])


if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()

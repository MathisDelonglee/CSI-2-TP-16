from PySide2.QtWidgets import *
from random import *

class IHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(600,400)
        self.layout = QVBoxLayout()
        self.button = QPushButton('Changer mon texte')
        self.layout.addWidget(self.button)
        self.Text = QTextEdit()
        self.layout.addWidget(self.Text)
        self.Text.setText("Le nombre de clics va être affiché ici")

        self.clic = 0
        self.button.clicked.connect(self.buttonCliqued)

        self.setLayout(self.layout)

    def buttonCliqued(self):
        #self.close()
        self.clic += 1
        self.button.setText("Clic "+str(self.clic))
        self.Text.setText("Clic "+str(self.clic))



if __name__ == "__main__":
   app = QApplication([])
   ihm = IHM()
   ihm.show()
   app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon



class Dialouge(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'File Name'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

    def initUI(self):
        """
        initializes the dialogue box and returns the user input as string
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #print(self.getText())
        return self.getText()


    def getText(self):
        text, okPressed = QInputDialog.getText(self, "File Name", "File Name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            return text


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dialouge()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()





    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec_())





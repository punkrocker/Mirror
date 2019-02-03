import sys
from PyQt5 import QtGui


def window():
    app = QtGui.QGuiApplication(sys.argv)
    w = QtGui.QWindow()
    w.setWidth(600)
    w.setHeight(600)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()

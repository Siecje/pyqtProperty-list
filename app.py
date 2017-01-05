import sys

from PyQt5 import QtCore, QtQml
from PyQt5.QtWidgets import QApplication


class CustomType(QtCore.QObject):
    names_changed = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(CustomType, self).__init__(parent)

        self._names = []

    @QtCore.pyqtProperty(QtQml.QQmlListProperty, notify = names_changed)
    def names(self):
        return QtQml.QQmlListProperty(str, self, self._names)
    @names.setter
    def names(self, names):
        print('here1')
        if names == self.names:
            print('here2')
            return
        print('here3')
        self._names = names
        print('here4')
        self.names_changed.emit()
        print('here5')
        print('============\n')


app = QApplication(sys.argv)
QtQml.qmlRegisterType(CustomType, 'CustomType', 1, 0, 'CustomType')
engine = QtQml.QQmlApplicationEngine("App.qml")
app.exec_()

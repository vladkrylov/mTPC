import os

from subprocess import call

def substitute(file_path, str_what, str_by):
    with open(file_path, 'r') as pyform:
        content = pyform.read()
        content = content.replace(str_what, str_by)
    with open(file_path, 'w') as pyform:
        pyform.write(content)


def subs_icons_path(pyform_file):
    substitute(pyform_file, 'addPixmap(QtGui.QPixmap("img/', 'addPixmap(QtGui.QPixmap("view/img/')


def add_matplotlib_widget_import(pyform_file):
    str_to_find = "from PyQt5 import QtCore, QtGui, QtWidgets"
    str_substit = "%s\nfrom axes import MyStaticMplCanvas" % str_to_find
    substitute(pyform_file, str_to_find, str_substit)


def add_matplotlib_widget(pyform_file):
    substitute(pyform_file, "self.plotWidget = QtWidgets.QWidget(self.centralwidget)", "self.plotWidget = PlotCanvas(self.centralwidget)")


if __name__ == "__main__":
    qtform_file = "mainwindow.ui"
    pyform_file = "mainwindow.py"
    qt2py_command = "pyuic5 -x %s -o %s" % (qtform_file, pyform_file)
    call(qt2py_command.split())

    add_matplotlib_widget_import(pyform_file)
    add_matplotlib_widget(pyform_file)
    subs_icons_path(pyform_file)



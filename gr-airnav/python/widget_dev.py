#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class RadioFreqDisp(QtGui.QWidget):

    def __init__(self, label = '', parent = None):
        super(RadioFreqDisp, self).__init__(parent)
        self.label = label
        self.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        self.initUI()

    def setFreq(self, value):
        self.freq_display.display(value)

    def getFreq(self):
        self.freq_display.value()

    def initUI(self):

        self.grid = QtGui.QGridLayout()

        self.gothic_font = QtGui.QFont('News Gothic')

        self.freq_display = QtGui.QLCDNumber(6)
        lcd_font = self.freq_display.font()
        lcd_font.setPointSize(12)
        self.freq_display.setFont(lcd_font)
        self.freq_display.display('{:6.2f}'.format(118.00))
        self.freq_display.setSegmentStyle(QtGui.QLCDNumber.Flat)
        lcd_pal = self.freq_display.palette()
        lcd_pal.setColor(lcd_pal.WindowText, QtGui.QColor(255, 0, 0))
        lcd_pal.setColor(lcd_pal.Window, QtGui.QColor(0, 0, 0))
        self.freq_display.setPalette(lcd_pal)
        self.freq_display.resize(800, 300)
        self.freq_display.setFrameStyle(QtGui.QFrame.NoFrame)

        self.freq_label = QtGui.QLabel(self.label)
        self.freq_label.setFont(self.gothic_font)
        lbl_pal = self.freq_label.palette()
        lbl_pal.setColor(lbl_pal.WindowText, QtGui.QColor(255, 255, 255))
        lbl_pal.setColor(lbl_pal.Window, QtGui.QColor(0, 0, 0))
        self.freq_label.setPalette(lbl_pal)

        self.grid.addWidget(self.freq_display, 0, 0)
        self.grid.addWidget(self.freq_label, 1, 0)
        self.grid.setAlignment(self.freq_label, QtCore.Qt.AlignHCenter)
        self.setLayout(self.grid)
        self.adjustSize()

class Radio(QtGui.QWidget):

    def __init__(self, parent = None):
        super(Radio, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.grid = QtGui.QGridLayout()

        self.stby = RadioFreqDisp('STBY')
        self.actv = RadioFreqDisp('ACTV')

        self.grid.addWidget(self.actv, 0, 0)
        self.grid.addWidget(self.stby, 0, 1)
        self.setLayout(self.grid)
        self.adjustSize()

    #     cb = QtGui.QCheckBox('Show title', self)
    #     cb.move(20, 20)
    #     cb.toggle()
    #     cb.stateChanged.connect(self.changeTitle)
    #
    #     self.setGeometry(300, 300, 250, 150)
    #     self.setWindowTitle('QtGui.QCheckBox')
    #     self.show()
    #
    # def changeTitle(self, state):
    #
    #     if state == QtCore.Qt.Checked:
    #         self.setWindowTitle('QtGui.QCheckBox')
    #     else:
    #         self.setWindowTitle('')

def main():

    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    window.setWindowTitle("Radio Stack")
    win_pal = window.palette()
    win_pal.setColor(win_pal.Window, QtGui.QColor(0, 0, 0))
    window.setPalette(win_pal)
    ex = Radio(parent=window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

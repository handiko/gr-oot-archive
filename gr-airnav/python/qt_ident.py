#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
import pmt
from PyQt4 import Qt, QtCore, QtGui
from gnuradio import gr

class qt_ident(gr.sync_block, QtGui.QWidget):
    """
    docstring for block qt_ident
    """
    def __init__(self):
        gr.sync_block.__init__(self, name="qt_ident", in_sig=[], out_sig=[])
        QtGui.QWidget.__init__(self)
        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handler)
        self.initUI()

    def initUI(self):
        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(2)

        self.label_font = QtGui.QFont()
        self.label_font.setWeight(QtGui.QFont.Bold)
        self.ident = Qt.QLabel('')
        self.ident_label = QtGui.QLabel('Ident:')
        self.ident_label.setFont(self.label_font)
        # self.ident.setStyleSheet("QLabel { background-color : black; color : white; }")

        self.grid.addWidget(self.ident_label, 0, 0)
        self.grid.addWidget(self.ident, 0, 1)

        self.setLayout(self.grid)

    def handler(self, ident_msg):
        self.ident.setText(pmt.to_python(ident_msg))
        # msg_type = pmt.to_long(pmt.tuple_ref(rds_data, 0))
        # msg = pmt.symbol_to_string(pmt.tuple_ref(rds_data, 1))
        # msg = msg.strip()
        # if msg_type == 0:
        #     if self.program_info.text() != callsign(msg):
        #         self.program_info.setText(callsign(msg))
        # elif msg_type == 1:
        #     if self.station_name.text() != msg:
        #         self.station_name.setText(msg)
        # elif msg_type == 4:
        #     if self.station_name.text() != msg:
        #         self.radio_text.setText(msg)
        # elif msg_type == 3:
        #     self.flags.update(msg)

    def work(self, input_items, output_items):
        pass

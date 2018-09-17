#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
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

import numpy as np
from gnuradio import gr
import pmt

class ax25_protocol_encode(gr.basic_block):
    """
    docstring for block ax25_protocol_encode
    """
    def __init__(self, dcall="CQ", scall="", shift_call=True, control=0x03):
        gr.basic_block.__init__(self,
            name="ax25_protocol_encode",
            in_sig=None,
            out_sig=None)

        self.shift_callsign = shift_call
        if self.shift_callsign:
            print "Callsign shifting enabled"
        self.message_port_register_out(pmt.intern("out"))
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern("in"), self.handle_message)
        self.control_byte = control

        self.dest_callsign = self.left_shift_call(dcall.ljust(6))
        self.source_callsign = self.left_shift_call(scall.ljust(6))
        print self.dest_callsign

    def handle_message(self, msg):
        payload = np.concatenate((self.dest_callsign,
            np.array([0x60], dtype=np.uint8),
            self.source_callsign,
            np.array([0x68, self.control_byte, 0xF0], dtype=np.uint8),
            np.fromstring(pmt.symbol_to_string(msg), dtype=np.uint8)))

        self.message_port_pub(pmt.intern("out"), pmt.cons(pmt.to_pmt(len(payload)),
            pmt.to_pmt(payload)))

    def left_shift_call(self, call):
        tmp = np.fromstring(call, dtype=np.uint8)
        if self.shift_callsign:
            for char in np.nditer(tmp, op_flags=['readwrite']):
                char[...] = (char << 1)

        return tmp

    def forecast(self, noutput_items, ninput_items_required):
        return 0

    def general_work(self, input_items, output_items):
        return len(output_items[0])

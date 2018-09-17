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

from gnuradio import analog
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
import igate
import math

class aprs_demod(gr.hier_block2):
    """
    docstring for block aprs_demod
    """
    def __init__(self, samp_rate):
        gr.hier_block2.__init__(self,
            "APRS demod",
            gr.io_signature(1, 1, gr.sizeof_float),
            gr.io_signature(0, 0, 0),
        )
        self.message_port_register_hier_out("out")

        self.samp_rate = samp_rate
        self.bit_rate = 1200

        taps = firdes.low_pass(1, self.samp_rate, 1200, 200)
        self.afsk_shift = filter.freq_xlating_fir_filter_fcc(1, taps, (1200+2200)/2, self.samp_rate)

        self.afsk_demod = analog.quadrature_demod_cf(1.0) # Don't care about gain just before binary slicer
        self.threashold = digital.binary_slicer_fb()
        self.clock_rec = igate.clock_recovery_timer_bb(self.samp_rate/self.bit_rate)
        self.diff_decode = digital.diff_decoder_bb(2)
        self.negate = digital.map_bb(([1,0]))
        self.packetizer = digital.hdlc_deframer_bp(16, 1024)
        self.parser = igate.aprs_decode_frame()

        self.connect((self, 0), (self.afsk_shift, 0))
        self.connect((self.afsk_shift, 0), (self.afsk_demod, 0))
        self.connect((self.afsk_demod, 0), (self.threashold, 0))
        self.connect((self.threashold, 0), (self.clock_rec, 0))
        self.connect((self.clock_rec, 0), (self.diff_decode, 0))
        self.connect((self.diff_decode, 0), (self.negate, 0))
        self.connect((self.negate, 0), (self.packetizer, 0))
        self.msg_connect((self.packetizer, 'out'), (self.parser, 'in'))
        self.msg_connect((self.parser, 'out'), (self, 'out'))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        taps = firdes.low_pass(1, self.samp_rate, 1200, 200)
        self.afsk_shift.set_taps(taps)

    def get_bit_rate(self):
        return self.bit_rate

    def set_bit_rate(self, bit_rate):
        self.bit_rate = bit_rate

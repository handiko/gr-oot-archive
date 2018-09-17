#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Daniel Estevez <daniel@destevez.net>.
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

import numpy
from gnuradio import gr
import collections
import pmt
import array

import hdlc

def pack(s):
    d = bytearray()
    for i in range(0, len(s), 8):
        x = 0
        for j in range(7,-1,-1): # LSB first
            x <<= 1
            x += s[i+j]
        d.append(x)
    return d

def fcs_ok(frame):
    if len(frame) <= 2: return False
    crc = hdlc.crc_ccitt(frame[:-2])
    return frame[-2] == (crc & 0xff) and frame[-1] == ((crc >> 8) & 0xff)

class hdlc_deframer(gr.sync_block):
    """
    docstring for block hdlc_deframer
    """
    def __init__(self, check_fcs, max_length):
        gr.sync_block.__init__(self,
            name="hdlc_deframer",
            in_sig=[numpy.uint8],
            out_sig=None)

        self.bits = collections.deque(maxlen = (max_length+2)*8 + 7)
        self.ones = 0 # consecutive ones for flag checking
        self.check = check_fcs

        self.message_port_register_out(pmt.intern('out'))

    def work(self, input_items, output_items):
        in0 = input_items[0]

        for x in in0:
            if x:
                self.ones += 1
                self.bits.append(x)
            else:
                if self.ones == 5:
                    # destuff = do nothing
                    None
                elif self.ones > 5: # should be ones == 6 unless packet is corrupted
                    # flag received
                    # prepare to send frame
                    for _ in range(min(7, len(self.bits))):
                                   self.bits.pop() # remove 7 previous flag bits
                    if len(self.bits) % 8:
                        # pad on the left with 0's
                        self.bits.extendleft([0] * (8 - len(self.bits) % 8))
                    frame = pack(self.bits)
                    self.bits.clear()
                    if frame and (not self.check or fcs_ok(frame)):
                        # send frame
                        buff = array.array('B', frame[:-2]) # trim fcs
                        self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.PMT_NIL, pmt.init_u8vector(len(buff), buff)))
                else:
                    self.bits.append(x)
                self.ones = 0
                
        return len(input_items[0])


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

class bell_202_modem(gr.interp_block):
    """
    docstring for block bell_202_modem
    """
    def __init__(self, samp_rate=38400, baud=1200):
        gr.interp_block.__init__(self,
            name="Bell 202 Modem",
            in_sig=[np.uint8],
            out_sig=[np.float32],
            interp = 32
        )

        if (samp_rate % baud) != 0:
            print "ERROR: Baud rate needs to be multiple of sample rate."
            return -1

        self.sample_rate = samp_rate
        self.baud_rate = baud
        self.last_freq = 0
        self.last_phase = 0
        self.last_w = 0

    def work(self, input_items, output_items):
        num_samples = 32 * len(input_items[0])

        for j in range(0,len(input_items[0])):
            if input_items[0][j] > 0:
                freq = 1200.0
            else:
                freq = 2200.0

            x = np.arange((j * 32), ((j + 1) * 32))
            w = (2 * np.pi * freq / self.sample_rate)
            phase = ((j * 32) - 1) * (self.last_w - w) + self.last_phase
            values = np.sin((w * x) + phase)

            self.last_freq = freq
            self.last_phase = phase
            self.last_w = w

            output_items[0][(j * 32):((j + 1) * 32)] = values

        return len(output_items[0])

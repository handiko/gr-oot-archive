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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from bell_202_modem import bell_202_modem
import numpy as np

class qa_bell_202_modem (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (0, 1)
        # calculation is np.sin((w * x) + phase)
        # w = w = (2 * np.pi * freq / sample_rate)
        # phase = ((j * 32) - 1) * (last_w - w) + last_phase
        # First calculation is for freq=2200
        expected_result1 = np.sin((0.359974158224 * np.arange(0, 32)) + 0.359974158224)
        # Second is for 1200
        expected_result2 = np.sin((0.196349540849 * np.arange(32, 64)) + 5.43233729683)
        # Concatenate arrays
        expected_result = np.concatenate([expected_result1, expected_result2])

        src = blocks.vector_source_b(src_data)
        but = bell_202_modem(38400, 1200)
        snk = blocks.vector_sink_f()

        self.tb.connect(src, but)
        self.tb.connect(but, snk)

        self.tb.run ()

        # check data
        result = snk.data()

        # Check for correct values
        self.assertFloatTuplesAlmostEqual(result, expected_result, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_bell_202_modem, "qa_bell_202_modem.xml")

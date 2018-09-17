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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import pmt
from aprs_info_filter import aprs_info_filter

class qa_aprs_info_filter (gr_unittest.TestCase):

    def setUp (self):
        self.msglog = []

    def tearDown (self):
        pass

    def _recv_msg (self, port, msg):
        """For monkey-patching message_port_pub in SUT"""
        self.msglog.append( (pmt.to_python(port), pmt.to_python(msg)) )

    def test_001_non_dict (self):
        sut = aprs_info_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt("A string, not a dict"))

        self.assertEquals(self.msglog, [])

    def test_002_missing_index (self):
        sut = aprs_info_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt({
            "src": "Source"
            # No path
        }))

        self.assertEquals(self.msglog, [])

    def test_003_not_matching (self):
        sut = aprs_info_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt({
            "info": "don't skip"
        }))

        self.assertEquals(self.msglog, [
                ('out', {
                    "info": "don't skip"
                })
            ])

    def test_004_matching (self):
        sut = aprs_info_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt({
            "info": "skip"
        }))

        self.assertEquals(self.msglog, [])

if __name__ == '__main__':
    gr_unittest.run(qa_aprs_info_filter, "qa_aprs_info_filter.xml")

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
from aprs_append_path import aprs_append_path

class qa_aprs_append_path (gr_unittest.TestCase):

    def setUp (self):
        self.msglog = []

    def tearDown (self):
        pass

    def _recv_msg (self, port, msg):
        """For monkey-patching message_port_pub in SUT"""
        self.msglog.append( (pmt.to_python(port), pmt.to_python(msg)) )

    def test_001_non_dict (self):
        dst = aprs_append_path("")
        dst.message_port_pub = self._recv_msg

        dst._handle_msg(pmt.to_pmt("A string, not a dict"))

        self.assertEquals(self.msglog, [])

    def test_002_missing_index (self):
        dst = aprs_append_path("")
        dst.message_port_pub = self._recv_msg

        dst._handle_msg(pmt.to_pmt({
            "src": "Source"
            # No path
        }))

        self.assertEquals(self.msglog, [])

    def test_003_empty_append_path_empty_path (self):
        dst = aprs_append_path("")
        dst.message_port_pub = self._recv_msg

        dst._handle_msg(pmt.to_pmt({
            "path": []
        }))

        self.assertEquals(self.msglog, [
                ('out', {
                "path": []
                })
            ])

    def test_004_append_path (self):
        dst = aprs_append_path("qAR,TEST-3")
        dst.message_port_pub = self._recv_msg

        dst._handle_msg(pmt.to_pmt({
            "path": ['ME-5*']
        }))

        self.assertEquals(self.msglog, [
                ('out', {
                "path": ['ME-5*', 'qAR', 'TEST-3']
                })
            ])

if __name__ == '__main__':
    gr_unittest.run(qa_aprs_append_path, "qa_aprs_append_path.xml")

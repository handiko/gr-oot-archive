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
import pmt
from aprs_path_filter import aprs_path_filter

class qa_aprs_path_filter (gr_unittest.TestCase):

    def setUp (self):
        self.msglog = []

    def tearDown (self):
        pass

    def _recv_msg (self, port, msg):
        """For monkey-patching message_port_pub in SUT"""
        self.msglog.append( pmt.to_python(msg) )
    
    def _add_testmsg(self, sut):
        msgs = [
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'match'   },
            {'dst': 'match',   'info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['match',      'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'match'     ],'src': 'call_src'}
            ]
        for msg in msgs:
            sut._handle_msg(pmt.to_pmt(msg))

    def test_001_non_dict (self):
        sut = aprs_path_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt("A string, not a dict"))

        self.assertEquals(self.msglog, [])

    def test_002_missing_index (self):
        sut = aprs_path_filter("^(?!skip)")
        sut.message_port_pub = self._recv_msg

        sut._handle_msg(pmt.to_pmt({
            "src": "Source"
            # No path
        }))

        self.assertEquals(self.msglog, [])

    def test_003_exclude_nodst (self):
        sut = aprs_path_filter("^match$", True, False)
        sut.message_port_pub = self._recv_msg
        self._add_testmsg(sut)

        self.assertEquals(self.msglog, [
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'match'   },
            {'dst': 'match',   'info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'}
            ])

    def test_004_include_nodst (self):
        sut = aprs_path_filter("^match$", False, False)
        sut.message_port_pub = self._recv_msg
        self._add_testmsg(sut)

        self.assertEquals(self.msglog, [
            {'dst': 'call_dst','info': 'info','path': ['match',      'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'match'     ],'src': 'call_src'}
            ])

    def test_005_exclude_includedst (self):
        sut = aprs_path_filter("^match$", True, True)
        sut.message_port_pub = self._recv_msg
        self._add_testmsg(sut)

        self.assertEquals(self.msglog, [
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'call_path2'],'src': 'match'   }
            ])

    def test_006_include_includedst (self):
        sut = aprs_path_filter("^match$", False, True)
        sut.message_port_pub = self._recv_msg
        self._add_testmsg(sut)

        self.assertEquals(self.msglog, [
            {'dst': 'match',   'info': 'info','path': ['call_path1', 'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['match',      'call_path2'],'src': 'call_src'},
            {'dst': 'call_dst','info': 'info','path': ['call_path1', 'match'     ],'src': 'call_src'}
            ])


if __name__ == '__main__':
    gr_unittest.run(qa_aprs_path_filter, "qa_aprs_path_filter.xml")

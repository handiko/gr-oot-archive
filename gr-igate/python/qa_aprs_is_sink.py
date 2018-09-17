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
from aprs_is_sink import aprs_is_sink

class qa_aprs_is_sink (gr_unittest.TestCase):

    def setUp (self):
        self._last_msg = None

    def tearDown (self):
        pass
    
    def _send(self, msg):
        self._last_msg = msg

    def test_001_simple_pack (self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        stimuli = {
            'src': 'DST2ZZ-3',
            'dst': 'SRC1ZZ-13',
            'path': ['MID1-5*', 'MID2-2'],
            'info': 'stuff'
        }
        expect = "DST2ZZ-3>SRC1ZZ-13,MID1-5*,MID2-2:stuff"
        
        sut._handle_msg(pmt.to_pmt(stimuli))
        self.assertEquals(self._last_msg, expect)

    def test_002_trim_first_line_LF (self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        stimuli = {
            'src': 'DST2ZZ-3',
            'dst': 'SRC1ZZ-13',
            'path': ['MID1-5*', 'MID2-2'],
            'info': 'stuff and stuff\nboll'
        }
        expect = "DST2ZZ-3>SRC1ZZ-13,MID1-5*,MID2-2:stuff and stuff"
        
        sut._handle_msg(pmt.to_pmt(stimuli))
        self.assertEquals(self._last_msg, expect)

    def test_003_trim_first_line_CR (self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        stimuli = {
            'src': 'DST2ZZ-3',
            'dst': 'SRC1ZZ-13',
            'path': ['MID1-5*', 'MID2-2'],
            'info': 'stuff and stuff\rboll'
        }
        expect = "DST2ZZ-3>SRC1ZZ-13,MID1-5*,MID2-2:stuff and stuff"
        
        sut._handle_msg(pmt.to_pmt(stimuli))
        self.assertEquals(self._last_msg, expect)
        
    def test_004_binary_safe (self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        info_bin = range(256)
        info_bin.remove(ord('\n')) # Linebreaks will be removed, se above
        info_bin.remove(ord('\r')) # Linebreaks will be removed, se above
        info = "".join([chr(c) for c in info_bin])
        stimuli = {
            'src': 'DST2ZZ-3',
            'dst': 'SRC1ZZ-13',
            'path': ['MID1-5*', 'MID2-2'],
            'info': info
        }
        expect = "DST2ZZ-3>SRC1ZZ-13,MID1-5*,MID2-2:"+info
        
        sut._handle_msg(pmt.to_pmt(stimuli))
        self.assertEquals(self._last_msg, expect)
    
    def test_005_login(self):
        sut = aprs_is_sink(None, None, 'CALL', 12345)
        sut._send = self._send # Monkey patch so we can verify
        
        sut._login()
        self.assertEquals(self._last_msg, 'user CALL pass 12345')

    
    def test_006_login_appname(self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        sut._login()
        self.assertEquals(self._last_msg, 'user CALL pass 12345 vers app unknown')

    
    def test_007_login_appname_appvers(self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app', 'vers')
        sut._send = self._send # Monkey patch so we can verify
        
        sut._login()
        self.assertEquals(self._last_msg, 'user CALL pass 12345 vers app vers')

    def test_008_info_dont_trim (self):
        sut = aprs_is_sink(None, None, 'CALL', 12345, 'app')
        sut._send = self._send # Monkey patch so we can verify
        
        stimuli = {
            'src': 'DST2ZZ-3',
            'dst': 'SRC1ZZ-13',
            'path': ['MID1-5*', 'MID2-2'],
            'info': 'stuff '
        }
        expect = "DST2ZZ-3>SRC1ZZ-13,MID1-5*,MID2-2:stuff "

if __name__ == '__main__':
    gr_unittest.run(qa_aprs_is_sink, "qa_aprs_is_sink.xml")

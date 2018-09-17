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
from aprs_decode_frame import ax25_parse

def pack_call(call, ssid, been_repeated=False, end=False):
    call += "       "
    return [
        ord(call[0])<<1,
        ord(call[1])<<1,
        ord(call[2])<<1,
        ord(call[3])<<1,
        ord(call[4])<<1,
        ord(call[5])<<1,
        0x60 | (0x80 if been_repeated else 0) | (ssid<<1) | (1 if end else 0)
        ]

def combine(*parts):
    out = ""
    for part in parts:
        if type(part) == str:
            out += part
        if type(part) == list:
            out += "".join([chr(c) for c in part])
    return out

basic_header = combine(
    pack_call("SRC1ZZ", 13, False, False), # source
    pack_call("DST2ZZ", 3, False, False), # destination
    pack_call("MID1", 5, True, False), # path
    pack_call("MID2", 2, False, True),
    [0x03], # control field
    [0xf0] # protocol id
    )

class qa_aprs_decode_frame (gr_unittest.TestCase):

    def setUp (self):
        self.msglog = []

    def tearDown (self):
        pass

    def test_001_invalid_data (self):
        stimuli = combine("boll")
        expect = None
        
        self.assertEquals(ax25_parse(stimuli), expect)

    def test_002_unpack (self):
        stimuli = combine(basic_header, "stuff")
        expect = {
            'dst': 'SRC1ZZ-13',
            'src': 'DST2ZZ-3',
            'path': ['MID1-5*', 'MID2-2'],
            'ctrl': 0x03,
            'pid': 0xf0,
            'info': 'stuff'
        }
        
        self.assertEquals(ax25_parse(stimuli), expect)

    def test_003_dont_trim (self):
        """
        Don't trim info field. Keep it intact.
        """
        stimuli = combine(basic_header, "  st  uf  f  ")
        expect = {
            'dst': 'SRC1ZZ-13',
            'src': 'DST2ZZ-3',
            'path': ['MID1-5*', 'MID2-2'],
            'ctrl': 0x03,
            'pid': 0xf0,
            'info': '  st  uf  f  '
        }
        
        self.assertEquals(ax25_parse(stimuli), expect)

    def test_004_accept_binary (self):
        """
        Should accept all binary values
        """
        stimuli = combine(basic_header, range(256))
        expect = {
            'dst': 'SRC1ZZ-13',
            'src': 'DST2ZZ-3',
            'path': ['MID1-5*', 'MID2-2'],
            'ctrl': 0x03,
            'pid': 0xf0,
            'info': "".join([chr(c) for c in range(256)])
        }
        
        self.assertEquals(ax25_parse(stimuli), expect)


if __name__ == '__main__':
    gr_unittest.run(qa_aprs_decode_frame, "qa_aprs_decode_frame.xml")

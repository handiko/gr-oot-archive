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

from gnuradio import gr
import pmt
import re
from lib2to3.pytree import generate_matches

class aprs_path_filter(gr.sync_block):
    """
    docstring for block aprs_path_filter
    """
    def __init__(self, regexp, exclude=True, include_dst=False):
        gr.sync_block.__init__(self,
            name="aprs_path_filter",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))

        self.d_regexp = re.compile(regexp)
        self.d_exclude = exclude
        self.d_include_dst = include_dst

        self.set_msg_handler(pmt.intern('in'), self._handle_msg)

    def _handle_msg(self, msg_pmt):
        pkt = pmt.to_python(msg_pmt)
        try:
            if self._matches(pkt):
                self.message_port_pub(pmt.intern('out'), pmt.to_pmt(pkt))
        except Exception as e:
            # TODO: Error handling, but for now, just output the error
            print "aprs_info_filter error:", e
            print "original message:", pkt
    
    def _matches(self, pkt):
        matches = False
        if self.d_include_dst:
            if self.d_regexp.match(pkt['dst']):
                matches |= True
        for pathelem in pkt['path']:
            if self.d_regexp.match(pathelem):
                matches |= True
        if self.d_exclude:
            return not matches
        return matches
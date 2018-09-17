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

from gnuradio import gr
import pmt
import re

class aprs_info_filter(gr.sync_block):
    """
    docstring for block aprs_info_filter
    """
    def __init__(self, regexp):
        gr.sync_block.__init__(self,
            name="aprs_info_filter",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))

        self.d_regexp = re.compile(regexp)

        self.set_msg_handler(pmt.intern('in'), self._handle_msg)

    def _handle_msg(self, msg_pmt):
        pkt = pmt.to_python(msg_pmt)
        try:
            if self.d_regexp.match(pkt['info']):
                self.message_port_pub(pmt.intern('out'), pmt.to_pmt(pkt))
        except Exception as e:
            # TODO: Error handling, but for now, just output the error
            print "aprs_info_filter error:", e
            print "original message:", pkt

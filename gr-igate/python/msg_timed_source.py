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
from threading import Thread, Event

class msg_timed_source(gr.sync_block):
    """
    docstring for block msg_timed_source
    """
    def __init__(self, message, interval):
        gr.sync_block.__init__(self,
            name="msg_timed_source",
            in_sig=None,
            out_sig=None)
        self.message_port_register_out(pmt.intern('out'))

        self.d_message = message
        self.d_interval = interval

    def start(self):
        self.d_thread = Thread(
            target = self._thread_main
        )
        self.d_stop = Event()
        self.d_thread.start()
        return True

    def stop(self):
        self.d_stop.set()
        self.d_thread.join()
        return True

    def _thread_main(self):
        while not self.d_stop.is_set():
            self.message_port_pub(pmt.intern('out'), pmt.to_pmt(self.d_message))
            self.d_stop.wait(self.d_interval)

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

class aprs_decode_frame(gr.sync_block):
    """
    docstring for block aprs_decode_frame
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="aprs_decode_frame",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern('in'))
        self.message_port_register_out(pmt.intern('out'))
        self.set_msg_handler(pmt.intern('in'), self._handle_msg)

    def _handle_msg(self, msg_pmt):
        meta = pmt.to_python(pmt.car(msg_pmt))
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print "[ERROR] invalid message"
        else:
            msg_str = "".join([chr(x) for x in pmt.u8vector_elements(msg)])
            pkt = ax25_parse(msg_str)
            if pkt != None:
                self.message_port_pub(pmt.intern('out'), pmt.to_pmt(pkt))
            else:
                print "[ERROR] invalid formatted message"


def ax25_parse( frame ):
    res = {}
    left = len( frame )
    ptr = 0

    ##### Addresses and path
    in_addr = True
    addr = ""

    while in_addr:
        if left == 0:
            return None

        byte = ord( frame[ptr] )
        ptr += 1
        left -= 1

        addr += chr( byte>>1 )
        if byte & 1 == 1:
            in_addr = False

    path = []
    while len(addr)>=7:
        flags = ord(addr[6])

        # Pack address to CALL-N*
        call = addr[0:6].rstrip()
        if (flags&0x0F)>0:
            call += "-" + str( flags&0x0F )
        if flags&0x40:
            call += "*"

        path.append( call  )
        addr = addr[7:]

    if len( addr ) != 0:
        return None

    if len( path ) < 2:
        return None

    res["dst"] = path[0].rstrip("*")
    res["src"] = path[1].rstrip("*")
    res["path"] = path[2:]

    ##### Control bytes

    if left < 1:
        return None
    res["ctrl"] = ord( frame[ptr] )
    ptr += 1
    left += 1

    # FIXME: different types and ctrl-fields

    if left < 1:
        return None
    res["pid"] = ord( frame[ptr] )
    ptr += 1
    left += 1

    res["info"] = frame[ptr:]

    return res

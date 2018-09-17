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

import numpy
import pmt
from gnuradio import gr


symbol_lookup = [['',  '',  '',  '',  '', ' ', ' ', ' ', ' '],
                 ['', '*', '*', '', '', '', '=', '=', '']]

morse_dictionary = {'*=':'A',
                    '=***':'B',
                    '=*=*':'C',
                    '=**':'D',
                    '*':'E',
                    '**=*':'F',
                    '==*':'G',
                    '****':'H',
                    '**':'I',
                    '*===':'J',
                    '=*=':'K',
                    '*=**':'L',
                    '==':'M',
                    '=*':'N',
                    '===':'O',
                    '*==*':'P',
                    '==*=':'Q',
                    '*=*':'R',
                    '***':'S',
                    '=':'T',
                    '**=':'U',
                    '***=':'V',
                    '*==':'W',
                    '=**=':'X',
                    '=*==':'Y',
                    '==**':'Z',
                    '*====':'1',
                    '**===':'2',
                    '***==':'3',
                    '****=':'4',
                    '*****':'5',
                    '=****':'6',
                    '==***':'7',
                    '===**':'8',
                    '====*':'9',
                    '=====':'0'
                    }


class morse_decode(gr.sync_block):
    """
    docstring for block morse_decode
    """
    def __init__(self, units_per_second, sample_rate):
        gr.sync_block.__init__(self,
            name="morse_decode",
            in_sig=[numpy.uint8],
            out_sig=None)
        self.message_port_register_out(pmt.intern('out'))
        self.message = ''
        self.count = 1
        self.last_sample = 0

    def emit_message(self):
        if self.message:
            output = []
            self.message = self.message.split(' ')
            for symbols in self.message:
                if symbols not in morse_dictionary.keys():
                    output.append('?')
                else:
                    output.append(morse_dictionary[symbols])
            output = pmt.to_pmt(''.join(output))
            self.message_port_pub(pmt.intern('out'), output)
        self.message = ''


    def work(self, input_items, output_items):
        in0 = input_items[0]

        for sample in in0:

            if sample == self.last_sample:
                self.count = self.count + 1
                if self.last_sample == 0 and self.count / 2 >= 8:
                        self.emit_message()

            else:
                if self.count != 0:
                    if self.count / 2 < 9:
                        symbol = symbol_lookup[self.last_sample][self.count/2]
                    else:
                        symbol = ''

                    self.message = self.message + symbol

                self.count = 1
                self.last_sample = sample

        return len(input_items[0])

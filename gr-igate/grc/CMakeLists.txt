# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
install(FILES
    igate_clock_recovery_timer_bb.xml
    igate_aprs_decode_frame.xml
    igate_debug_print_msg.xml
    igate_aprs_append_path.xml
    igate_aprs_pkt_gen.xml
    igate_aprs_demod.xml
    igate_aprs_info_filter.xml
    igate_aprs_is_sink.xml
    igate_aprs_path_filter.xml DESTINATION share/gnuradio/grc/blocks
)

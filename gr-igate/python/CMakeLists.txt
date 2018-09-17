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

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    aprs_decode_frame.py
    debug_print_msg.py
    aprs_append_path.py
    msg_timed_source.py
    aprs_pkt_gen.py
    aprs_demod.py
    aprs_info_filter.py
    aprs_is_sink.py
    aprs_path_filter.py DESTINATION ${GR_PYTHON_DIR}/igate
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-igate)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_clock_recovery_timer_bb ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_clock_recovery_timer_bb.py)
GR_ADD_TEST(qa_aprs_decode_frame ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_decode_frame.py)
GR_ADD_TEST(qa_aprs_append_path ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_append_path.py)
GR_ADD_TEST(qa_aprs_pkt_gen ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_pkt_gen.py)
GR_ADD_TEST(qa_aprs_info_filter ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_info_filter.py)
GR_ADD_TEST(qa_aprs_is_sink ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_is_sink.py)
GR_ADD_TEST(qa_aprs_path_filter ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_aprs_path_filter.py)

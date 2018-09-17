# Copyright 2011,2012,2016 Free Software Foundation, Inc.
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
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND igate_sources
    clock_recovery_timer_bb_impl.cc
    meta.cc )

set(igate_sources "${igate_sources}" PARENT_SCOPE)
if(NOT igate_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT igate_sources)

add_library(gnuradio-igate SHARED ${igate_sources})
target_link_libraries(gnuradio-igate ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-igate PROPERTIES DEFINE_SYMBOL "gnuradio_igate_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-igate PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
include(GrMiscUtils)
GR_LIBRARY_FOO(gnuradio-igate RUNTIME_COMPONENT "igate_runtime" DEVEL_COMPONENT "igate_devel")

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_igate_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_igate.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_igate.cc
)

add_executable(test-igate ${test_igate_sources})

target_link_libraries(
  test-igate
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-igate
)

GR_ADD_TEST(test_igate test-igate)

########################################################################
# Print summary
########################################################################
message(STATUS "Using install prefix: ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Building for version: ${VERSION} / ${LIBVER}")


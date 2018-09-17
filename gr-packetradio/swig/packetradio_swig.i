/* -*- c++ -*- */

#define PACKETRADIO_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "packetradio_swig_doc.i"

%{
#include "packetradio/hdlc_framer_ax25.h"
%}


%include "packetradio/hdlc_framer_ax25.h"
GR_SWIG_BLOCK_MAGIC2(packetradio, hdlc_framer_ax25);

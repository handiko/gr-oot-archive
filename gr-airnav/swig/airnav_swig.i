/* -*- c++ -*- */

#define AIRNAV_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "airnav_swig_doc.i"

%{
#include "airnav/unitcircle_ff.h"
%}


%include "airnav/unitcircle_ff.h"
GR_SWIG_BLOCK_MAGIC2(airnav, unitcircle_ff);

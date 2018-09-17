/* -*- c++ -*- */

#define IGATE_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "igate_swig_doc.i"

%{
#include "igate/clock_recovery_timer_bb.h"
#include "igate/meta.h"
%}

%include "igate/clock_recovery_timer_bb.h"
GR_SWIG_BLOCK_MAGIC2(igate, clock_recovery_timer_bb);
%include "igate/meta.h"

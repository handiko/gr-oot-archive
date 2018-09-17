/* -*- c++ -*- */
/*
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "unitcircle_ff_impl.h"
#include <math.h>

namespace gr {
  namespace airnav {

    unitcircle_ff::sptr
    unitcircle_ff::make()
    {
      return gnuradio::get_initial_sptr
        (new unitcircle_ff_impl());
    }

    /*
     * The private constructor
     */
    unitcircle_ff_impl::unitcircle_ff_impl()
      : gr::sync_block("unitcircle_ff",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {}

    /*
     * Our virtual destructor.
     */
    unitcircle_ff_impl::~unitcircle_ff_impl()
    {
    }

    int
    unitcircle_ff_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const float *in = (const float *) input_items[0];
      float *out = (float *) output_items[0];

      // Do <+signal processing+>
      for(int i = 0; i < noutput_items; i++) {
        float val = in[i];
        val = fmod(val, this->FULL_CIRCLE);
        if(val < 0) val = this->FULL_CIRCLE + val;
        out[i] = val;
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace airnav */
} /* namespace gr */

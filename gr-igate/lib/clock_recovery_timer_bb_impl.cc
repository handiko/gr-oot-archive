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
#include "clock_recovery_timer_bb_impl.h"

#include <stdio.h>

namespace gr {
  namespace igate {

    clock_recovery_timer_bb::sptr
    clock_recovery_timer_bb::make(float samples_per_bit)
    {
      return gnuradio::get_initial_sptr
        (new clock_recovery_timer_bb_impl(samples_per_bit));
    }

    /*
     * The private constructor
     */
    clock_recovery_timer_bb_impl::clock_recovery_timer_bb_impl(float samples_per_bit)
      : gr::block("clock_recovery_timer_bb",
              gr::io_signature::make(1, 1, sizeof(int8_t)),
              gr::io_signature::make(1, 1, sizeof(int8_t))),
      d_samples_per_bit(samples_per_bit),
      d_samples_since_change(0.0f),
      d_last_bit(0)
    {
    }

    /*
     * Our virtual destructor.
     */
    clock_recovery_timer_bb_impl::~clock_recovery_timer_bb_impl()
    {
    }

    void
    clock_recovery_timer_bb_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = (int)ceil(d_samples_per_bit * noutput_items);
    }

    int
    clock_recovery_timer_bb_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const int8_t *in = (const int8_t *) input_items[0];
      int8_t *out = (int8_t *) output_items[0];
      int ii, oo, ni;
      int8_t cur_bit;

      ni = ninput_items[0];
      oo = 0;
      ii = 0;
      while(oo < noutput_items && ii < ni) {
        /* Send out bits, if we have bits in input buffer */
        if(d_samples_since_change > d_samples_per_bit) {
          d_samples_since_change -= d_samples_per_bit;
          out[oo++] = d_last_bit;
          /* We might have more in input buffer, thus, just retry */
          continue;
        }

        /* Fetch a bit */
        cur_bit = in[ii++];
        if(d_last_bit == cur_bit) {
          /* No change, thus, increase time since change */
          d_samples_since_change += 1.0f;
        } else {
          /* Changed, see if more than half a bit since last change, thus send */
          if(d_samples_since_change >= d_samples_per_bit/2.0f) {
            out[oo++] = d_last_bit;
          }
          d_last_bit = cur_bit;
          d_samples_since_change = 0.0f;
        }
      }
      consume_each (ii);

      // Tell runtime system how many output items we produced.
      return oo;
    }

  } /* namespace igate */
} /* namespace gr */

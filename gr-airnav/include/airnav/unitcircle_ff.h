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


#ifndef INCLUDED_AIRNAV_UNITCIRCLE_FF_H
#define INCLUDED_AIRNAV_UNITCIRCLE_FF_H

#include <airnav/api.h>
#include <gnuradio/sync_block.h>
#include <math.h>

namespace gr {
  namespace airnav {

    /*!
     * \class unitcircle_ff
     * \brief Constrain a value (in radians) to fall within a unit circle
     * \ingroup airnav
     *
     */
    class AIRNAV_API unitcircle_ff : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<unitcircle_ff> sptr;
      static const float FULL_CIRCLE = 2 * M_PI;

      /*!
       * \brief Return a shared_ptr to a new instance of airnav::unitcircle_ff.
       *
       * To avoid accidental use of raw pointers, airnav::unitcircle_ff's
       * constructor is in a private implementation
       * class. airnav::unitcircle_ff::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace airnav
} // namespace gr

#endif /* INCLUDED_AIRNAV_UNITCIRCLE_FF_H */

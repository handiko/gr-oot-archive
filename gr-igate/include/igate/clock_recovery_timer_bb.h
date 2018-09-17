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


#ifndef INCLUDED_IGATE_CLOCK_RECOVERY_TIMER_BB_H
#define INCLUDED_IGATE_CLOCK_RECOVERY_TIMER_BB_H

#include <igate/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace igate {

    /*!
     * \brief <+description of block+>
     * \ingroup igate
     *
     */
    class IGATE_API clock_recovery_timer_bb : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<clock_recovery_timer_bb> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of igate::clock_recovery_timer_bb.
       *
       * To avoid accidental use of raw pointers, igate::clock_recovery_timer_bb's
       * constructor is in a private implementation
       * class. igate::clock_recovery_timer_bb::make is the public interface for
       * creating new instances.
       */
      static sptr make(float samples_per_bit);
    };

  } // namespace igate
} // namespace gr

#endif /* INCLUDED_IGATE_CLOCK_RECOVERY_TIMER_BB_H */

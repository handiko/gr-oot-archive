/* -*- c++ -*- */
/*
 * Copyright 2017 Daniel Estevez <daniel@destevez.net>.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef INCLUDED_SATELLITES_LILACSAT1_DEMUX_IMPL_H
#define INCLUDED_SATELLITES_LILACSAT1_DEMUX_IMPL_H

#include <string>
#include <pmt/pmt.h>

#include <satellites/lilacsat1_demux.h>

namespace gr {
  namespace satellites {

    class lilacsat1_demux_impl : public lilacsat1_demux
    {
     private:
      int d_position;
      pmt::pmt_t d_tag;

     public:
      lilacsat1_demux_impl(std::string tag);
      ~lilacsat1_demux_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace satellites
} // namespace gr

#endif /* INCLUDED_SATELLITES_LILACSAT1_DEMUX_IMPL_H */


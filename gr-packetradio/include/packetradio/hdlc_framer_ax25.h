/* -*- c++ -*- */
/*
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
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


#ifndef INCLUDED_PACKETRADIO_HDLC_FRAMER_AX25_H
#define INCLUDED_PACKETRADIO_HDLC_FRAMER_AX25_H

#include <packetradio/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace packetradio {

    /*!
     * \brief <+description of block+>
     * \ingroup packetradio
     *
     */
    class PACKETRADIO_API hdlc_framer_ax25 : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<hdlc_framer_ax25> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of packetradio::hdlc_framer_ax25.
       *
       * To avoid accidental use of raw pointers, packetradio::hdlc_framer_ax25's
       * constructor is in a private implementation
       * class. packetradio::hdlc_framer_ax25::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string frame_tag_name, int flag_count);
    };

  } // namespace packetradio
} // namespace gr

#endif /* INCLUDED_PACKETRADIO_HDLC_FRAMER_AX25_H */

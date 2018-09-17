# APRS I-Gate lib for GnuRadio

Blocks for decoding APRS packets, preparing the packet for APRS-IS, and pass
packets to the APRS-IS system

Currently, the tools support only osmocom source, which means RTL-SDR and
others. Blocks are source independent, and can be used within GRC.

## Author

Max Sikström, SA6BBC

## Build
Those instructions expects that you run linux or macOS.

You need to have gnuradio installed. Please refer to gnuradio documentation:
http://gnuradio.org/redmine/projects/gnuradio/wiki

You also need the osmosdr suorce block, more information here:
http://sdr.osmocom.org/trac/wiki/GrOsmoSDR

Then check out this repository and run:
```
cd gr-igate # This repository
mkdir build
cd build
cmake ..
make
sudo make install
```

## Execution

To dump frames from radio to terminal, run:
```sh
aprs_dump
```

To start an RX-only I-Gate, run:
```sh
aprs_igate \
  -c <callsign> \
  -t 600 \
  -i <info message> \
  -X <aprs-is password>
```
With the following replaced:
- ```<callsign>``` The callsign of the I-gate, including SSID
- ```600``` Number of seconds between beacon packets from the I-Gate
- ```<info message>``` The info block of the beacon packets, should contain
  location of I-gate, encoded properly for APRS.
- ```<aprs-is password>``` The password for authentication to the APRS-IS system

## Links

- http://www.aprs-is.net/ - Information about APRS-IS
- http://aprs2.net/ - Tier2 ARPS-IS network, servers for accessing APRS-IS
- http://www.aprs.org/ - General information about APRS
- http://aprs.fi/ - APRS live map


Like GNU Radio, this module uses *master* and *next* branches, which are supposed to be used with the corresponding GNU Radio branches.
I recommend staying up-to-date by using the *next* branch.

### Dependencies

- GNU Radio v3.7.X or the v3.8 development branch (*next*). <br> See the [GNU Radio Wiki](http://gnuradio.org/redmine/projects/gnuradio/wiki/InstallingGR) for installation instructions.

- Software from your package manager. For Ubuntu systems, it's
```
sudo apt-get install cmake libboost-all-dev liblog4cpp5-dev swig
```


### Installation

```
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```


### Usage

open apps/rds_rx.grc example flow graph in GNU Radio Companion.


### Demos

Quick example:
http://www.youtube.com/watch?v=05i9C5lhorY

HAK5 episode (including installation):
http://www.youtube.com/watch?v=ukhrIl4JHbw

FOSDEM'15 talk (video and slides):
https://archive.fosdem.org/2015/schedule/event/sdr_rds_tmc/



### History

Continuation of gr-rds on BitBucket (originally from Dimitrios Symeonidis https://bitbucket.org/azimout/gr-rds/ and also on CGRAN https://www.cgran.org/wiki/RDS).

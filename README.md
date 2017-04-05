# White space network
### A simple OFDM based network

#### Contributors
* Andrew Keener - Author

#### Stages
1. Test (test) - Experimental and initial commits
2. Stable (Master) - TODO

#### Technical Details
##### App
* Platform - GNU Radio Companion
* Development - Flow chart with custom blocks in C++
##### Background
* TODO

#### Tutorial/Quick start guide

Notes: 
* all commands are ran as root (sudo is ommitted)
* install instructions for ubuntu 14.04

Install Hackrf one, if using another SDR you can skip
Also see: installing hackrf as per: https://mborgerson.com/getting-started-with-the-hackrf-one-on-ubuntu-14-04
1. $ apt-get update
2. $ apt-get upgrade
3. $ apt-get install hackrf

Alternative
I had trouble with different versions of hackrf including the one from cannonical
Try:
1. $ git clone https://github.com/mossmann/hackrf.git
2. $ cd hackrf/host
3. $ mkdir build && cd build
4. $ cmake ../ -DINSTALL_UDEV_RULES=ON
5. $ make
6. $ make install
7. $ ldconfig

At this point you should be able to test your hackrf
1. $ hackrf_info

Install Pybombs see: https://github.com/gnuradio/pybombs/ for troubleshooting
4. $ pip install pybombs
5.  pip install [--upgrade] git+https://github.com/gnuradio/pybombs.git

Add recipes for pybombs
6. $ pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git
7. $ pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-etcetera.git

Install GNU Radio with pybombs
8. $ pybombs prefix init ~/prefix -a myprefix -R gnuradio-default

Setup your prefix and run GRC
9. $ source ~/prefix/setup_env.sh
10. $ gnuradio-companion



Other tools:

GQRX is helpful for visualizing spectrum and has a digital radio tuner for radio stations as well
To Install:
1. $ add-apt-repository -y ppa:gqrx/gqrx-sdr
2. $ apt-get update
3. $ apt-get upgrade
4. $ apt-get install gqrx

If everything works and you can pick up radio stations you are good to go

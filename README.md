# White space network
### A simple OFDM based network

#### Contributors
* Andrew Keener - Author

#### Stages
1. Development (dev) - Experimental and initial commits
2. Test (test) - TODO
3. Stable (Master) - TODO

#### Technical Details
##### App
* Platform - GNU Radio Companion
* Development - Flow chart with custom blocks in C++
##### Background
* TODO

#### Tutorial/Quick start guide


apt-get update
apt-get upgrade
apt-get install hackrf
follow: https://github.com/gnuradio/pybombs/

//installing hackrf as per: https://mborgerson.com/getting-started-with-the-hackrf-one-on-ubuntu-14-04

git clone https://github.com/mossmann/hackrf.git
cd hackrf/host
mkdir build && cd build
cmake ../ -DINSTALL_UDEV_RULES=ON
make
make install
ldconfig

//test hackrf
hackrf_info

//install gqrx for testing sdr
add-apt-repository -y ppa:gqrx/gqrx-sdr

//If everything works and you can pick up radio stations you are good to go

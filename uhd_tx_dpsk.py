#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: UHD TX DPSK
# Generated: Mon Apr 10 10:51:26 2017
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import numpy
import osmosdr
import sip
import sys

class uhd_tx_dpsk(gr.top_block, Qt.QWidget):

    def __init__(self, address="addr=192.168.10.2", gain=0, samp_rate=1e6, freq=145.25):
        gr.top_block.__init__(self, "UHD TX DPSK")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD TX DPSK")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "uhd_tx_dpsk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.address = address
        self.gain = gain
        self.samp_rate = samp_rate
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.tun_gain = tun_gain = 0
        self.tun_freq = tun_freq = 145.25e6
        self.samps_per_sym = samps_per_sym = 4
        self.ampl = ampl = 0.1

        ##################################################
        # Blocks
        ##################################################
        self._tun_freq_layout = Qt.QVBoxLayout()
        self._tun_freq_tool_bar = Qt.QToolBar(self)
        self._tun_freq_layout.addWidget(self._tun_freq_tool_bar)
        self._tun_freq_tool_bar.addWidget(Qt.QLabel("UHD Freq (Hz)"+": "))
        self._tun_freq_counter = Qwt.QwtCounter()
        self._tun_freq_counter.setRange(40e6, 200e6, 1)
        self._tun_freq_counter.setNumButtons(2)
        self._tun_freq_counter.setValue(self.tun_freq)
        self._tun_freq_tool_bar.addWidget(self._tun_freq_counter)
        self._tun_freq_counter.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_freq_slider.setRange(40e6, 200e6, 1)
        self._tun_freq_slider.setValue(self.tun_freq)
        self._tun_freq_slider.setMinimumWidth(200)
        self._tun_freq_slider.valueChanged.connect(self.set_tun_freq)
        self._tun_freq_layout.addWidget(self._tun_freq_slider)
        self.top_layout.addLayout(self._tun_freq_layout)
        self._ampl_layout = Qt.QVBoxLayout()
        self._ampl_tool_bar = Qt.QToolBar(self)
        self._ampl_layout.addWidget(self._ampl_tool_bar)
        self._ampl_tool_bar.addWidget(Qt.QLabel("Amplitude"+": "))
        self._ampl_counter = Qwt.QwtCounter()
        self._ampl_counter.setRange(0, 1, 0.01)
        self._ampl_counter.setNumButtons(2)
        self._ampl_counter.setValue(self.ampl)
        self._ampl_tool_bar.addWidget(self._ampl_counter)
        self._ampl_counter.valueChanged.connect(self.set_ampl)
        self._ampl_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._ampl_slider.setRange(0, 1, 0.01)
        self._ampl_slider.setValue(self.ampl)
        self._ampl_slider.setMinimumWidth(200)
        self._ampl_slider.valueChanged.connect(self.set_ampl)
        self._ampl_layout.addWidget(self._ampl_slider)
        self.top_layout.addLayout(self._ampl_layout)
        self._tun_gain_layout = Qt.QVBoxLayout()
        self._tun_gain_tool_bar = Qt.QToolBar(self)
        self._tun_gain_layout.addWidget(self._tun_gain_tool_bar)
        self._tun_gain_tool_bar.addWidget(Qt.QLabel("UHD Tx Gain"+": "))
        self._tun_gain_counter = Qwt.QwtCounter()
        self._tun_gain_counter.setRange(0, 20, 1)
        self._tun_gain_counter.setNumButtons(2)
        self._tun_gain_counter.setValue(self.tun_gain)
        self._tun_gain_tool_bar.addWidget(self._tun_gain_counter)
        self._tun_gain_counter.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._tun_gain_slider.setRange(0, 20, 1)
        self._tun_gain_slider.setValue(self.tun_gain)
        self._tun_gain_slider.setMinimumWidth(200)
        self._tun_gain_slider.valueChanged.connect(self.set_tun_gain)
        self._tun_gain_layout.addWidget(self._tun_gain_slider)
        self.top_layout.addLayout(self._tun_gain_layout)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	tun_freq, #fc
        	samp_rate, #bw
        	"Transmit Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(tun_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.digital_dxpsk_mod_0 = digital.dqpsk_mod(
        	samples_per_symbol=samps_per_sym,
        	excess_bw=0.35,
        	mod_code="gray",
        	verbose=False,
        	log=False)
        	
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((ampl, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2**8, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_dxpsk_mod_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_dxpsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_tx_dpsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.tun_freq, self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_tun_gain(self):
        return self.tun_gain

    def set_tun_gain(self, tun_gain):
        self.tun_gain = tun_gain
        self._tun_gain_counter.setValue(self.tun_gain)
        self._tun_gain_slider.setValue(self.tun_gain)

    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        self.osmosdr_sink_0.set_center_freq(self.tun_freq, 0)
        self._tun_freq_counter.setValue(self.tun_freq)
        self._tun_freq_slider.setValue(self.tun_freq)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.tun_freq, self.samp_rate)

    def get_samps_per_sym(self):
        return self.samps_per_sym

    def set_samps_per_sym(self, samps_per_sym):
        self.samps_per_sym = samps_per_sym

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl
        self._ampl_counter.setValue(self.ampl)
        self._ampl_slider.setValue(self.ampl)
        self.blocks_multiply_const_vxx_0.set_k((self.ampl, ))

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-a", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set IP Address [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Default Gain [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set Sample Rate [default=%default]")
    parser.add_option("-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(145.25),
        help="Set Default Frequency [default=%default]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = uhd_tx_dpsk(address=options.address, gain=options.gain, samp_rate=options.samp_rate, freq=options.freq)
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets


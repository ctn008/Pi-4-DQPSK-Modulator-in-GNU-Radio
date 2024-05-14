#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: pi4dqpsk_mod_demod_w_pi4mapper
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import pi4dqpsk_mod_demod_w_pi4mapper_epy_block_1 as epy_block_1  # embedded python block



from gnuradio import qtgui

class pi4dqpsk_mod_demod_w_pi4mapper(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "pi4dqpsk_mod_demod_w_pi4mapper", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("pi4dqpsk_mod_demod_w_pi4mapper")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "pi4dqpsk_mod_demod_w_pi4mapper")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 18000
        self.samp_per_symbol = samp_per_symbol = 4

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                samp_per_symbol,
                (samp_per_symbol*symbol_rate),
                symbol_rate,
                0.35,
                (32*samp_per_symbol)))
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                samp_per_symbol,
                (samp_per_symbol*symbol_rate),
                symbol_rate,
                0.35,
                (32*samp_per_symbol)))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            256, #size
            samp_per_symbol*symbol_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.epy_block_1 = epy_block_1.blk()
        self.blocks_vector_source_x_1 = blocks.vector_source_f((1, 0, 0, 0), True, 1, [])
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, (symbol_rate*samp_per_symbol),True)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_float*1, samp_per_symbol)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, samp_per_symbol)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 4, 4192))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_repeat_0, 0))
        self.connect((self.epy_block_1, 1), (self.blocks_repeat_0_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_float_to_complex_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pi4dqpsk_mod_demod_w_pi4mapper")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.blocks_throttle_0_0_0.set_sample_rate((self.symbol_rate*self.samp_per_symbol))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_per_symbol*self.symbol_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_symbol, (self.samp_per_symbol*self.symbol_rate), self.symbol_rate, 0.35, (32*self.samp_per_symbol)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(self.samp_per_symbol, (self.samp_per_symbol*self.symbol_rate), self.symbol_rate, 0.35, (32*self.samp_per_symbol)))

    def get_samp_per_symbol(self):
        return self.samp_per_symbol

    def set_samp_per_symbol(self, samp_per_symbol):
        self.samp_per_symbol = samp_per_symbol
        self.blocks_repeat_0.set_interpolation(self.samp_per_symbol)
        self.blocks_repeat_0_0.set_interpolation(self.samp_per_symbol)
        self.blocks_throttle_0_0_0.set_sample_rate((self.symbol_rate*self.samp_per_symbol))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_per_symbol*self.symbol_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(self.samp_per_symbol, (self.samp_per_symbol*self.symbol_rate), self.symbol_rate, 0.35, (32*self.samp_per_symbol)))
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(self.samp_per_symbol, (self.samp_per_symbol*self.symbol_rate), self.symbol_rate, 0.35, (32*self.samp_per_symbol)))




def main(top_block_cls=pi4dqpsk_mod_demod_w_pi4mapper, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()

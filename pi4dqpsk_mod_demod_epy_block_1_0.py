"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Pi4DQPSK Mapper',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.float32, np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.index = 0

    def work(self, input_items, output_items):
        # Phase Index Change Table: corresponding to current phase (row 0-7) and current dibit value (column 0-3)
        LK_table = [[1, 3, 7, 5],
                    [2, 4, 0, 6],
                    [3, 5, 1, 7],
                    [4, 6, 2, 0],
                    [5, 7, 3, 1],
                    [6, 0, 4, 2],
                    [7, 1, 5, 3],
                    [0, 2, 6, 4]]
        # Phase value corresponding to Phase Index
        IQ_table = [[ np.cos(np.pi/4 * 0) , np.sin(np.pi/4 * 0) ],
                    [ np.cos(np.pi/4 * 1) , np.sin(np.pi/4 * 1) ],
                    [ np.cos(np.pi/4 * 2) , np.sin(np.pi/4 * 2) ],
                    [ np.cos(np.pi/4 * 3) , np.sin(np.pi/4 * 3) ],
                    [ np.cos(np.pi/4 * 4) , np.sin(np.pi/4 * 4) ],
                    [ np.cos(np.pi/4 * 5) , np.sin(np.pi/4 * 5) ],
                    [ np.cos(np.pi/4 * 6) , np.sin(np.pi/4 * 6) ],
                    [ np.cos(np.pi/4 * 7) , np.sin(np.pi/4 * 7) ]]

        index = 0 # Set initial phase: I = 1 Q = 0
        for i in range (len(input_items[0])):
            self.index = LK_table[self.index][input_items[0][i]]
            output_items[0][i] = IQ_table[self.index][0]
            output_items[1][i] = IQ_table[self.index][1]
        return len(output_items[0])

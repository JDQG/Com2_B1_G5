import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following: Recibe dos entradas: una que controla la amplitud de la señal y otra que ajusta la fase, y produce una salida compleja donde la parte real e imaginaria representan la modulación en cuadratura. La señal resultante se calcula como una exponencial compleja, lo que permite crear modulaciones digitales o generar señales en banda base para comunicaciones."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])

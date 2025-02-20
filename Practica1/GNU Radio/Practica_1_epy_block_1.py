import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_Diff',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # Guarda la última muestra de la ejecución anterior
        self.prev_sample = 0.0

    def work(self, input_items, output_items):
        x = input_items[0]
        y = output_items[0]
        N = len(x)
        
        if N == 0:
            return 0
        
        # 1) Diferencia para la primera muestra del bloque actual
        #    usando la última muestra del bloque anterior
        y[0] = x[0] - self.prev_sample
        
        # 2) Diferencia entre muestras consecutivas dentro del bloque
        for i in range(1, N):
            y[i] = x[i] - x[i-1]
        
        # 3) Actualiza el estado para el siguiente bloque
        self.prev_sample = x[-1]
        
        return N
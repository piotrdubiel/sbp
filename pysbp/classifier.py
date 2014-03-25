from .decoder import Decoder
from .loader import load_from_octave
import sbp


class Classifier:
    def __init__(self, network_filename, mapping_filename):
        self.decoder = Decoder.from_yaml(mapping_filename)
        net = load_from_octave(network_filename)
        for layer in net:
            sbp.add_layer(*layer)

    def classify(self, x):
        y = sbp.classify(x)
        code = y.index(max(y))
        return self.decoder.map(code)

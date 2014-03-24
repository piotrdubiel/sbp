import sbp
import loader


init = sbp.init
classify = sbp.classify
add_layer = sbp.add_layer
train = sbp.train


def load_from_octave(filename):
    init()
    net = loader.load_from_octave(filename)

    for layer in net:
        add_layer(*layer)

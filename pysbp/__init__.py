import sbp

def load(filename):
    with open(filename) as f:
        sbp.init()

init = sbp.init
classify = sbp.classify
add_layer = sbp.add_layer
train = sbp.train

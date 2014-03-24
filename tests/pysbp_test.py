from nose.tools import assert_raises
import pysbp

EPS = 0.7e-2


def load_xor_network_and_classify_test():
    # given
    pysbp.init()
    pysbp.add_layer([43.259, 43.268, -66.366], [65.075, 65.101, -27.079])
    pysbp.add_layer([-29.041, 27.2972, -5.0622])

    examples = [[[0.0, 0.0], [0.0]],
                [[1.0, 0.0], [1.0]],
                [[0.0, 1.0], [1.0]],
                [[1.0, 1.0], [0.0]]]

    # when
    def check_examples(input, output):
        answer = pysbp.classify(input)
        assert abs(answer[0] - output[0]) < EPS, \
            "Network answer for {} should be {}, not {}".format(
                input, output, answer)

    # then
    for input, output in examples:
        yield check_examples, input, output


def classify_with_random_network_test():
    # given
    pysbp.init()
    pysbp.add_layer([0.5, 0.5, 0.5])

    # when
    answer = pysbp.classify([1, 0])

    # then
    assert all(a >= 0.0 and a <= 1.0 for a in answer),\
        "Some values in {} aren't from range [0,1]".format(answer)


def classify_accepts_only_list_test():
    # given
    pysbp.init()

    # when
    def check_argument_type(exception, *args):
        assert_raises(exception, pysbp.classify, *args)
    # then
    for arg in [3, {'f': 3}, 'some string', 4.6]:
        yield check_argument_type, TypeError, arg


#def train_to_solve_xor_test():
#    # given
#    examples = [[[0.0, 0.0], [0.0]],
#                [[1.0, 0.0], [1.0]],
#                [[0.0, 1.0], [1.0]],
#                [[1.0, 1.0], [0.0]]]
#
#    pysbp.init()
#    pysbp.add_layer([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
#    pysbp.add_layer([0.5, 0.5, 0.5])
#
#    # when
#    for i in range(1000):
#        for input, output in examples:
#            pysbp.train(input, output)
#
#    # then
#    def check_examples(input, output):
#        answer = pysbp.classify(input)
#        assert abs(answer[0] - output[0]) < EPS, \
#            "Network answer for {} should be {}, not {}".format(
#                input, output, answer)
#
#    for input, output in examples:
#        yield check_examples, input, output
#

def load_octave_test():
    # given
    # letter w
    example = [1.5182029, 4.2104764, -0.9496237, 0.615157, 1.8448412, -0.3655337, 1.593656,
               -0.401572, -1.7964933, -0.29715088, 0.30455363, 2.2069676, -0.3178953,
               1.2597578, 1.6501256, -1.6158084, -0.669811, 0.85303575, 0.27090243,
               0.8615778, 0.56952584, 0.95694315, -1.9922807, -0.43113938, 0.49479017,
               1.2703928, 1.5572349, -0.08066087, 1.8068724, 0.62642187, -0.48374003,
               0.9044069, 0.11108308, 0.07535343, 0.4748401, -0.6188048, -0.07887313,
               -0.3505041, -0.70318097, -0.59820455, -0.2938594, -0.19870493, 0.42195785,
               0.21510367, 0.54319054, 0.16215804, -0.1808343, 0.0510478, 1.0164162,
               0.35691723, 1.3395526, 0.76272136, -1.4247293, 0.41414088, -0.7273988,
               0.29539558, -0.51242316, 0.014501013, -1.0800554, 0.013855811, 0.40949804,
               -0.26722014, 0.6959366, 0.69734293, 0.16188288, -0.09776891, 0.09395206,
               0.032530826, -0.26055062, 8.730186E-4, 0.5129696, 0.24590321, -0.3367841,
               0.31336462, -0.41695657, 0.036724858, -0.9864306, 0.03783525, 0.40775126,
               -0.11667539, -1.001846, 0.50752866, 0.39828777, 0.34053615, 0.3474453,
               0.085608006, 0.27205867, 0.7626132, -0.23783158, 0.46978295, 0.48218146,
               0.015115089, -0.29299927, -0.18095985, 0.014097757, 0.23929955, -0.19612126,
               -0.037772242, 0.11949382, 0.1612628, -0.36138365, -0.019882096, -0.5185845,
               -0.029387899, -0.5840359, 0.20192197, -0.09736326, -0.76652694, -0.022606745,
               0.17889309, -0.43191314, -0.004612534, 0.48162824, -0.30936575, -0.050524455,
               0.12856568, -0.34870595, 0.07073312, -0.09698311, 0.1318148, -0.13789801,
               0.043483153, 0.13860495, 0.17612338, -0.1422962, 0.28367153, 0.14920713,
               -0.07946629, 0.123614, 0.23785505, -0.5135928, -0.047427915, -0.103826374,
               0.35870075, -0.29971167, -0.49939138, -0.13281187, 0.32142022, 0.14256476,
               -0.4507181, 0.121927395, 0.24987419, -0.33211565, -0.16789456, 0.3849047,
               0.32664162, -0.07831076, -0.11389559, -0.2222453, -0.5383057]

    # when
    pysbp.load_from_octave('net/nets-v1/pl_small_net.txt')
    answer = pysbp.classify(example)
    # then
    assert answer.index(max(answer)) == 29 # code for w

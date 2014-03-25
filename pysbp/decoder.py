import yaml


class Decoder:
    def __init__(self, mapping):
        self.mapping = mapping

    @classmethod
    def from_yaml(cls, filename):
        with open(filename) as file:
            return cls(yaml.load(file))

    def map(self, code):
        return self.mapping[code]

    def remap(self, value):
        for k, v in self.mapping.iteritems():
            if v == value:
                return k

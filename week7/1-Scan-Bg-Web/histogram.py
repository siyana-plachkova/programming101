import json


class Histogram:

    def __init__(self):
        self.histogram_dictionary = {}

    def add(self, server):
        if server not in self.histogram_dictionary.keys():
            self.histogram_dictionary[server] = 1
        else:
            self.histogram_dictionary[server] += 1

    def count(self, server):
        if server not in self.histogram_dictionary.keys():
            return None
        else:
            return self.histogram_dictionary[server]

    def get_dict(self):
        return self.histogram_dictionary

    def items(self):
        return tuple(zip(self.histogram_dictionary.keys(), self.histogram_dictionary.values()))

    def save(self):
        json.dump(self.get_dict(), open('histogram.json', 'w'))

    def load(self):
        self.histogram_dictionary = json.load(open('histogram.json', 'r'))

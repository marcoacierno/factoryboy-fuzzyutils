import factory

from factory import fuzzy
from factory.fuzzy import BaseFuzzyAttribute


class FuzzyColor(BaseFuzzyAttribute):
    def fuzz(self):
        color = lambda: fuzzy._random.randint(0, 255)
        return '#%02X%02X%02X' % (color(), color(), color())
  

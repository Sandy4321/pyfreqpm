# -*- coding: utf-8 -*-
"""
    pyfreqpm
    ~~~~~~~~~~~~~~
    Implements prediction model
    :copyright: (c) 2016 by Alexey Smirnov.
    :license: BSD, see LICENSE for more details.
"""

from .analyzer import AprioriGen, AnalyzerGen, AprioriTid, Eclat, FPGrowth
from pprint import pprint


class FreqPM:
    analyzers = {'apriori-gen': AprioriGen,
                 'apriori-tid': AprioriTid,
                 'eclat': Eclat,
                 'max-miner': AnalyzerGen,
                 'fp-growth': FPGrowth}

    @classmethod
    def model(cls, analyzer):
        return cls.analyzers.get(analyzer, AnalyzerGen)()


if __name__ == '__main__':
    with open('test/basic.csv', 'r') as f:
        dataset = [[i.strip() for i in l.split(',')] for l in f]
    items = ['beer', 'wine', 'apple', 'pear']

    test = FreqPM.model('fp-growth')
    test.fit(dataset, items)
    pprint(test.support)
    pprint(test.rules)
    pprint(test.predict({'beer'}))



This is a frequent pattern mining framework implementing the following algorithms

1) generic Apriori

3) Apriori-TID

4) Eclat

5) FP-Growth

**Usage**

```python
>>> from pyfreqpm import FreqPM
>>> dataset = [['i1', 'i2'],
>>>            ['i1', 'i3'],
>>>            ['i1', 'i2']] # list of all transactions
>>> items = ['i1', 'i2', 'i3'] # list of all possible items
>>>
>>> """ Possible analyzers are
>>> - apriori-gen
>>> - apriori-tid
>>> - eclat
>>> - fp-growth
>>> """
>>> test = FreqPM.model(analyzer='apriori-gen')
>>> test.fit(dataset, items)
>>> test.predict(['i1'])
{'confidence': 0.6666666666666666, 'lift': 1.0, 'to': frozenset({'i2'})}
```

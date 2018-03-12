## About
Frequent patterns are patterns which appear frequently within a dataset. A frequent itemset is one which is made up of one of these patterns, which is why frequent pattern mining is often alternately referred to as frequent itemset mining.

Frequent pattern mining is most easily explained by introducing market basket analysis (or affinity analysis), a typical usage for which it is well-known. Market basket analysis attempts to identify associations, or patterns, between the various items that have been chosen by a particular shopper and placed in their market basket, be it real or virtual, and assigns support and confidence measures for comparison. The value of this lies in cross-marketing and customer behavior analysis.

The generalization of market basket analysis is frequent pattern mining, and is actually quite similar to classification except that any attribute, or combination of attributes (and not just the class), can be predicted in association. As association does not require the pre-labeling of classes, it is a form of unsupervised learning. [source](https://www.kdnuggets.com/2016/10/association-rule-learning-concise-technical-overview.html)



## Framework

![Alt Text](docs.gif)

#### Algorithms
This frequent pattern mining framework implementing the following algorithms

1) generic [Apriori](https://en.wikipedia.org/wiki/Apriori_algorithm)
3) [Apriori-TID](https://www.philippe-fournier-viger.com/spmf/AprioriTID.php)
4) [Eclat](https://www.slideshare.net/wanaezwani/apriori-and-eclat-algorithm-in-association-rule-mining)
5) [FP-Growth](https://en.wikibooks.org/wiki/Data_Mining_Algorithms_In_R/Frequent_Pattern_Mining/The_FP-Growth_Algorithm)

#### Usage

1. Get a list if all transactions (previous orders) and a list of items being sold that are encountered in
the dataset
```python
from pyfreqpm import FreqPM
dataset = [['i1', 'i2'],
           ['i1', 'i3'],
           ['i1', 'i2']]
items = ['i1', 'i2', 'i3']
```

2. Create an analyzer and provide algorithm to use and `min_support`, `min_confidence`, `min_lift` parameters.

Possible values for analyzer are `apriori-gen`, `apriori-tid`, `eclat`, `fp-growth`

```python
test = FreqPM.model(analyzer='apriori-gen')
test.fit(dataset, items, min_support=0.1, min_confidence=0.5, min_lift=1.0)
```

3. After creating a model a prediction may be made for a new basket based on mined association rules
```python
test.predict(['i1'])
{'confidence': 0.6666666666666666, 'lift': 1.0, 'to': frozenset({'i2'})}
```
This prediction recommends item `i2` for someone having `i1` already in the shopping cart.
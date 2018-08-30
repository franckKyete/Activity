import pandas as pd
from collections import Counter
from pylab import *

def printEmpiricDistribution(data):

    strength = len(data)
    counter = Counter(data)
	
    for word, quatity in counter.most_common():
        print('The modality "{}" has a quatity of {} and a frequency of {:0.5f}'.format(word, quatity, quatity/strength))
		
def getX(data):
	counter = Counter(data)
	strength = len(data)
	x = []
	for w, q in counter.most_common():
		x.append(q)
	return x
		

data = pd.read_csv("operations_enrichies.csv", parse_dates = [0])

data["categ"].value_counts(normalize=True).plot(kind='hist')
show()
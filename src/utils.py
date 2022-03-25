#!/usr/bin/env python

import pandas as pd

def integratemetadata():
	medidas = "../datasets/medidas/"+"2020-21.csv"
	medidas2020 = pd.read_csv(medidas)
	test = medidas2020.count()
	return test

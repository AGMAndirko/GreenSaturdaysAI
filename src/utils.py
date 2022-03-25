#!/usr/bin/env python

import pandas as pd
import numpy as np

def integratemetadata():
	"""
	integratemetadata() arregla el problema de que en las medidas de 2020-21 los contaminantes salen por código en vez de por nombre propio.
	devuelve una copia de las medidas de 2020-2021 con una columna nueva (CONTAMINANTE) con el nombre del contaminante
	"""
	medidas_str = "../datasets/medidas/"+"2020-21.csv"
	medidas = pd.read_csv(medidas_str)
	
	meta = "../datasets/meta/qualitat_aire_contaminants.csv"
	meta = pd.read_csv(meta)

	# crea diccionario con código de contaminante y nombres, reemplaza la columna
	dic = dict(meta[["Codi_Contaminant","Desc_Contaminant"]].values)
	print(dic)
	#medidas["CODI_CONTAMINANT"] = medidas["CODI_CONTAMINANT"].replace('nan', np.nan).fillna(0)
	test = medidas["CODI_CONTAMINANT"]
	print(set(test))
	print(medidas["CODI_CONTAMINANT"])
	medidas["CONTAMINANTE"] = medidas["CODI_CONTAMINANT"].replace(dic)
	return medidas



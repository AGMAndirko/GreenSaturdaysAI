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
	test = medidas["CODI_CONTAMINANT"]
	medidas["CONTAMINANTE"] = medidas["CODI_CONTAMINANT"].replace(dic)
	return medidas

def join_mapas():
	"""
	join_mapas() genera un único csv para los csvs de /maps
	Return: un único csv con dos columnas extra para diferenciar:
		- Año
		- Contaminante
	"""
	maps_path = "../datasets/maps/"
	anyo = ['2018', '2019']
	contaminante = ['no2', 'pm10', 'pm2-5']

	final = pd.DataFrame()
	
	for i in anyo:
		for k in contaminante:
			path = maps_path+i+"/"+i+"_tramer_"+k+"_mapa_qualitat_aire_bcn.csv"
			df = pd.read_csv(path)
			df['año'] = i
			df['contaminante'] = k
			final = final.append(df)

	path = maps_path+"mapas_qualitat_aire_bcn.csv"
	final.to_csv(path)
	return final




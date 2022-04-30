#!/usr/bin/env python

import pandas as pd
import numpy as np
import datetime as dt

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

def mediciones_unif():

	'''
	Leemos y unificamos ambos dataframes forzando la misma estructura y tipo de datos:
	'''

	#Leemos los csv y convertimos a dataframe saltando las líneas que no tengan el mismo formato:
	df_21 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/medidas/2020-21.csv",on_bad_lines='skip')
	df_estaciones_21 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/estaciones/2021/2021_qualitat_aire_estacions.csv")

	#Unificamos dataframes y eliminamos las columnas que no aportan información:
	df_21 = df_21.drop(["CODI_PROVINCIA", "PROVINCIA", "CODI_MUNICIPI", "MUNICIPI"], axis=1)
	df_estaciones_21 = df_estaciones_21.drop(["codi_eoi","Nom_districte","Codi_barri","zqa","Codi_districte","Clas_1"], axis=1)

	#Limpiamos y unificamos con descripción de estaciones el df del 21:
	df_21 = df_21.merge(df_estaciones_21, how='left', left_on="ESTACIO", right_on='Estacio')

mediciones_unif()

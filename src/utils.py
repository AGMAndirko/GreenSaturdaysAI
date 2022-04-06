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

	'''
	Leemos y unificamos ambos dataframes forzando la misma estructura y tipo de datos:
	'''

	#Leemos los csv y convertimos a dataframe saltando las líneas que no tengan el mismo formato:
	df_19 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/medidas/2018-19.csv",on_bad_lines='skip')
	df_21 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/medidas/2020-21.csv",on_bad_lines='skip')
	df_estaciones_21 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/estaciones/2021/2021_qualitat_aire_estacions.csv")
	df_estaciones_18 = pd.read_csv("C:/Users/koke_/GreenSaturdaysAI/datasets/estaciones/2018/2018_qualitat_aire_estacions_bcn.csv")

	#Unificamos dataframes y eliminamos las columnas que no aportan información:
	df_21 = df_21.drop(["CODI_PROVINCIA", "PROVINCIA", "CODI_MUNICIPI", "MUNICIPI"], axis=1)
	df_estaciones_21 = df_estaciones_21.drop(["codi_eoi","Nom_districte","Codi_barri","zqa","Codi_districte","Clas_1"], axis=1)

	#Limpiamos y unificamos con descripción de estaciones el df del 19:
	df_estaciones_18 = df_estaciones_18.drop(["zqa","codi_eoi","Codi_Districte", "Ocupacio_sol","Contaminant_1","Contaminant_2","Contaminant_3"], axis = 1)
	df_19 = df_19.merge(df_estaciones_18,how="left",left_on="codi_dtes", right_on='codi_dtes')
	df_19 = df_19.drop(["codi_dtes","codi_eoi","zqa","Codi_Barri","Nom_Districte","dateTime"], axis=1)

		#Formateamos las fechas para que case con el df de 2021:
	df_19[["fecha","hora"]] = df_19.generat.str.split(" ",expand=True)
	df_19[["DIA","MES","ANY"]] = df_19.fecha.str.split("/", expand=True)
	df_19 = df_19.drop(["generat","qualitat_aire","hora_o3","hora_no2","hora_pm10","qualitat_o3","qualitat_no2","qualitat_pm10"], axis=1)

		#Hay que separar las mediciones de los 3 contaminantes en distintas filas:

	colo3 = colno2 = colpm10 = []
	columns = df_19.columns.tolist()
	colo3 = [e for e in columns if e not in ('valor_no2', 'valor_pm10')]
	dfo3 = df_19[colo3]
	colno2 = [e for e in columns if e not in ('valor_o3', 'valor_pm10')]
	dfno2 = df_19[colno2]
	colpm10 = [e for e in columns if e not in ('valor_no2', 'valor_o3')]
	dfpm10 = df_19[colpm10]
	dfo3['CODI_CONTAMINANT'] = 14
	dfo3 = dfo3.rename({'valor_o3': 'H'},axis='columns')
	dfno2['CODI_CONTAMINANT'] = 8
	dfno2 = dfno2.rename({'valor_no2': 'H'}, axis='columns')
	dfpm10['CODI_CONTAMINANT'] = 10
	dfpm10 = dfpm10.rename({'valor_pm10': 'H'}, axis='columns')

	#Formato final del df_19:
	df_19 = pd.concat([dfo3,dfno2,dfpm10])

	#Limpiamos y unificamos con descripción de estaciones el df del 21:
	df_21 = df_21.merge(df_estaciones_21, how='left', left_on="ESTACIO", right_on='Estacio')

	print(df_19)

mediciones_unif()

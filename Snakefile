
DTM = "datasets/maps"
DTE = "datasets/estaciones/"

TMP = "temp"
##### SET UP #####
rule downloads_mapas:
    log:
        "logs/sm_downloads_maps.log"
    output:
	"{DTM}2019/2019_tramer_no2_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2019/2019_tramer_pm2-5_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2019/2019_tramer_pm2-5_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2019/2019_estil_qgis_tramer_pm10_mapa_qualitat_aire_bcn.qml"
	"{DTM}/2019/2019_tramer_pm10_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2019/2019_tramer_no2_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2019/2019_tramer_pm10_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2019/2019_estil_qgis_tramer_no2_mapa_qualitat_aire_bcn.qml"
	"{DTM}/2019/2019_estil_qgis_tramer_pm2-5_mapa_qualitat_aire_bcn.qml"
	"{DTM}/2018/2018_tramer_no2_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2018/2018_tramer_pm10_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2018/2018_tramer_pm2-5_mapa_qualitat_aire_bcn.gpkg"
	"{DTM}/2018/2018_tramer_no2_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2018/2018_tramer_pm10_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2018/2018_tramer_pm2-5_mapa_qualitat_aire_bcn.csv"
	"{DTM}/2018/2018_estil_qgis_tramer_no2_mapa_qualitat_aire_bcn.qml"
	"{DTM}/2018/2018_estil_qgis_tramer_pm10_mapa_qualitat_aire_bcn.qml"
	"{DTM}/2018/2018_estil_qgis_tramer_pm2-5_mapa_qualitat_aire_bcn.qml"
    shell:
        """
	wget -P {TMP}/ --input-file urls_maps.txt 2>> logs/sm_downloads_maps.log
	mv {TMP}/2019* {DTM}/2019/
	mv {TMP}/2018* {DTM}/2018/
        """

rule downloads_estaciones:
    log:
        "logs/sm_downloads_est.log"
    output:
        "{DTE}/2018/2018_qualitat_aire_estacions.csv"
	"{DTE}/2021/2021_qualitat_aire_estacions.csv"
    shell:
        """
        wget -P {TMP}/ --input-file urls_estaciones.txt 2>> logs/sm_downloads_est.log
	mv {TMP}/qualitat_aire_estacions_bcn.csv {DTE}/2018/2018_qualitat_aire_estacions.csv
	mv {TMP}/2021_qualitat_aire_estacions.csv {DTE}/2021/2021_qualitat_aire_estacions.csv        
	"""

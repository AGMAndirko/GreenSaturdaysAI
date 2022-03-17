#!/usr/bin/env bash

# Mapas immisión
wget -i urls_maps.txt
 
mkdir datasets/maps/2019
mkdir datasets/maps/2018
cp 2019* datasets/maps/2019/
cp 2018* datasets/maps/2018/
rm 2019* 2018*

# estaciones
wget -i urls_estaciones.txt
mkdir datasets/estaciones/2021
mkdir datasets/estaciones/2020
mkdir datasets/estaciones/2019
mkdir datasets/estaciones/2018
cp 2021* datasets/estaciones/2021/
cp 2020* datasets/estaciones/2020/
cp 2019* datasets/estaciones/2019/
cp 2018* datasets/estaciones/2018/

rm 2019* 2018* 2020* 2021*



#!/usr/bin/env bash

# Mapas immisión
wget -i urls_maps.txt
 
mkdir datasets/maps/2019
mkdir datasets/maps/2018
cp 2019* datasets/maps/2019/
cp 2018* datasets/maps/2018/
rm 2019*
rm 2018*


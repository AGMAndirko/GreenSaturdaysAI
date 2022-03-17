#!/usr/bin/env bash

# Mapas immisión 2019
wget -i url_maps_2019.txt

mkdir datasets/maps/
mkdir datasets/maps/2019
mkdir datasets/maps/2018
cp 2019* datasets/maps/2019/
rm 2019*

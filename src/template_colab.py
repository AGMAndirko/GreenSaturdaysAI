#!pip install prophet
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import prophet
import requests

!rm -r /content/GreenSaturdaysAI
!git clone https://github.com/AGMAndirko/GreenSaturdaysAI/

import sys
sys.path.append('/content/GreenSaturdaysAI/src/')
import utils

#Llamada al df

root = "/content/GreenSaturdaysAI/datasets/"
df = utils.mediciones_unif(root+'medidas/', root+'/estaciones/2021/', root+'/meta/')
df = utils.add_festivos_findes(df)


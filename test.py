import numpy as np
import pandas as pd

def main():
    path = 'C:\Users\cesar\Desktop\Proyecto\GreenSaturdaysAI\datasets\estaciones\2018\2018_qualitat_aire_estaciones_bcn.csv'
    path.replace('\'','/')
    hola = pd.read_csv(path)
    print(hola.describe())
    print(hola.head())




if __name__ == '__main__':
    import sys
    sys.exit(main())



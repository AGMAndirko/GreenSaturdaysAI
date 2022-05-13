import pandas as pd
import datetime
import utils

df = utils.mediciones_unif()

#obtenemos df mediciones

df_cont = utils.mediciones_unif()

df = pd.read_csv("../content/2020-21.csv")

df["covid"] = 0
df["fecha"] = df[["DIA", "MES", "ANY"]].astype(str).agg('/'.join, axis = 1)

festivos = ["1/1/2018","6/1/2018","30/3/2018","2/4/2018","1/5/2018","21/5/2018","15/8/2018","11/9/2018","24/9/2018","12/10/2018","1/11/2018","6/12/2018","8/12/2018","25/12/2018","26/12/2018","1/1/2019","6/1/2019","19/4/2019","22/4/2019","1/5/2019","10/6/2019","15/8/2019","11/9/2019","24/9/2019","12/10/2019","1/11/2019","6/12/2019","8/12/2019","25/12/2019","26/12/2019","1/1/2020","6/1/2020","10/4/2020","13/4/2020","1/5/2020","1/6/2020","24/6/2020","15/8/2020","11/9/2020","24/9/2020","12/10/2020","8/12/2020","25/12/2020","26/12/2020","1/1/2021","6/1/2021","2/4/2021","5/4/2021","1/5/2021","24/6/2021","11/9/2021","12/10/2021","1/11/2021","6/12/2021","8/12/2021","25/12/2021"]
#[lambda x: datetime.datetime.strftime(datetime.datetime.strptime(x, '%d/%m/%Y'),'%d/%m/%Y') for x in festivos]
#[lambda x: datetime.datetime.strftime(datetime.datetime.strptime(x, '%d/%m/%Y'),'%d/%m/%Y') for x in fechas]

df['festivo'] = 100
df['festivo'] = df['fecha'].apply(lambda x: 1 if x in festivos else 0)

#intentando sacar fines de semana también:
#[datetime.datetime.strptime(x, '%d/%m/%Y'),'%d/%m/%Y') for x in df['fecha']]





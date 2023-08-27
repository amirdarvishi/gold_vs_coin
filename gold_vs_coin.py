import pandas as pd 
import matplotlib.pyplot as plt
import datetime

gold_gram = pd.read_csv('geram18_D.txt')
rob = pd.read_csv('rob_D.txt')
# <Ticker> <Per>  <DTYYYYMMDD>  <TIME>    <OPEN>    <HIGH>     <LOW>   <CLOSE>  <TSEClose>

gold_gram = gold_gram[['<Ticker>','<DTYYYYMMDD>','<CLOSE>']]
rob = rob[['<Ticker>','<DTYYYYMMDD>','<CLOSE>']]

gold_gram['close22'] = (gold_gram['<CLOSE>'] * (22/18)).astype(int)

df_complete = pd.merge(gold_gram,rob,how='inner',on='<DTYYYYMMDD>')
df_complete['indice'] = df_complete['<CLOSE>_y']/df_complete['close22']

years = [str(y)[:4] for y in df_complete['<DTYYYYMMDD>']]
months = [str(m)[4:6] for m in df_complete['<DTYYYYMMDD>']]

dates = [datetime.date(int(y),int(m),1) for y,m in zip(years,months)]

df_complete['date'] = dates

plt.plot(df_complete['date'],df_complete['indice'])
plt.xlabel('date')
plt.ylabel('indice')
plt.axhline(y=2.5,color ='r')
plt.show()

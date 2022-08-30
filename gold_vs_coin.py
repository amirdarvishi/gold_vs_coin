import pandas as pd
import matplotlib.pyplot as plt 
import datetime

gold_gram = pd.read_csv('geram18_D.txt')
rob = pd.read_csv('rob_D.txt')

gold_gram = gold_gram[['<Ticker>','<DTYYYYMMDD>','<CLOSE>']]
rob = rob[['<Ticker>','<DTYYYYMMDD>','<CLOSE>']]

gold_gram['close22'] = (gold_gram['<CLOSE>']* (22 /18)).astype(int)

complete_df = pd.merge(gold_gram,rob,on = '<DTYYYYMMDD>',how = 'inner')

complete_df['indice'] = complete_df['<CLOSE>_y'] / complete_df['close22']

years = [str(y)[:4] for y in complete_df['<DTYYYYMMDD>']]
months = [str(m)[4:6] for m in complete_df['<DTYYYYMMDD>']]

dates = [datetime.date(int(y),int(m),1) for y,m in zip(years, months)]
complete_df['date'] = dates

plt.plot(complete_df['date'], complete_df['indice'])
plt.axhline(y=2.5,color = 'r')
plt.xlabel('Date')
plt.ylabel('indice')
plt.show()

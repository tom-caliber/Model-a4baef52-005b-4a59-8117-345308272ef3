'''
Generate dummy timeseries
'''
from sygmoid.imports import *

mode = 42
spread = 11.7

days = np.arange('2016-01', '2016-02', dtype='datetime64[D]') #arange for evenly spaced values in an interval
n_days = len(days)

dist = np.random.gumbel(loc=mode,scale=spread,size=n_days)  #gumbel distribution to model extreme maximas or minimas
dist[dist < 0] = 0

df = pd.DataFrame({'Val':dist},index=days)
#print(type(df))
df.to_csv('04-ts.csv')
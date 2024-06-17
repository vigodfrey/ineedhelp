import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
resultDF = pd.DataFrame({'robot':[],'human':[]})

for item in data.values:
    if item == 'robot':
        resultDF.loc[len(resultDF)] = {'robot':[1], 'human':[0]}
    else:
        resultDF.loc[len(resultDF)] = {'robot': [0], 'human': [1]}
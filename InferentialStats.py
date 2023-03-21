#Infernetial stats
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

from statsmodels.stats.outliers_influence import variance_inflation_factor
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

MainDF = pd.read_excel('PartiesV12.xlsx')

headers = []
count = 0
for i in MainDF.columns:
    headers.append(i)
    #print(f'{count}={headers[count]}')
    count+=1


#Get all traits higher than 0
TraitsDF = MainDF[headers[14:24]]
Traits = headers[14:24]
for i in Traits:
    TraitsDF = TraitsDF[TraitsDF[i]>-1]
    TraitsDF = TraitsDF[TraitsDF[i]<100]

#show histogram for entire DF
TraitsDF.hist()
plt.show()

#calculate correlation for entire DF
print(TraitsDF.corr())

#TraitsDF['Int_Trust'] = TraitsDF.apply(lambda x: (x['Integrity'] + x['Trustworthiness'])/2,axis=1)
#TraitsDF['Warm_Emp'] = TraitsDF.apply(lambda x: (x['Warmth'] + x['Empathy'])/2,axis=1)
#TraitsDF['Comp_Exp'] = TraitsDF.apply(lambda x: (x['Competence'] + x['Expertise'])/2,axis=1)
#TraitsDF['Fim_Sim'] = TraitsDF.apply(lambda x: (x['Familiarity'] + x['Similarity'])/2,axis=1)
#TraitsDF = TraitsDF.drop(['Integrity','Trustworthiness','Warmth','Empathy','Competence','Expertise','Familiarity','Similarity'], axis = 1)

# VIF dataframe
vif_data = pd.DataFrame()
vif_data["feature"] = TraitsDF.columns
  
# calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(TraitsDF.values, i)
                          for i in range(len(TraitsDF.columns))]
  
print(vif_data)
print(TraitsDF.corr())
#print(TraitsDF.mode(numeric_only=True))


'''

#split DF by a value in a column
PolDF = MainDF[MainDF['Condition'] =='POLITICALLEADER']
OrgDF = MainDF[MainDF['Condition']== 'ORGANISATIONALLEADER']

#Only include Rows that have a score of 0 and higher
PlotDF = MainDF[MainDF['Competence']>-1]


PlotDF.hist(column='Competence',bins=3)


plt.show()
'''

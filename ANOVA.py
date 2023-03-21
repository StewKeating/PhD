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
   # print(f'{count}={headers[count]}')
    count+=1

#1,6,7,8,13,26,27,28
#Get all traits higher than 0
DF = MainDF.filter(['Age','EduLevel','RecentVote','AlwaysSameParty',
                    'Line','LikeLeaders','HearFrom','ExpertInArea'],axis=1)
#print(DF['RecentVote'].value_counts())
#print(DF['EduLevel'].value_counts())
#print(DF['LikeLeaders'].value_counts())
print(DF['HearFrom'].value_counts())
#print(DF['ExpertInArea'].value_counts())


#print(TraitsDF)
#Traits = headers[14:24]
#for i in Traits:
#    TraitsDF = TraitsDF[TraitsDF[i]>-1]
#    TraitsDF = TraitsDF[TraitsDF[i]<100]

#ANOVA
    #Age by Voted for
    #Education by number line

    #Age by line

#chi square
    #voted for by education

#always vote for the same party
#important to like leaders
#important for leaders to be experts
#how often to hear from them
    

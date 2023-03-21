# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

#Descriptive stats
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)


MainDF = pd.read_excel('PartiesV12.xlsx')
#print(MainDF.columns)

Condition = 'POLITICALLEADER'
#Condition = 'ORGANISATIONALLEADER'
PoliticalParty = 'LIBDEM'
#'LABOUR','CONSERVATIVE','LIBDEM','SNP','GREEN','NO VOTE'


MainDF = MainDF.drop([ 'Age', 'Ethnicity', 'sex', 'GenderSameAsBirth',
       'GenderID', 'AlwaysSameParty', 'DescribeParty', 'MemberOfParty', 'MemberWhich',
       'OtherParty', 'Line','LeaderInMind', 'LikeLeaders', 'HearFrom','ExpertInArea', 'AnythingElse',
       'mt1', 'mt1n', 'mt2', 'mt2n', 'mt3', 'mt3n', 'mt4', 'mt4n',
       'mt5', 'mt5n', 'mt6', 'mt6n', 'mt7', 'mt7n', 'mt8', 'mt8n', 'mt9',
       'mt9n', 'mt10', 'mt10n', 'mt11', 'mt11n', 'mt12', 'mt12n', 'mt13',
       'mt13n'],axis=1)

#print(MainDF.columns)
#'ProlificID','Competence', 'Integrity', 'Trustworthiness', 'Charisma', 'Empathy',
#       'Warmth', 'Expertise', 'Similarity', 'Familiarity', 'Likeability',
#       'Attractiveness', 'Condition', 'EduLevel', 'RecentVote'

MainDF = MainDF.drop(['ProlificID','EduLevel'],axis=1)
#print(MainDF['Condition'])

match Condition:
    case 'POLITICALLEADER':
        Leader = MainDF[MainDF['Condition']=='POLITICALLEADER']
        Cond = 'Org'
    case 'ORGANISATIONALLEADER':
        Leader = MainDF[MainDF['Condition']=='ORGANISATIONALLEADER']       
        Cond = 'Pol'
#match Leader['Condition'].iloc[0]:
#    case "ORGANISATIONALLEADER":
#        Cond = 'Org'
#    case "POLITICALLEADER":
#        Cond = 'Pol'

#Leader = Leader[Leader['RecentVote']=='LABOUR']

match PoliticalParty:#Leader['RecentVote'].iloc[0]:
    case "LABOUR":
        Leader = Leader[Leader['RecentVote']=='LABOUR']
        Vote = 'Lab'
    case "CONSERVATIVE":
        Leader = Leader[Leader['RecentVote']=='CONSERVATIVE']
        Vote = 'Con'
    case "LIBDEM":
        Leader = Leader[Leader['RecentVote']=='LIBDEM']
        Vote = 'Lib'
    case "SNP":
        Leader = Leader[Leader['RecentVote']=='SNP']
        Vote = 'SNP'
    case "GREEN":
        Leader = Leader[Leader['RecentVote']=='GREEN']
        Vote = 'Grn'
    case "NO VOTE":
        Leader = Leader[Leader['RecentVote']=='NO VOTE']
        Vote = 'No vote'

Nrow = Leader[Leader.columns[0]].count() 

Leader = Leader.drop(['Condition','RecentVote'],axis=1)
#PolComp = Leader[Leader['Integrity']>0]
#PolComp = PolComp['Integrity'].mean()
#print(PolComp)


#Where Leader['Column'] >0 give the mean only for that column
#(otherwise it does means on other columns that arent correct
#as its removing rows in col 1 but also giving mean in col 2 with a row missing)
#PC = Leader[Leader['Integrity']>0]['Integrity'].mean()

#Get Mean() for all columns, if greater than 0
Vals = [1]
Cols = ['ProlificID']
for i in Leader.columns:
   # print(i)
    print(Leader[Leader[i]>-1][i].mean())
    M = Leader[Leader[i]>-1][i].mean()
    Vals.append(M)
    Cols.append(i)

Leader2 = pd.DataFrame([Vals],columns=Cols)
#print(PolDF2)

# number of variable
categories=list(Leader2)[1:]
categories = ['3','2','1','11','10','9','8','7','6','5','4']
#print(categories)
N = len(categories)
 
# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values=Leader2.loc[0].drop('ProlificID').values.flatten().tolist()
values += values[:1]
values
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=20)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30,40,50,60,70,80,90,100], ["10","20","30","40","50","60","70","80","90","100"], color="grey", size=7)
plt.ylim(0,100)
 
# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
# Fill area
ax.fill(angles, values, 'k', alpha=0.1)

my_title = f'Condition: {Cond}\n Recent Vote: {Vote}\n N: {Nrow}'
plt.title(my_title,y=0.95,x=-0.1, fontsize=10)

# Save the graph
plt.savefig(f'{Cond}_{Vote}.png')
# Show the graph
plt.show()

#1 - Trustworthiness
#2 - Integrity
#3 - Competence
#4 - Attractiveness
#5 - Likeability
#6 - Familiarity
#7 - Similarity
#8 - Expertise
#9 - Warmth
#10 - Empathy
#11 - Charisam



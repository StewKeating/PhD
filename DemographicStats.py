#Descriptive stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)


MainDF = pd.read_excel('PartiesV12.xlsx')
#print(MainDF.columns)
#print(MainDF['Ethinicity'].value_counts())
#print(MainDF.describe())
#print(MainDF.head())

print(MainDF['Age'].describe())

SexNum =  MainDF['sex'].value_counts()
GsaBNum =  MainDF['GenderSameAsBirth'].value_counts()
GenderIDNum = MainDF['GenderID'].value_counts()
EduNum =  MainDF['EduLevel'].value_counts()
VoteNum = MainDF['RecentVote'].value_counts()
SamePartyNum =  MainDF['AlwaysSameParty'].value_counts()
CondNum =  MainDF['Condition'].value_counts()
EthniNum = MainDF['Ethnicity'].value_counts()
Leader = MainDF['LeaderInMind'].value_counts()

likeleader= MainDF['LikeLeaders'].value_counts()
hearfrom= MainDF['HearFrom'].value_counts()
expertiseinarea= MainDF['ExpertInArea'].value_counts()

#split DF by a value in a column
PolDF = MainDF[MainDF['Condition'] =='POLITICALLEADER']
OrgDF = MainDF[MainDF['Condition']== 'ORGANISATIONALLEADER']

PolFreq = PolDF['HearFrom'].value_counts()
OrgFreq = OrgDF['HearFrom'].value_counts()

print(PolFreq)
print(OrgFreq)

#print(PolDF['RecentVote'].value_counts())
#print(OrgDF['RecentVote'].value_counts())
'''
mt1 =  MainDF['mt1'].value_counts()
mt2 =  MainDF['mt2'].value_counts()
mt3 =  MainDF['mt3'].value_counts()
mt4 =  MainDF['mt4'].value_counts()
mt5 =  MainDF['mt5'].value_counts()

print(mt1)
print('##')
print(mt2)
print('##')
print(mt3)
print('##')
print(mt4)
print('##')
print(mt5)
'''

'''
print(Leader)
print(SexNum)
print(GsaBNum)
print(GenderIDNum)
print(EduNum)
print(VoteNum)
print(SamePartyNum)
print(CondNum)
print(EthniNum)
print(likeleader)
print(hearfrom)
print(expertiseinarea)
'''
#Scatter plot Age*Line
#scatter plot x*y
#plt.scatter(MainDF['Age'],MainDF['Line'])
#plt.show()
#plt.scatter(MainDF.index,MainDF['Line'])
#plt.show()
'''
#Plot by index on X, plot line on Y, separate colours based on political party
Colours = {'LABOUR':'red','CONSERVATIVE':'blue','NO VOTE':'black','LIBDEM':'orange','GREEN':'green','OTHER<5':'grey','SNP':'yellow','I NO VOTE':'black'}
plt.scatter(MainDF.index,MainDF['Line'],c= MainDF['RecentVote'].map(Colours),cmap='viridis')

#Create singular instance of a label and colour
red_p = mpatches.Patch(color='red', label='Lab')
blue_p = mpatches.Patch(color='blue', label='Con')
black_p = mpatches.Patch(color='black', label='No vote')
orange_p = mpatches.Patch(color='orange', label='LibDem')
green_p = mpatches.Patch(color='green', label='Green')
yellow_p = mpatches.Patch(color='yellow', label='SNP')
grey_p = mpatches.Patch(color='grey', label='Other <5')

#bbox_to_anchor is to make it above the graph
#mode = expand makes it the length of the total graph
#ncol gives it the number of columns
plt.legend(handles=[red_p, blue_p,orange_p,green_p,yellow_p,grey_p, black_p],bbox_to_anchor=(0., 1.02, 1., .102),mode='expand',ncol=7)

xlab = 'Left                    Central                    Right'
plt.ylabel(f'{xlab}')#Left leaning          Centrist        Right leaning")
plt.xlabel('Participant number')
plt.show()
'''

#very useful for annotating a grpah
#plt.annotate("here",xy=(2, 5), xycoords='axes points',xytext=(-1, 2), textcoords='data',arrowprops=dict(arrowstyle="->",connectionstyle="arc3"),)

#https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html#sphx-glr-gallery-text-labels-and-annotations-text-alignment-py
#plt.text(left, 0.5 * (bottom + top), 'right center',
#        horizontalalignment='right',
#        verticalalignment='center',
#        rotation='vertical',
#        transform=plt.transAxes)



#plt.show()

#print(EthniNum)
#print(EduNum)
#plt.hist(MainDF['RecentVote'],bins=20,align='left')
#plt.show()

#EthniNum.plot(kind='bar')
#plt.show()
#SexNum.plot(kind='bar')
#plt.show()
#GsaBNum.plot(kind='bar')
#plt.show()
#GenderIDNum.plot(kind='bar')
#plt.show()
#EduNum.plot(kind='bar')
#plt.show()
#VoteNum.plot(kind='bar')
#plt.show()
#SamePartyNum.plot(kind='bar')
#plt.show()
#CondNum.plot(kind='bar')
#plt.show()
#MainDF.to_excel("PartiesV2.xlsx",sheet_name="sheet1",index=False)

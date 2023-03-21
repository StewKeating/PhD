#Scatter
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

#DF = pd.read_excel('O:\PHD\Assignments_Stew_PHD\Study1\Data\PartiesV11.xlsx')

DF = pd.read_excel('C:/Users/28415/OneDrive - The University of Winchester/PHD/Assignments_Stew_PHD/Study1/Data/PartiesV11.xlsx')

print(DF.columns)

#get rows with labour and conservative in recent vote column
SubDF = DF[DF['RecentVote'].isin(['LABOUR','CONSERVATIVE','GREEN','LIBDEM','SNP','NO VOTE'])]

#fig, ax = plt.subplots()

#set colours to use
colors = {'CONSERVATIVE':'blue', 'LABOUR':'red','GREEN':'green', 'LIBDEM':'orange', 'SNP':'yellow','NO VOTE':'black'}
Label=['cons','lab','lib','grn','snp','nvt']
#only use rows with values in competence over -1

#13 items in var list
var1= ['Age','Line','Competence', 'Integrity','Trustworthiness', 'Charisma','Empathy',
'Warmth', 'Expertise','Similarity', 'Familiarity','Likeability','Attractiveness']

var2=['Age','Line','Competence', 'Integrity','Trustworthiness', 'Charisma','Empathy',
'Warmth', 'Expertise','Similarity', 'Familiarity','Likeability','Attractiveness']

var1no = 2
var2no = 6


PlotDF = SubDF[SubDF[var1[var1no]]>-1]
PlotDF = PlotDF[PlotDF[var2[var2no]]>-1]

#DF = CompDF[SubDF['Expertise']>-1]

#plot x axis , by y axis,using the colours
#plotted = ax.scatter(PlotDF[var2[var2no]], PlotDF[var1[var1no]], c=PlotDF['RecentVote'].map(colors))
#plt.xlabel(f'{var2[var2no]} rating 0-100')
#plt.ylabel(f'{var1[var1no]} rating 0-100')
#plt.title(f'Scatter plot of {var2[var2no]} by {var1[var1no]}')
#plt.legend(hndles=loc='lower right')
#print(plotted.legend_elements())
#plt.show()
#plt.savefig("one4.png")
#ProlificID

#Create singular instance of a label and colour
red_p = mpatches.Patch(color='red', label='Lab')
blue_p = mpatches.Patch(color='blue', label='Con')
black_p = mpatches.Patch(color='black', label='No vote')
orange_p = mpatches.Patch(color='orange', label='LibDem')
green_p = mpatches.Patch(color='green', label='Green')
yellow_p = mpatches.Patch(color='yellow', label='SNP')


plotted = plt.scatter(PlotDF[var2[var2no]], PlotDF[var1[var1no]], c=PlotDF['RecentVote'].map(colors))
plt.xlabel(f'{var2[var2no]} rating 0-100')
plt.ylabel(f'{var1[var1no]} rating 0-100')
plt.title(f'Scatter plot of {var2[var2no]} by {var1[var1no]}')
plt.legend(handles=[red_p, blue_p,orange_p,green_p,yellow_p, black_p],bbox_to_anchor=(0., 1.06, 1., .107),mode='expand',ncol=7)
plt.savefig("one4.png")
plt.show()

'''
for i in range(0,len(var1)):
    PlotDF = SubDF[SubDF[var1[i]]>-1]
    for j in range(0,len(var2)):
        PlotDF = PlotDF[PlotDF[var2[j]]>-1]
        plotted = plt.scatter(PlotDF[var2[j]], PlotDF[var1[i]], c=PlotDF['RecentVote'].map(colors))
        plt.xlabel(f'{var2[j]} rating 0-100')
        plt.ylabel(f'{var1[i]} rating 0-100')
        plt.title(f'Scatter plot of {var2[j]} by {var1[i]}')
        plt.legend(handles=[red_p, blue_p,orange_p,green_p,yellow_p, black_p],bbox_to_anchor=(0., 1.06, 1., .107),mode='expand',ncol=7)
        plt.savefig(f'{var2[j]}_by_{var1[i]}.png')
       # plt.show()
        plt.close()
'''


#'LikeLeaders','ExpertInArea','Sex', 'GenderID'

#'HearFrom','RecentVote''EduLevel','AlwaysSameParty'

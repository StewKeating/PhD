#KMeans
from sklearn.cluster import KMeans
from scipy.cluster.vq import kmeans, vq as km, vq
import matplotlib.pyplot as plt
import pandas as pd
import os

cwd = os.getcwd()

df = pd.read_excel('PartiesV11.xlsx')

#13 items in var list
var1= ['Age','Line','Competence', 'Integrity','Trustworthiness', 'Charisma','Empathy',
'Warmth', 'Expertise','Similarity', 'Familiarity','Likeability','Attractiveness']

var2=['Age','Line','Competence', 'Integrity','Trustworthiness', 'Charisma','Empathy',
'Warmth', 'Expertise','Similarity', 'Familiarity','Likeability','Attractiveness']

var1no = 6
var2no = 2


PlotDF = df[df[var1[var1no]]>-1]
PlotDF = PlotDF[PlotDF[var2[var2no]]>-1]

x = PlotDF[[var1[var1no],var2[var2no]]].copy()
'''
for i in range(0,len(var1)):
    PlotDF = df[df[var1[i]]>-1]
    for j in range(0,len(var2)):
        wcss = []
        PlotDF = PlotDF[PlotDF[var2[j]]>-1]
        x = PlotDF[[var1[i],var2[j]]].copy()
        for k in range(1,11):
            kmeans = KMeans(n_clusters=k, random_state=0)
            kmeans.fit(x)
            wcss.append(kmeans.inertia_)
        plt.plot(range(1,11),wcss)
        plt.xlabel(f'Number of clusters')
        plt.ylabel(f'Within cluster sum of squares')
        plt.title(f'Elbow chart for determining cluster number {var2[j]} by {var1[i]}')
        plt.savefig(f'{cwd}\\ScatterPlots\\Elbow{var1[i]}by{var2[j]}.png')
        #plt.show()
        plt.close()

'''
'''
#Elbow method using sklearn
wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
#plt.savefig('Elbow.png')
plt.show()
'''

#Cluster analysis using the elbow as indicator of cluster
#uses scipy.cluster.vq
varX = x.columns[0]
varY = x.columns[1]
x[varX] = x[varX].astype(float)
x[varY] = x[varY].astype(float)
cluster_centers, _ = kmeans(x[[varX, varY]],3)
x['cluster_labels'],_ = vq(x[[varX, varY]], cluster_centers)
x['cluster_labels'] = x['cluster_labels'].astype(str)
Colours = {'0':'red','1':'blue','2':'green','3':'yellow','4':'black'}

plt.scatter(x[varX], x[varY], c=x['cluster_labels'].map(Colours), cmap='viridis')
plt.xlabel(f'{varX}')
plt.ylabel(f'{varY}')
plt.title(f'Clusters of {varX} by {varY}')
plt.savefig(f'{cwd}\\ScatterPlots\\Cluster_{varX}_by_{varY}.png')
plt.show()


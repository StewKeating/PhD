import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    random_state=42
    )
print(features[:5])
print(true_labels[:5])


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)
print(scaled_features[:5])


kmeans = KMeans(
    init='random',
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
    )
kmeans.fit(scaled_features)
kmeans.inertia_
kmeans.cluster_centers_
kmeans.n_iter_
kmeans.labels_[:5]
print(kmeans.fit(scaled_features))
print(kmeans.inertia_)
print(kmeans.cluster_centers_)
print(kmeans.n_iter_)
print(kmeans.labels_[:5])

kmeans_kwargs = {"init":"random",
                 "n_init":10,
                 "max_iter":300,
                 "random_state":42,
                 }

sse = []
for k in range(1,11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    sse.append(kmeans.inertia_)
#plt.style.use("fivethirtyeight")
#plt.plot(range(1,11),sse)
#plt.xticks(range(1,11))
#plt.xlabel('number of clusters')
#plt.ylabel('sse')
#plt.show()


k1 = KneeLocator(
    range(1,11),sse,curve='convex',direction='decreasing'
    )

print(k1.elbow)


silhouette_coefficients = []
for k in range(2,11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)

plt.style.use("fivethirtyeight")
plt.plot(range(2,11), silhouette_coefficients)
plt.xticks(range(2,11))
plt.xlabel("number of clusters")
plt.ylabel("silhouette coefficient")
plt.show()
    




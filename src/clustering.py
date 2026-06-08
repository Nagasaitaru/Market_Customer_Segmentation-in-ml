from sklearn.cluster import KMeans

def elbow_method(data):

    wcss=[]

    for i in range(1,11):

        model=KMeans(
            n_clusters=i,
            random_state=42
        )

        model.fit(data)

        wcss.append(model.inertia_)

    return wcss

def apply_kmeans(data):

    model=KMeans(
        n_clusters=3,
        random_state=42
    )

    labels=model.fit_predict(data)

    return labels
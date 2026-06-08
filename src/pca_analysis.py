from sklearn.decomposition import PCA

def apply_pca(data):

    pca = PCA(n_components=2)

    reduced_data = pca.fit_transform(data)

    return reduced_data
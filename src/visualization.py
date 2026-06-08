import matplotlib.pyplot as plt

def plot_elbow(wcss):

    plt.figure(figsize=(8,5))

    plt.plot(
        range(1,11),
        wcss,
        marker='o'
    )

    plt.title("Elbow Method")

    plt.xlabel("Clusters")

    plt.ylabel("WCSS")

    plt.savefig(
        "outputs/elbow_method.png"
    )

def plot_clusters(data,labels):

    plt.figure(figsize=(8,5))

    plt.scatter(
        data[:,0],
        data[:,1],
        c=labels,
        cmap='viridis'
    )

    plt.title("PCA Customer Clusters")

    plt.savefig(
        "outputs/pca_clusters.png"
    )
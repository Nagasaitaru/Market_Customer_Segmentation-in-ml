import os
import matplotlib.pyplot as plt


def plot_elbow(wcss):

    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(8, 5))

    plt.plot(
        range(1, len(wcss) + 1),
        wcss,
        marker="o"
    )

    plt.title("Elbow Method")
    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")

    plt.savefig(
        "outputs/elbow_method.png"
    )

    plt.close()


def plot_clusters(data, labels):

    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(8, 5))

    plt.scatter(
        data[:, 0],
        data[:, 1],
        c=labels,
        cmap="viridis"
    )

    plt.title("PCA Customer Clusters")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")

    plt.savefig(
        "outputs/pca_clusters.png"
    )

    plt.close()
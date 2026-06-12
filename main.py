import os

from src.data_preprocessing import load_data
from src.data_preprocessing import preprocess_data

from src.rfm_analysis import create_rfm

from src.pca_analysis import apply_pca

from src.clustering import elbow_method
from src.clustering import apply_kmeans

from src.visualization import plot_elbow
from src.visualization import plot_clusters


def main():

    # Create outputs folder automatically
    os.makedirs("outputs", exist_ok=True)

    filepath = "dataset/Mall_Customers.csv"

    df = load_data(filepath)

    df = create_rfm(df)

    scaled_data, original_df = preprocess_data(df)

    # Elbow Method
    wcss = elbow_method(scaled_data)

    plot_elbow(wcss)

    # KMeans Clustering
    labels = apply_kmeans(scaled_data)

    # PCA
    pca_data = apply_pca(scaled_data)

    # Save cluster results
    original_df["Cluster"] = labels

    original_df.to_csv(
        "outputs/cluster_report.csv",
        index=False
    )

    # PCA Visualization
    plot_clusters(
        pca_data,
        labels
    )

    print("Project Completed Successfully!")
    print("Files saved in outputs folder")


if __name__ == "__main__":
    main()
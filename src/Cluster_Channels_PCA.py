import numpy as np
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def get_KMeans_cluster_MS_System(freqs, fft_data):

    # 1. Use only the positive frequencies
    pos_freqs = freqs > 0
    fft_mag = np.abs(fft_data[:, pos_freqs])  # shape: (60, N/2)

    # Optional: take log scale to compress dynamic range
    #fft_log_mag = np.log1p(fft_mag)

    # 2. Standardize across features
    X_scaled = StandardScaler().fit_transform(fft_mag)

    # 3. PCA
    pca = PCA(n_components=5)
    X_pca = pca.fit_transform(X_scaled)

    # 4. KMeans Clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    labels = kmeans.fit_predict(X_pca)

    # 5. Plot PCA projection with cluster labels
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='tab10', s=50)
    for i in range(len(labels)):
        plt.text(X_pca[i, 0], X_pca[i, 1], str(i), fontsize=8)
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    plt.title("PCA of FFT Magnitudes with KMeans Clusters")
    plt.colorbar(label="Cluster")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

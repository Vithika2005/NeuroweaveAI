import numpy as np
from sklearn.cluster import KMeans

# Example biological features:
# [sleep_hours, stress_level, activity_score]

def generate_bio_data():
    return np.array([
        [6, 7, 5],
        [5, 8, 4],
        [8, 3, 7],
        [7, 4, 6],
        [4, 9, 3],
        [9, 2, 8]
    ])


def train_phylo_model(data, n_clusters=2):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(data)
    return model


def get_user_cluster(model, user_data):
    cluster = model.predict([user_data])[0]

    if cluster == 0:
        return "High Stress Cluster"
    else:
        return "Balanced Health Cluster"

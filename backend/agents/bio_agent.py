from ml.phylo_graph import generate_bio_data, train_phylo_model, get_user_cluster

def bio_agent(user_features):
    """
    Bio Agent:
    - Clusters biological data
    - Assigns user to cluster
    """

    dataset = generate_bio_data()
    model = train_phylo_model(dataset)

    cluster = get_user_cluster(model, user_features)

    return {
        "agent": "bio_agent",
        "cluster": cluster,
        "features": user_features
    }

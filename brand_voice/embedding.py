import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(texts):
    return embedder.encode(texts)

def consistency_score(embeddings):
    sim_matrix = cosine_similarity(embeddings)
    n = sim_matrix.shape[0]
    upper_tri = sim_matrix[np.triu_indices(n, k=1)]
    return np.mean(upper_tri), np.std(upper_tri)

def outlier_files(embeddings, filenames, top_n=2):
    mean_emb = np.mean(embeddings, axis=0, keepdims=True)
    dists = 1 - cosine_similarity(embeddings, mean_emb).flatten()
    outlier_indices = np.argsort(dists)[-top_n:]
    return [filenames[i] for i in outlier_indices], dists
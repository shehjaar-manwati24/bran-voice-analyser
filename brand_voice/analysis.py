import pandas as pd
from .metrics import (
    average_sentence_length, readability_score, sentiment_polarity,
    passive_voice_percentage, formality_score
)
from .embedding import get_embeddings, consistency_score, outlier_files

def analyze_texts(texts, filenames):
    metrics = {
        "filename": [],
        "avg_sentence_length": [],
        "readability": [],
        "sentiment": [],
        "passive_voice_%": [],
        "formality": [],
    }
    for fname, text in zip(filenames, texts):
        metrics["filename"].append(fname)
        metrics["avg_sentence_length"].append(average_sentence_length(text))
        metrics["readability"].append(readability_score(text))
        metrics["sentiment"].append(sentiment_polarity(text))
        metrics["passive_voice_%"].append(passive_voice_percentage(text))
        metrics["formality"].append(formality_score(text))
    embeddings = get_embeddings(texts)
    mean_sim, std_sim = consistency_score(embeddings)
    outliers, dists = outlier_files(embeddings, filenames)
    metrics["cosine_dist_from_mean"] = dists
    metrics["outlier"] = [fname in outliers for fname in filenames]
    df = pd.DataFrame(metrics)
    summary = {
        "consistency_score_mean_similarity": mean_sim,
        "consistency_score_std": std_sim,
        "outlier_files": outliers,
    }
    return df, summary
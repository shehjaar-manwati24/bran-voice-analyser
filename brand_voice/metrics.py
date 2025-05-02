import textstat
from textblob import TextBlob
import spacy

nlp = spacy.load("en_core_web_sm")

def average_sentence_length(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    if not sentences:
        return 0
    total_words = sum(len([token for token in sent if token.is_alpha]) for sent in sentences)
    return total_words / len(sentences)

def readability_score(text):
    return textstat.flesch_reading_ease(text)

def sentiment_polarity(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def passive_voice_percentage(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    if not sentences:
        return 0
    passive_count = 0
    for sent in sentences:
        for token in sent:
            if token.dep_ in ("auxpass", "nsubjpass"):
                passive_count += 1
                break
    return 100 * passive_count / len(sentences)

def formality_score(text):
    doc = nlp(text)
    sentences = list(doc.sents)
    if not sentences:
        return 0
    avg_len = average_sentence_length(text)
    words = [token.text.lower() for token in doc if token.is_alpha]
    unique_words = set(words)
    vocab_complexity = len(unique_words) / (len(words) + 1e-5)
    return 0.7 * avg_len + 0.3 * (vocab_complexity * 100)
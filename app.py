import streamlit as st

st.set_page_config(page_title="Brand Voice Consistency Analyzer", layout="wide")

import pandas as pd
from brand_voice.analysis import analyze_texts

st.title("🗣️ Brand Voice Consistency Analyzer")
st.markdown("""
Upload one or more text samples (as `.txt` files or paste text directly) to analyze your brand's voice consistency.
""")

uploaded_files = st.file_uploader(
    "Upload one or more .txt files", type=["txt"], accept_multiple_files=True
)

st.markdown("Or paste your text samples below (one per box):")
num_samples = st.number_input("Number of samples to paste", min_value=0, max_value=10, value=0, step=1)
pasted_texts = []
for i in range(num_samples):
    text = st.text_area(f"Sample {i+1}", height=100)
    if text.strip():
        pasted_texts.append(text.strip())

samples = []
filenames = []

if uploaded_files:
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        samples.append(content)
        filenames.append(file.name)

if pasted_texts:
    for idx, text in enumerate(pasted_texts):
        samples.append(text)
        filenames.append(f"Pasted Sample {idx+1}")

if samples:
    st.success(f"Analyzing {len(samples)} sample(s)...")
    df, summary = analyze_texts(samples, filenames)
    st.subheader("📊 Analysis Report")

    # Highlight outlier rows
    def highlight_outlier(row):
        return ['background-color: #ffcccc' if row['outlier'] else '' for _ in row]

    st.dataframe(df.style.apply(highlight_outlier, axis=1))

    st.markdown("### Consistency Score")
    st.metric("Mean Similarity", f"{summary['consistency_score_mean_similarity']:.3f}")
    st.metric("Similarity Std Dev", f"{summary['consistency_score_std']:.3f}")

    st.markdown("### Outlier Samples")
    if summary['outlier_files']:
        st.warning(", ".join(summary['outlier_files']))
    else:
        st.info("No significant outliers detected.")

    st.download_button(
        label="Download CSV Report",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="brand_voice_report.csv",
        mime="text/csv"
    )

    st.subheader("📈 Visualizations")
    st.bar_chart(df.set_index('filename')[['avg_sentence_length', 'readability', 'formality']])
    st.line_chart(df.set_index('filename')['sentiment'])
    st.bar_chart(df.set_index('filename')['passive_voice_%'])

else:
    st.info("Upload files or paste text samples to begin analysis.")
# app.py

import streamlit as st
import pandas as pd
from phenotype_extractor import extract_phenotypes
from model import train_model

st.title("Headache Outcome Prediction – Prototype")

st.write("Synthetic-data demo for NLP-based phenotyping and explainable prediction.")

note = st.text_area("Paste clinical-style headache note")

if st.button("Analyse"):
    features = extract_phenotypes(note)
    df = pd.DataFrame([features])

    model = train_model()
    pred = model.predict(df)[0]
    proba = model.predict_proba(df)[0][1]

    st.subheader("Extracted Phenotypes")
    st.json(features)

    st.subheader("Predicted Risk")
    st.write("High risk of poor outcome" if pred == 1 else "Lower risk of poor outcome")
    st.write(f"Estimated risk score: {proba:.2f}")

    st.subheader("Feature Importance")
    importance = pd.Series(model.feature_importances_, index=df.columns)
    st.bar_chart(importance)

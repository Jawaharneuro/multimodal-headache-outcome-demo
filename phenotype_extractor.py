#phenotype_extractor.py

import re

def extract_phenotypes(text):
    text = text.lower()
    features = {
        "nausea": int("nausea" in text),
        "photophobia": int("photophobia" in text or "light sensitivity" in text),
        "aura": int("aura" in text),
        "unilateral_pain": int("one-sided" in text or "unilateral" in text),
        "daily_headache": int("daily" in text),
        "med_overuse": int("overuse" in text or "analgesic" in text)
    }
    return features

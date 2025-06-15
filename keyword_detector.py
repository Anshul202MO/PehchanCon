
import re

scam_keywords = [
    "guaranteed return", "instant profit", "double paisa", "asli tip", "solid tip",
    "link below", "download app", "best investment", "crypto se lakhpati",
    "stock guaranteed", "IPO sure shot", "multibagger", "100% return"
]

def detect_keywords(transcript):
    transcript_lower = transcript.lower()
    found_keywords = []
    timestamps = []
    for keyword in scam_keywords:
        matches = re.finditer(keyword.lower(), transcript_lower)
        for match in matches:
            found_keywords.append(keyword)
            timestamps.append(f"{match.start()}s")
    return found_keywords, timestamps

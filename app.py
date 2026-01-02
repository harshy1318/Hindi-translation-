import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(
    page_title="English → Hindi Translator",
    page_icon="🇮🇳",
    layout="centered"
)

st.title("🇮🇳 English → Hindi Translator")
st.markdown(
    """
    ✔ Works Offline  
    ✔ No API  
    ✔ Letters • Words • Sentences  
    ✔ Dictionary-based (Stable & Error-free)
    """
)

# ---------------- LARGE DICTIONARY ----------------
EN_HI = {

    # Pronouns
    "i": "मैं",
    "you": "आप",
    "he": "वह",
    "she": "वह",
    "it": "यह",
    "we": "हम",
    "they": "वे",
    "me": "मुझे",
    "him": "उसे",
    "her": "उसे",

    # Helping verbs
    "am": "हूँ",
    "is": "है",
    "are": "हैं",
    "was": "था",
    "were": "थे",
    "be": "होना",
    "been": "रहा",

    # Common verbs
    "go": "जाना",
    "come": "आना",
    "eat": "खाना",
    "drink": "पीना",
    "see": "देखना",
    "read": "पढ़ना",
    "write": "लिखना",
    "learn": "सीखना",
    "teach": "सिखाना",
    "make": "बनाना",
    "do": "करना",
    "say": "कहना",
    "know": "जानना",
    "think": "सोचना",
    "work": "काम करना",

    # Nouns
    "name": "नाम",
    "king": "राजा",
    "queen": "रानी",
    "man": "आदमी",
    "woman": "महिला",
    "child": "बच्चा",
    "people": "लोग",
    "country": "देश",
    "india": "भारत",
    "world": "दुनिया",
    "language": "भाषा",
    "school": "स्कूल",
    "book": "किताब",
    "teacher": "शिक्षक",
    "student": "छात्र",

    # Adjectives
    "big": "बड़ा",
    "small": "छोटा",
    "new": "नया",
    "old": "पुराना",
    "good": "अच्छा",
    "bad": "बुरा",
    "happy": "खुश",
    "sad": "दुखी",
    "easy": "आसान",
    "hard": "कठिन",

    # Prepositions
    "in": "में",
    "on": "पर",
    "at": "पर",
    "to": "को",
    "from": "से",
    "with": "के साथ",
    "for": "के लिए",
    "of": "का",

    # Greetings
    "hello": "नमस्ते",
    "hi": "नमस्ते",
    "thanks": "धन्यवाद",
    "thank": "धन्यवाद",
    "welcome": "स्वागत है",

    # Numbers
    "one": "एक",
    "two": "दो",
    "three": "तीन",
    "four": "चार",
    "five": "पांच",
}

# ---------------- TRANSLATION FUNCTION ----------------
def translate(text):
    words = text.lower().split()
    output = []

    for word in words:
        clean = word.strip(".,!?")
        if clean in EN_HI:
            output.append(EN_HI[clean])
        else:
            output.append(f"[{clean}]")

    return " ".join(output)

# ---------------- UI ----------------
text = st.text_input("Enter English text:")

if st.button("Translate"):
    if text.strip():
        st.subheader("📘 Hindi Translation")
        st.success(translate(text))
    else:
        st.warning("Please enter text.")

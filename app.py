import streamlit as st
from gtts import gTTS
import pandas as pd
import PyPDF2
from deep_translator import GoogleTranslator

st.title("Multilingual Storytelling with Accents")

st.write("Translate text into different languages and convert it into speech")

# Language options
languages = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Malayalam": "ml"
}

language = st.selectbox("Select Language", list(languages.keys()))

# Text input
text_input = st.text_area("Enter text")

# File upload
uploaded_file = st.file_uploader("Upload file", type=["txt","pdf","csv","xlsx"])

text_data = ""

if uploaded_file is not None:

    if uploaded_file.type == "text/plain":
        text_data = uploaded_file.read().decode()

    elif uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            text_data += page.extract_text()

    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        text_data = df.to_string()

    else:
        df = pd.read_excel(uploaded_file)
        text_data = df.to_string()

if text_input:
    text_data = text_input


if st.button("Translate and Convert to Speech"):

    if text_data == "":
        st.warning("Please enter text or upload a file")

    else:
        # 🌍 Free Translation
        translated_text = GoogleTranslator(
            source='auto',
            target=languages[language]
        ).translate(text_data)

        st.subheader("Translated Text")
        st.write(translated_text)

        # 🔊 Convert to speech
        tts = gTTS(translated_text, lang=languages[language])
        tts.save("output.mp3")

        audio_file = open("output.mp3","rb")
        st.audio(audio_file.read(), format="audio/mp3")

        with open("output.mp3","rb") as file:
            st.download_button(
                label="Download Audio",
                data=file,
                file_name="translated_audio.mp3",
                mime="audio/mp3"
            )
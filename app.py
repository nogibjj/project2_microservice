import gradio as gr
from transformers import pipeline
from gtts import gTTS

def audio(text):
    # Summarize the input text using the Hugging Face model
    # Load the pre-trained summarization model from Hugging Face
    summarizer =  pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, do_sample=False)[0]["summary_text"]
    # Convert the summary to audio using Google Text-to-Speech
    tts = gTTS(summary)
    tts.save("summary.mp3")
    return "summary.mp3"

def text_summary(text):
    # Summarize the input text using the Hugging Face model
    # Load the pre-trained summarization model from Hugging Face
    summarizer =  pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, do_sample=False)[0]["summary_text"]
    return summary

# using streamlit to create a web app to display the summary or play the audio

import streamlit as st

st.title("📌 Your Personal Audio Summary")
text = st.text_input("Enter text to summarize")

#choose between text summary or audio summary
option = st.selectbox("Choose between text summary  or audio summary", ("📃Text Summary", "🗣Audio Summary"))

if st.button("Summarize"):
    if option == "📃Text Summary":
        summary = text_summary(text)
        st.write(summary)
    if option == "🗣Audio Summary":
        file_path = audio(text)
        st.audio(file_path)

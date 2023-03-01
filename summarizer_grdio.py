from transformers import pipeline
import gradio as gr

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#transforming the summary into audio

def summarize_audio(text):
    summary = summarizer(text)
    return summary

# Create a Gradio interface

gr.Interface(summarize_audio, "textbox", "textbox").launch()
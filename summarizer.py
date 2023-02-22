from transformers import pipeline
import gradio as gr

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Define a function to generate the summary
def summarize(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Define the user interface
input_text = gr.inputs.Textbox(lines=15, label="Input Text")
output_text = gr.outputs.Textbox(label="Summary")

# Create the user interface and launch it
gr.Interface(summarize, inputs=input_text, outputs=output_text, title="Summarizer").launch()

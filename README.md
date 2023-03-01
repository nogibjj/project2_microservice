# Project2: Audio Summarizer via Streamlit, AWS EC2, HuggingFace Space

[![Python application test with Github Actions](https://github.com/nogibjj/fastapi_news/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/fastapi_news/actions/workflows/main.yml) !

## Project Workflow diagram
![project4_diagram](https://user-images.githubusercontent.com/112578755/204114921-dd0ffe8f-923a-4749-b7fd-313f9efc369b.jpg)

# Containerized Audio Summary App

`docker build .`


# Project purpose:

The project aims to build a Microservice that is able to take input (text) and return both text summary and audio version for users and perform Continuous Integration through Github Actions and configure Build Server to deploy changes on build (Continuous Delivery) using HuggingFace Space, AWS EC2. 

# Project process:
1. The summary pipeline was developed using Hugging Face text-to-text and text-to-speech models.
2. The microservice was pushed to poduction using streamlit (Gradio was leveraged to display the summarization interface, but the audio output cannot play successfully.)
3. Using Codespace as the environment, the microservice was containerized in Docker.
4. Continous Integration was enabled via Github Actions.

# Deployed domain 
`http://20.124.177.144:8501 `

# Example Output

<img width="1003" alt="Screen Shot 2023-03-01 at 11 34 46 AM" src="https://user-images.githubusercontent.com/112578755/222203131-7e338da7-05d9-4c90-9ad6-e2e619150e1e.png">

# Project2: Audio Summarizer via Streamlit, AWS EC2, HuggingFace Space

[![Python application test with Github Actions](https://github.com/nogibjj/fastapi_news/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/fastapi_news/actions/workflows/main.yml)

# Containerized Audio Summary App

* Connect your EC2 and github repo by using SSH keys
* Add your security group rule with port 8501 8502
* use the external link to access the web app

<img width="1003" alt="Screen Shot 2023-03-01 at 11 49 57 AM" src="https://user-images.githubusercontent.com/112578755/222207026-5c46a35c-5e3d-495a-91de-eae2f6191344.png">

(Due to EC2 costs, the instance has been stopped and the project would use free version of HuggingFace Space to deploy the web app instead.)


# Project purpose:

The project aims to build a Microservice that is able to take input (text) and return both text summary and audio version for users and perform Continuous Integration through Github Actions and configure Build Server to deploy changes on build (Continuous Delivery) using HuggingFace Space, AWS EC2. 

# Project process:
1. The summary pipeline was developed using Hugging Face text-to-text and text-to-speech models.
2. The microservice was pushed to poduction using streamlit (Gradio was leveraged to display the summarization interface, but the audio output cannot play successfully.)
3. Using Codespace as the environment, the microservice was containerized in Docker.
4. Continous Integration was enabled via Github Actions.

# Deployed domain 
* make sure you are using virtual environment to run the commands
* `make run`
* Access the web app via `http://20.124.177.144:8501 `or `https://huggingface.co/spaces/Emmawang/audio_summarizer`
* 
<img width="790" alt="Screen Shot 2023-03-01 at 12 47 21 PM" src="https://user-images.githubusercontent.com/112578755/222220573-730349d9-1e6e-44fa-993c-6e99ca925533.png">

# Example Output

<img width="1003" alt="Screen Shot 2023-03-01 at 11 34 46 AM" src="https://user-images.githubusercontent.com/112578755/222203131-7e338da7-05d9-4c90-9ad6-e2e619150e1e.png">

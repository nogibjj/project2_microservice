from fastapi import FastAPI
from podcast_api import search
import uvicorn
from transformers import pipeline

app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "what podcast do you want to listen?"}

# @app.get("/podcast/{query}")
# async def podcast(query: str):
#     return search(query)

# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')

@app.get("/")
async def root():
    return {"message": "lets summarize some text"}

@app.get("/summarize/{text}")
async def summarize(text: str):
    summarizer = pipeline("sshleifer/distilbart-cnn-12-6")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
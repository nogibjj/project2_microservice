from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")

from pydub import AudioSegment

audio_file = AudioSegment.from_file("/workspaces/project2_microservice/podcast/SGU/2023/2023.02.11 The Skeptics Guide #918 - Feb 11 2023.mp3", format="mp3")
raw_audio = audio_file.raw_data

import torch
import torchaudio

resampler = torchaudio.transforms.Resample(orig_freq=audio_file.frame_rate, new_freq=16_000)
audio_tensor = torch.from_numpy(raw_audio).float()
audio_tensor = resampler(audio_tensor)

inputs = tokenizer(audio_tensor, return_tensors="pt").input_values

with torch.no_grad():
    logits = model(inputs).logits

predicted_ids = torch.argmax(logits, dim=-1)
transcription = tokenizer.decode(predicted_ids[0])

import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import librosa
import soundfile as sf
from pydub import AudioSegment

# Load the pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")

# Load the audio file
audio_input, _ = librosa.load("test.wav", sr=16000)
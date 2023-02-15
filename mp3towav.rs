use std::fs::File;
use std::io::Read;
use speech_to_text::{SpeechClient, SpeechConfig};

fn main() {
    // Load the MP3 file into memory
    let mut file = File::open("audio.mp3").unwrap();
    let mut buffer = Vec::new();
    file.read_to_end(&mut buffer).unwrap();

    // Set up the speech client and configuration
    let config = SpeechConfig::from_env();
    let client = SpeechClient::new(&config);

    // Transcribe the audio data
    let result = client.recognize(&buffer, "mp3", 16000).unwrap();

    // Print the transcription
    println!("{}", result.text);
}

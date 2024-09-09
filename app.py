import os
import speech_recognition as sr
import requests
import pandas as pd
from flask import Flask, render_template, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Replace with your actual AssemblyAI API key
ASSEMBLYAI_API_KEY = ''

# Load your CSV with song data
df = pd.read_csv('songs.csv')  # Ensure the CSV has columns 'Title' and 'Lyric' ######
data = df.to_dict('records')

# Load pre-trained embedding model
embeddings_model = SentenceTransformer("sentence-transformers/nli-mpnet-base-v2")

# Create embeddings for the song lyrics
song_embeddings = embeddings_model.encode([d['Lyric'] for d in data], convert_to_tensor=True) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    print("called")
    print("-------")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:
        # Capture audio from the microphone
        with mic as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # Save the captured audio to a temporary WAV file
        # audio_filename = "speech.wav"
        # with open(audio_filename, "wb") as f:
        #     f.write(audio.get_wav_data())

        # Send the file to AssemblyAI for transcription
        # transcription = transcribe_with_assemblyai(audio_filename)
        
        # google
        transcription = recognizer.recognize_google(audio)

        # Remove the audio file after transcription
        os.remove(audio_filename)

        # Perform semantic search on the transcribed text
        search_results = semantic_search(transcription)

        return jsonify({"transcription": transcription, "search_results": search_results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def transcribe_with_assemblyai(audio_file_path):
    headers = {
        'authorization': ASSEMBLYAI_API_KEY,
        'content-type': 'application/json'
    }

    # Step 1: Upload the audio file to AssemblyAI
    upload_url = 'https://api.assemblyai.com/v2/upload'
    with open(audio_file_path, 'rb') as f:
        response = requests.post(upload_url, headers=headers, data=f)
        audio_url = response.json().get('upload_url')

    # Step 2: Request transcription
    transcript_url = 'https://api.assemblyai.com/v2/transcript'
    transcript_request = {
        'audio_url': audio_url
    }
    transcript_response = requests.post(transcript_url, json=transcript_request, headers=headers)
    transcript_id = transcript_response.json().get('id')

    # Step 3: Poll until the transcription is ready
    while True:
        transcript_result_url = f'{transcript_url}/{transcript_id}'
        transcript_result = requests.get(transcript_result_url, headers=headers).json()
        if transcript_result['status'] == 'completed':
            return transcript_result['text']
        elif transcript_result['status'] == 'failed':
            raise Exception('Transcription failed')

def semantic_search(query):
    # Encode the query using the same embeddings model
    query_embedding = embeddings_model.encode(query, convert_to_tensor=True)

    # Compute cosine similarity between the query and each song lyric embedding
    from torch import nn
    cosine_sim = nn.CosineSimilarity(dim=1)
    similarities = cosine_sim(query_embedding, song_embeddings)

    # Find the top 2 most similar results
    top_results_idx = similarities.argsort(descending=True)[:2]
    results = []

    for idx in top_results_idx:
        title = data[idx]['Title']
        lyric = data[idx]['Lyric']
        results.append({'Title': title, 'Lyric': lyric})

    return results

if __name__ == '__main__':
    app.run(debug=True)

# TuneInsight 🎶

Unlock the Secrets Behind Your Favorite Songs with AI!

TuneInsight is an AI-powered web app that identifies the song you're playing and provides detailed information. Using either an open-source AI model or Assembly AI, TuneInsight delivers a seamless song recognition experience, all through a simple, responsive web interface.

## 🌟 Features

- Instant Song Identification: Just play a song, and TuneInsight recognizes it using state-of-the-art AI models.
- Detailed Song Information: View artist, album, genre, and other insights about the song.
- Lightweight Web Interface: Built with HTML and CSS, offering a clean and fast interface.
- AI-driven Recommendations: Discover similar songs based on the music you play.
- Pretrained AI Model: Leverage either an open-source model or Assembly AI for accurate recognition.

## 🔧 Technology Stack

### Frontend:

- HTML5: Structure and content of the web page.
- CSS3: Styling for a visually appealing, responsive user interface.

### Backend:

- Flask: Python web framework to handle the backend processes.
- Pretrained AI Model: Using either an open-source model or Assembly AI to recognize songs from audio data.

## 🚀 Getting Started

### Prerequisites:

- Python 3.x
- Flask
- Required Python libraries (install via requirements.txt)
- Your own song dataset (e.g., .csv file)

### Installation Steps:

1. Clone the Repository:

```bash
git clone https://github.com/neeldevenshah/TuneInsight.git
cd TuneInsight
```

2. Set Up Backend: Navigate to the backend folder and install required dependencies:

```bash
cd backend
pip install -r requirements.txt
```

3. Modify Dataset: Update the song dataset before running the app:

- Replace Maroon5.csv with your own dataset.
- Ensure the dataset is placed correctly for the backend to process song data.

4. Run Backend: Start the Flask server:

```bash
python app.py
```

5. Run Frontend: Open the index.html file located in the root folder of the project in any web browser:

```bash
open index.html
```

## 🧠 AI Architecture

TuneInsight integrates a pretrained AI model for song recognition, allowing for fast and accurate music identification. The backend processes the song's audio features and matches them against the dataset to return detailed song insights. You have the flexibility to use:

- Open-source AI Models: Lightweight and customizable for local usage.
- Assembly AI: Cloud-based API for high-accuracy song recognition.

## 🔄 Data Handling

Ensure your song dataset (e.g., Maroon5.csv) is formatted with columns such as Song Name, Artist, Album, Genre, and Audio Features. This dataset feeds into the AI model for accurate song recognition.

## 🛠️ Future Enhancements

- Lyrics Synchronization: Display lyrics in real-time as the song plays.
- Extended Song Data: Include additional details like release date, album art, and background stories about the song.
- Advanced Recommendations: Use AI to suggest playlists based on song preferences.
- Multilingual Support: Expand song recognition and data display to multiple languages.

## 🙌 Contributing

We welcome contributions to TuneInsight! Feel free to submit pull requests or raise issues to suggest features or report bugs.

## 📜 License

This project is licensed under the MIT License.

## 📧 Contact

For any queries or support, feel free to reach out to the project maintainer at:

Email: neeldevenshah@gmail.com

Dive into your favorite music with TuneInsight and enjoy a whole new level of song recognition! 🎧

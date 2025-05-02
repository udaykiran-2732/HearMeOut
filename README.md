# HearMeOut
HearMeOut is an assistive tool designed for deaf and mute individuals. It converts sign language (A–Z) to text using OpenCV and includes text-to-speech and speech-to-text features for smoother communication. The project aims to bridge accessibility gaps and promote inclusive interaction using simple, real-time solutions.

Link: https://drive.google.com/drive/folders/1YYHm2RFWk3k8nQozAPWLI-2NzFWMr-YQ?usp=sharing



# 🎓 Hear Me Out – Bridging Communication Gaps

This repository contains **Hear Me Out**, an assistive web application that empowers **deaf, mute, and blind** individuals through AI-powered communication tools. Developed using **Django**, **HTML/CSS**, and **JavaScript**, it integrates multiple accessibility features on a single platform.

---

## 🖼️ Preview

### 🔊 Text-to-Speech Module  
![TTS Screenshot](images/tts.png)

### 🗣️ Speech-to-Text Module  
![STT Screenshot](images/stt.png)

### 🤟 Sign Language Recognition  
![Sign Language Screenshot](images/sign.png)



---

## 🎬 Demo

https://user-images.githubusercontent.com/your-username/your-video-id.mp4  


---

## 📌 Features

- 🔡 **Text-to-Speech (TTS):** Converts typed text or uploaded `.txt` / `.pdf` files into audio using dynamic voices.
- 🎙️ **Speech-to-Text (STT):** Live and file-based voice transcription into text.
- 🤟 **ASL Translator:** Detects American Sign Language gestures using webcam, converts them to text and speech in real-time.
- 🌍 **Multilingual & Custom Voices:** Choose voice type and language for TTS playback.
- 🗂️ **Document Support:** Upload and convert text documents to speech.
- ♻️ **Undo, Redo, Reset:** Full interaction control in the Sign Language interface.

---

## ⚙️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** gTTS, SpeechRecognition, OpenCV, Mediapipe

---

## 🛠️ Installation & Usage

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/hear-me-out.git
cd hear-me-out
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Django development server

```bash
python manage.py runserver
```

### 5️⃣ Open the app in your browser

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
hear-me-out/
├── templates/             # HTML files
├── static/                # CSS, JS, and media
├── images/                # Add your preview images here
├── app/                   # Django app folder
├── requirements.txt       # Project dependencies
├── manage.py              # Django management script
└── README.md              # You're reading it 👀
```

---

## 📊 Applications

- 🧏 Assisting individuals with speech, hearing, or visual impairments
- 🏫 Enhancing inclusion in schools, clinics, and public environments
- 💡 Promoting accessibility-first development practices

---

## 🚀 Future Scope

- Indian Sign Language (ISL) Support
- Emotion Detection
- Blind Accessibility (Screen Reader Integration)
- Assistive Device Compatibility (Smart Glasses, Gloves)

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.  
Don’t forget to ⭐ this repo if it helped you!

---

> Made with ❤️ to make communication universal.

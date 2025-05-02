# 🎓 Hear Me Out – Bridging Communication Gaps

This repository contains **Hear Me Out**, an assistive web application that empowers **deaf, mute, and blind** individuals through AI-powered communication tools. Developed using **Django**, **HTML/CSS**, and **JavaScript**, it integrates multiple accessibility features on a single platform.

---

## 🖼️ Preview

### 🔊 Text-to-Speech Module  
![TTS Screenshot]([https://drive.google.com/uc?export=view&id=YOUR_IMAGE_ID_1](https://drive.google.com/file/d/1h8yh9090G8niU8gwsSQIol5Q3wmD8C4z/view?usp=sharing))

### 🗣️ Speech-to-Text Module  
![STT Screenshot](https://drive.google.com/file/d/1l_g_cxcnWNGECtNOc04z0-DGx1qVJ91x/view?usp=sharing)

### 🤟 Sign Language Recognition  
![Sign Language Screenshot]([https://drive.google.com/uc?export=view&id=YOUR_IMAGE_ID_3](https://drive.google.com/file/d/1qivEOfmN55w1kH0cNybIDg_uHLxiHpOT/view?usp=sharing))

> 📁 These images are hosted on Google Drive. Make sure your files are shared publicly and you use the `FILE_ID` part from the Drive URL.

---

## 🎬 Demo

🎥 [Watch Demo Video](https://drive.google.com/file/d/1FvsMm-IoqFo_--KzgAZJ8HQXzI7EfNoc/view?usp=sharing)

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

### 2️⃣ Create a virtual environment

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
├── images/                # If hosting images locally
├── app/                   # Django app folder
├── requirements.txt       # Project dependencies
├── manage.py              # Django management script
└── README.md              # You're reading it 👀
```

---

## 🔗 External Files (Hosted on Google Drive)

- 📂 [ASL Sign Recognition Model Code](https://drive.google.com/file/d/YOUR_CODE_FILE_ID/view?usp=sharing)
- 📂 [Heavyweight NLP Script](https://drive.google.com/file/d/YOUR_NLP_FILE_ID/view?usp=sharing)

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

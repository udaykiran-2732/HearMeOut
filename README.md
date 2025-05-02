<h1 align="center">🎓 Hear Me Out – Bridging Communication Gaps</h1>
<p>This repository contains <strong>Hear Me Out</strong>, an assistive web application that empowers <strong>deaf, mute, and blind</strong> individuals through AI-powered communication tools. Developed using <strong>Django</strong>, <strong>HTML/CSS</strong>, and <strong>JavaScript</strong>, it integrates multiple accessibility features on a single platform.</p>

<hr>




<h2>🖼️ Preview</h2>
<h3>🔊 Text-to-Speech Module</h3>
<a href="https://ibb.co/tTpccM7f"><img src="https://i.ibb.co/tTpccM7f/Screenshot-2025-04-05-at-6-42-20-PM.png" alt="Screenshot-2025-04-05-at-6-42-20-PM" border="0" /></a>


<h3>🗣️ Speech-to-Text Module</h3>

<a href="https://ibb.co/1YQwLMfY"><img src="https://i.ibb.co/1YQwLMfY/Screenshot-2025-04-05-at-2-48-59-AM.png" alt="Screenshot-2025-04-05-at-2-48-59-AM" border="0"></a>

<h3>🤟 Sign Language Recognition</h3>
<a href="https://ibb.co/mCn41gY3"><img src="https://i.ibb.co/mCn41gY3/Screenshot-2025-04-13-at-6-11-41-PM.png" alt="Screenshot-2025-04-13-at-6-11-41-PM" border="0"></a>
<p>📁 These images are hosted on Imgbb. Make sure your files are shared publicly and you use the <strong>direct image URL</strong> to display them properly.</p>

<hr>

<h2>🎬 Demo</h2>
<p>🎥 <a href="https://drive.google.com/file/d/1FvsMm-IoqFo_--KzgAZJ8HQXzI7EfNoc/view?usp=sharing">Watch Demo Video</a></p>

<hr>

<h2>📌 Features</h2>
<ul>
    <li>🔡 <strong>Text-to-Speech (TTS):</strong> Converts typed text or uploaded .txt / .pdf files into audio using dynamic voices.</li>
    <li>🎙️ <strong>Speech-to-Text (STT):</strong> Live and file-based voice transcription into text.</li>
    <li>🤟 <strong>ASL Translator:</strong> Detects American Sign Language gestures using webcam, converts them to text and speech in real-time.</li>
    <li>🌍 <strong>Multilingual & Custom Voices:</strong> Choose voice type and language for TTS playback.</li>
    <li>🗂️ <strong>Document Support:</strong> Upload and convert text documents to speech.</li>
    <li>♻️ <strong>Undo, Redo, Reset:</strong> Full interaction control in the Sign Language interface.</li>
</ul>

<hr>

<h2>⚙️ Tech Stack</h2>
<ul>
    <li><strong>Backend:</strong> Django (Python)</li>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
    <li><strong>Libraries:</strong> gTTS, SpeechRecognition, OpenCV, Mediapipe</li>
</ul>

<hr>

<h2>🛠️ Installation & Usage</h2>
<p>Follow these steps to run the project locally:</p>
<h3>1️⃣ Clone the repository</h3>
<pre><code>git clone https://github.com/your-username/hear-me-out.git
cd hear-me-out</code></pre>
<h3>2️⃣ Create a virtual environment</h3>
<pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
<h3>3️⃣ Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>
<h3>4️⃣ Run the Django development server</h3>
<pre><code>python manage.py runserver</code></pre>
<h3>5️⃣ Open the app in your browser</h3>
<pre><code>http://127.0.0.1:8000</code></pre>

<hr>

<h2>📁 Project Structure</h2>
<pre><code>hear-me-out/
├── templates/             # HTML files
├── static/                # CSS, JS, and media
├── images/                # If hosting images locally
├── app/                   # Django app folder
</code></pre>

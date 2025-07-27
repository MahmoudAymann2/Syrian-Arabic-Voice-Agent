# Syrian-Arabic-Voice-Agent

<h1>🎙 Syrian Arabic Voice Agent - Charco Chicken</h1>

<p><strong>Charco Chicken</strong> is building a real-time voice ordering assistant to handle phone orders in flawless Syrian Arabic. This prototype demonstrates SIP-ready, real-time conversational AI using Google Cloud and Whisper.</p>

<hr />

<h2>🛠 Features</h2>
<ul>
  <li>📞 <strong>SIP Telephony Ready:</strong> Agent can be connected to Twilio or SIP Trunk</li>
  <li>🧠 <strong>Intent Detection:</strong> Order, Complaints, Greetings, Fallback</li>
  <li>🗣 <strong>Syrian Arabic Voice:</strong> Google TTS with Arabic prosody</li>
  <li>🔊 <strong>Speech-to-Text:</strong> Whisper for accurate Arabic transcription</li>
  <li>📦 <strong>Order API:</strong> Receives name and order, returns order ID + ETA</li>
  <li>🧪 <strong>Streamlit UI:</strong> Upload audio, see transcription + intent + TTS</li>
</ul>

<hr />

<h2>📁 Project Structure</h2>

<pre>
├── agent.py               # Orchestrates STT → Intent → TTS
├── stt.py                 # Whisper transcription
├── tts.py                 # Google Cloud TTS Arabic voice
├── intent_detector.py     # Rule-based Arabic intent detection
├── api.py                 # Flask backend for order processing
├── streamlit_ui.py        # Streamlit UI for testing agent
├── requirements.txt       # Python dependencies
├── google-key.json        # Google Cloud credentials (not uploaded)
├── sip_config.md          # SIP/Twilio connection notes
</pre>

<hr />

<h2>🚀 How to Run Locally</h2>

<ol>
  <li>Clone the repo:
    <pre>git clone https://github.com/your-username/syrian-voice-agent.git</pre>
  </li>
  <li>Navigate to the project:
    <pre>cd "Syrian Voice Agent"</pre>
  </li>
  <li>Create & activate virtual environment:
    <pre>python -m venv venv
venv\Scripts\activate</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Enable Google Cloud TTS:
    <ul>
      <li>Go to <a href="https://console.cloud.google.com/">Google Cloud Console</a></li>
      <li>Enable <strong>Text-to-Speech API</strong></li>
      <li>Create a Service Account, download JSON key</li>
    </ul>
  </li>
  <li>Set credentials:
    <pre>set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\google-key.json"</pre>
  </li>
  <li>Run UI:
    <pre>venv\Scripts\python.exe -m streamlit run streamlit_ui.py</pre>
  </li>
</ol>

<hr />

<h2>📦 API Endpoint</h2>

<pre><code>POST /submit-order</code></pre>
<p>Sample JSON:</p>
<pre>
{
  "name": "عميل مجهول",
  "order": ["فروج مشوي", "بطاطا"]
}
</pre>

Response:
<pre>
{
  "order_id": "1234-5678-90",
  "eta": "30 دقيقة"
}
</pre>

<hr />

<h2>📞 SIP Integration (Optional)</h2>
<p>Use Twilio SIP or any VoIP provider to connect phone calls:</p>
<pre>
&lt;Response&gt;
  &lt;Start&gt;&lt;Stream url="wss://your-server.com/audio" /&gt;&lt;/Start&gt;
  &lt;Say language="ar-SA"&gt;مرحبا بك في فروج شاركو!&lt;/Say&gt;
&lt;/Response&gt;
</pre>

<hr />

<h2>📊 Bonus (Not included yet)</h2>
<ul>
  <li>Monitoring dashboard (conversation logs)</li>
  <li>Replayable responses</li>
  <li>Multilingual extension (Arabic / English / Turkish)</li>
</ul>

<hr />

<h2>📽 Demo Video (Attach separately)</h2>
<ul>
  <li>✅ Live SIP call with Syrian voice</li>
  <li>✅ Order flow demo with transcription</li>
  <li>✅ UI flow via Streamlit</li>
</ul>

<hr />

<h2>👨‍💻 Built With</h2>
<ul>
  <li><strong>Python</strong> – Core language</li>
  <li><strong>Google Cloud TTS</strong> – Arabic voice output</li>
  <li><strong>Whisper</strong> – Speech-to-Text in Arabic</li>
  <li><strong>Streamlit</strong> – UI for test and validation</li>
  <li><strong>Flask</strong> – Simple backend API</li>
</ul>

<hr />

<h2>📩 Contact</h2>
<p>If you'd like to collaborate or have questions, open an issue or reach out via GitHub.</p>

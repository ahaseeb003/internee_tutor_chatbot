# Internee.pk Tutor Chatbot

A simple **Streamlit + LangChain** chatbot that guides interns through Internee.pk learning modules.  
It uses **OpenRouter’s free model Z.AI: GLM 4.5 Air** (`z-ai/glm-4.5-air`) as the backend.

## 🚀 Features
- Interactive web UI (Streamlit)
- Personalized tutor bot with memory
- Easy API key management (`.env` or sidebar)
- Runs locally with just Python

## 📦 Installation

1. Clone or download the project:
   ```bash
   git clone https://github.com/yourname/internee_tutor_chatbot.git
   cd internee_tutor_chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API keys:
   - Copy `.env.example` → `.env`
   - Add your **OpenRouter API key**:
     ```
     OPENROUTER_API_KEY=sk-xxxx
     OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
     MODEL=z-ai/glm-4.5-air
     ```

## ▶️ Run the App
```bash
streamlit run app.py
```

## 🔑 Notes
- Get a free API key from [OpenRouter](https://openrouter.ai/).
- Default model is `z-ai/glm-4.5-air` (Z.AI GLM 4.5 Air, free tier).

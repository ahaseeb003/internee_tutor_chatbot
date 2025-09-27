import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI


from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
MODEL = os.getenv("MODEL", "z-ai/glm-4.5-air")

st.set_page_config(page_title="Internee.pk Tutor Chatbot")
st.title("🤖 Internee.pk Tutor Chatbot")

st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("OpenRouter API Key", value=OPENROUTER_API_KEY, type="password")
model = st.sidebar.text_input("Model ID", value=MODEL)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2)
max_tokens = st.sidebar.number_input("Max tokens", 64, 2048, 512)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def make_llm():
    return ChatOpenAI(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=api_key,
        openai_api_base=OPENROUTER_BASE_URL,
    )

def generate_reply(user_text):
    llm = make_llm()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    prompt = PromptTemplate(
        input_variables=["input", "chat_history"],
        template="You are Internee.pk Tutor Bot. Help interns step by step.\n\nChat history:\n{chat_history}\nUser: {input}\nTutor:"
    )
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    return chain.run({"input": user_text, "chat_history": st.session_state.chat_history})

user_input = st.text_input("Ask me anything about Internee.pk learning modules:")

if st.button("Send") and user_input.strip():
    reply = generate_reply(user_input.strip())
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Tutor", reply))

for role, msg in st.session_state.chat_history:
    st.markdown(f"**{role}:** {msg}")

if st.button("Clear Chat"):
    st.session_state.chat_history = []

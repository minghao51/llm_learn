from groq import Groq
import streamlit as st
import os

#### Side Bar
with st.sidebar:
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


#### Main
st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by Groq LLM")

_temperature = st.slider('temperature', min_value=0.0, max_value=1.0, value=0.1, step=0.1)

## Actual ChatBot
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    client = Groq(
        api_key=os.environ.get("GROQ"),
    )
    
    

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = client.chat.completions.create(
        # Required
        model="mixtral-8x7b-32768", 
        messages=st.session_state.messages,
        # Optional
        temperature=_temperature,
    )
    
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})

    st.chat_message("assistant").write(msg)

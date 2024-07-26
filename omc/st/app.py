from dataclasses import dataclass
from functools import partial
import os
from pathlib import Path

import openai
import streamlit as st
from streamlit.components.v1 import html


@dataclass
class AppContext:
    pass


HERE = Path(__file__).parent
insert_html = partial(st.markdown, unsafe_allow_html=True)


def setup_page(config) -> AppContext:
    st.set_page_config(
        page_title="Oh My Chatty",
        page_icon="🔴",
    )
    st.title("Oh My Chatty")
    with open(HERE / 'style.css') as cssf:
        insert_html(f'<style>{cssf.read()}</style>')
    with open(HERE / 'script.js') as scriptf:
        html(f'<script>{scriptf.read()}</script>')
    return AppContext()


def main():
    setup_page(config={})
    base_url = os.environ["OPENAI_API_BASE"]
    client = openai.OpenAI(
        base_url=base_url,
        api_key=os.environ["OPENAI_API_KEY"],
    )

    model_options = []
    if "localhost" in base_url:
        model_options = [
            "/app/model",
        ]
    else:
        model_options = [
            "mistralai/Mixtral-8x22B-Instruct-v0.1",
            "meta-llama/Meta-Llama-3-8B-Instruct",
        ]
    model = st.sidebar.selectbox(
        "Model",
        options=model_options,
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # A welcome message
    with st.chat_message("assistant"):
        st.markdown(f"Hi! I'm `{model}`")

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == '__main__':
    main()

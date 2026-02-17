from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
from chat_openAI import modelo, mensagens

def abrir_chat(prompt, modelo, mensagens):
    if "mensagens" in st.session_state:
        mensagens = st.session_state["mensagens"]
    else:
        st.session_state["mensagens"] = mensagens
    if prompt:
        mensagens.append(HumanMessage(prompt))
        resposta = modelo.invoke(mensagens)
        mensagens.append(resposta)
    for mensagem in mensagens:
        if mensagem.type != "system":
            with st.chat_message(mensagem.type):
                st.write(mensagem.content)

def meu_app():
    st.header("Chat com a OpenAI - Michaell Dantas", divider=True)
    st.markdown("##### Converse com o Chat GPT")
    prompt = st.chat_input("Digite a sua mensagem")
    abrir_chat(prompt, modelo, mensagens)
meu_app()

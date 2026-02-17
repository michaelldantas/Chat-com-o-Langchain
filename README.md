Chat com LangChain, usando a OpenAI.
Precisa criar um arquivo .env e colocar a chave API da openAI numa variavél chamada OPENAI_API_KEY.
Além disso, importar as seguintes bibliotecas:
  - from langchain_openai import ChatOpenAI
    from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
    from dotenv import load_dotenv
    import streamlit as st
    from chat_openAI import modelo, mensagens

    A biblioteca chat_openAI é o segundo arquivo que contem a chamada para o modelo e a configuração do tipo de agente e o que ele faz. 

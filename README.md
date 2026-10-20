# Chat com LangChain: tutor de concursos públicos

Aplicação de chat com IA feita em Python, com LangChain, a API da OpenAI e uma interface em Streamlit. O assistente foi configurado como um **professor especialista no concurso do Congresso Nacional** (Câmara dos Deputados e Senado Federal).

## O que ele faz

- Conversa pelo navegador, numa interface de chat parecida com a do ChatGPT
- Guarda o histórico da conversa durante a sessão, então dá pra fazer perguntas de continuação
- Segue um *system prompt* que define o papel do assistente:
  - domina as disciplinas do concurso (Direito Constitucional e Administrativo, Regimentos Internos da Câmara e do Senado, Processo Legislativo, AFO, Lei 8.112/90, Lei 14.133/21, LRF e outras)
  - cita o artigo de lei que fundamenta a resposta
  - resolve questões comentando alternativa por alternativa
  - aponta as pegadinhas e o perfil de cada banca (Cebraspe, FGV, FCC)
  - monta resumos em tópicos e sugere estratégias de estudo

## Tecnologias

- **Python 3.14**
- **LangChain** (`langchain-openai`): troca de mensagens com o modelo (SystemMessage, HumanMessage, AIMessage)
- **OpenAI API**
- **Streamlit**: interface de chat e estado da sessão
- **python-dotenv**: leitura da chave da API

## Como rodar

1. Instale as dependências:

   ```bash
   pip install langchain-openai streamlit python-dotenv
   ```

2. Crie um arquivo `.env` na pasta do projeto com a sua chave da OpenAI:

   ```
   OPENAI_API_KEY=sua-chave-aqui
   ```

3. Abra o chat:

   ```bash
   streamlit run chat.py
   ```

Para um teste rápido no terminal, sem interface: `python chat_openAI.py`.

## Estrutura

```
chat.py          interface em Streamlit e histórico da conversa
chat_openAI.py   modelo, system prompt do tutor e teste pelo terminal
```

Para mudar o assunto do assistente, basta trocar o texto do `SystemMessage` em `chat_openAI.py`.

---

Projeto de estudo de IA aplicada · [Michaell Dantas](https://github.com/michaelldantas)

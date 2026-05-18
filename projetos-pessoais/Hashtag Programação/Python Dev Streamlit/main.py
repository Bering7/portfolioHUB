# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuatio enviar:
    # mostrar a mensagem que o usuario enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a respota da IA na tela

# Streamlit -> apenas com Python criar o frontend e o backend
# a IA que vamos usar> OpenAI


import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="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") 
# chave que somente voce tem acesso gerado no site da openai para o chatbot saber que é voce que está utilizando o chat

st.write("# Chatbot com IA") # markdown

if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = [] 
    # st.sesstion_state # cookie no navegador do usuario para a lista de mensagem, cria um dicionario com a chave lista mensagem dentro, que armazena a lista de mensagens

texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagem"]:
    role = mensagem['role'] # role é quem mandou a mensagem
    content = mensagem['content'] # content é o conteudo da mensagem
    st.chat_message(role).write(content) # coloca a mensagem na tela
    
if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state["lista_mensagem"].append(mensagem_usuario)
    # Nome -> vai mostrar a primeira letra do nome
    # user -> icone de usuario
    # assistant -> icone do robo

    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagem"],
        model="gpt-4o"
    )
    print(resposta_ia.choices[0].message.content)
    texto_resposta_ia = "Você perguntou: " + texto_usuario

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {'role': 'assitant', 'content': resposta_ia}
    st.session_state["lista_mensagem"].append(mensagem_ia)
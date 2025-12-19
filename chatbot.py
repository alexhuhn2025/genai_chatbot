from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
# import json
# import os 

# env_path = "//ad.corp.loans2go.co.uk/dfs/Shared/Application Support/Private/Alex H/env/"
# env_file = 'environment.json'
# with open(env_path + env_file, 'r') as fp:
#     env_data = json.load(fp)

# os.environ["GROQ_API_KEY"] = env_data["groq_api_key"]
# load the env variables
load_dotenv()   # path to where .env file is located. leave blank if in same directory. do not need to run os.environ[]=...


# os.environ["GROQ_API_KEY"] = GROK_API_KEY 
# set up streamlit
# run with:
#      python -m streamlit run .\chatbot.py
# to open again after accidentally closing window, goto new browser and search in line the localURL link,
#       localhost:8501
st.set_page_config(
    page_title="˚.🎀༘⋆ Generative AI Chatbot, hmmm",
    page_icon = "⸜(｡˃ ᵕ ˂ )⸝♡", # emojhttps://emojidb.org/cute-japanese-emojis
    layout = 'centered'
)

st.title("Generative AI CHatbot, ask me a question")

# initiate chat history
# chat_history = [] # after every user interaction, streamlit re-reads the entire code again, and this varaible will get re-initiated, thus not able to keep record of chat history, need session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# session_state is a dictionary that holds the variable name chat_history as a Key, ie. The variables in this dictionary are not rendered again after user interaction -- maintains memory
# {
#     "chat_history":[]
# }

 # show the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# initialize llm
llm = ChatGroq(model = 'llama-3.3-70b-versatile',
               temperature=0.0)

# input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    st.chat_message('user').markdown(user_prompt)
    st.session_state.chat_history.append({'role':'user','content':user_prompt})

    response = llm.invoke(
        input = [{'role':'system', 'content':'You are a helpful assistant'}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({'role':'assistant','content':assistant_response})

    with st.chat_message('assistant'):
        st.markdown(assistant_response)
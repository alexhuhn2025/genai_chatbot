from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# load the env variables
load_dotenv()   

# set up streamlit
st.set_page_config(
    page_title="˚.🎀༘⋆ Generative AI Chatbot",
    page_icon = "⸜(｡˃ ᵕ ˂ )⸝♡",
    layout = 'centered'
)

st.title("Generative AI CHatbot L2G, ask me a question, any question, like what is better to read, dostoyevsky or tolstoy?")

# initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

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





import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv
from llama_index.llms.gemini import Gemini
from llama_index.experimental.query_engine import PandasQueryEngine
from auth import is_logged_in, logout
from login_page import show_login_page

load_dotenv()

st.set_page_config(page_title="Dumroo.ai", page_icon="", layout="wide")

if not is_logged_in():
    show_login_page()
    st.stop()  

user = st.session_state['user']

col1, col2 = st.columns([4, 1])
with col1:
    st.title(" Student Data Query System")
    st.markdown(f"**Welcome, {user['full_name']}** | Role: `{user['role']}`")

with col2:
    st.write("") 
    if st.button(" Logout", use_container_width=True):
        logout()

st.markdown("---")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = Gemini(model="gemini-flash-latest", api_key=GEMINI_API_KEY)

def load_dataset():
    """Load student data from CSV"""
    try:
        df = pd.read_csv("student.csv")
        return df
    except FileNotFoundError:
        st.error(" student.csv not found")
        return None
    except Exception as e:  
        st.error(f"Error loading data: {e}")
        return None

def filter_data_by_scope(df, user):
  
    scope = user['scope']
    role = user['role']
    
    if scope['type'] == 'all_classes':
        st.success(f"Access Level: All Classes ({len(df)} students)")
        return df
    
   
    
    elif scope['type'] == 'class':
        filtered = df[df['class'].astype(str) == str(scope['value'])]
        st.success(f" Access Level: Class {scope['value']} ({len(filtered)} students)")
        return filtered
 
    
    else:
        st.error("Invalid scope configuration")
        return None

# Load and filter data
df = load_dataset()

if df is not None:
    filtered_df = filter_data_by_scope(df, user)
    
    if filtered_df is not None and not filtered_df.empty:
        
        st.subheader(" Your Accessible Data")
        st.dataframe(filtered_df, use_container_width=True)
        
        query_engine = PandasQueryEngine(
            df=filtered_df,
            llm=llm,
            verbose=True,
            synthesize_response=True,
            # instruction_str=instruction_str
        )
        
        
        st.markdown("---")
        st.subheader(" Ask Your Question")
        query = st.text_input(
            "",
            placeholder="Type your question here...",
            key="query"
        )
        
        if st.button(" Search", type="primary", use_container_width=True):
            if not query:
                st.warning("Please enter a question")
            else:
                with st.spinner("Loading..."):
                    try:
                        response = query_engine.query(query)
                        st.markdown("###  Answer")
                        st.success(response.response)
                    except Exception as e:
                        st.error(f"Error: {e}")

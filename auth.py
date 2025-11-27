import streamlit as sl
import json
# import hashlib

def load_user():
  try:
    with open('users.json','r') as f:
      data = json.load(f)
      return data["users"]
  except FileNotFoundError:
    sl.error('file not found')
    return 
  except Exception as e:
    sl.error(f"something went wrong {e}" )
    return

# def hash_password(password):
#   return hashlib.sha256(password.encode()).hexdigest

def authenticate_user(username,password):
  users=load_user()

  for user in users:
    if user['username'].lower()== username.lower():
      if user['password']== password:
        return True,user
      else: 
        return False,None   
  return False,None

def logout():
    for key in list(sl.session_state.keys()):
        del sl.session_state[key]
    sl.rerun()

def is_logged_in():
    return 'user' in sl.session_state and sl.session_state['user'] is not None    


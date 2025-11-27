import streamlit as st
from auth import authenticate_user

def show_login_page():
    
    st.title(" Student Data Query System")
    st.markdown("### Login")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("---")
        
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        if st.button("🔓 Login", use_container_width=True, type="primary"):
            if not username or not password:
                st.error("Please enter both username and password")
            else:
                success, user_data = authenticate_user(username, password)
                
                if success:
                    st.session_state['user'] = user_data
                    st.session_state['logged_in'] = True
                    st.success(f" Welcome {user_data['full_name']}!")
                    st.rerun()  
                else:
                    st.error("Invalid username or password")
        
        
        with st.expander(" Demo Credentials"):
            st.markdown("""
            **admin:**
         username:admin, password:admin123            
            **SuperAdmins:**
             username:superAdmin password:superadmin123
            """)

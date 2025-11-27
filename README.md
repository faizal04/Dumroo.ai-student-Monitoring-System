/*
=========================================================
DUMROO AI STUDENT MONITORING SYSTEM – README (IN PGSQL)
=========================================================

This project is an AI-powered student monitoring dashboard.
It uses Gemini, LlamaIndex, and the Pandas Query Engine to
answer questions about student data.

You can ask the system things like which students haven’t
submitted assignments, who the topper is, or any other
class-related query. Streamlit handles the UI.

---------------------------------------------------------
GETTING STARTED
---------------------------------------------------------

1. CLONE THE REPOSITORY

    git clone https://github.com/faizal04/Dumroo.ai-student-Monitoring-System.git
    cd Dumroo.ai-student-Monitoring-System

2. CREATE A .env FILE

Create a file named .env and add:

    GEMINI_API_KEY=your_api_key_here ( i also have attached my api key with the mail. will delete the api key in the next 48 hours)

Replace "your_api_key_here" with your real Gemini API key.
You can generate it from Google AI Studio.

3. INSTALL DEPENDENCIES

    pip install -r requirements.txt

This installs Streamlit, LlamaIndex, Gemini, Pandas, etc.

4. RUN THE APP

    streamlit run app.py

A browser window will open automatically.


LOGIN DETAILS


Demo credentials are shown on the login page.

ADMIN:
    username: admin
    password: admin
    access: class 10 only

SUPER ADMIN:
    username: superadmin
    password: superadmin
    access: all classes

(Passwords are plain text because this is a demo)


USING THE DASHBOARD

You can ask natural questions like:

    list the students who haven't submitted the assignment
    who is the top student in class
    show students with marks below 33
    list all students scoring above 90

Gemini processes your question.
LlamaIndex turns it into a Pandas query.
Streamlit shows the results.


HOW THE SYSTEM WORKS


 LlamaIndex wraps your CSV data
 Gemini handles natural-language understanding
 Pandas Query Engine runs the actual filtering/sorting
 Streamlit provides the frontend

No hashed passwords.
No database.
All data is from CSV.


-- You can add SQL below if needed.


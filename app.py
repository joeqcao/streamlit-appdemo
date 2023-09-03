import streamlit as st

import os
# from pdfminer.high_level import extract_text
# Assuming the necessary imports for your question answering system

CACHE_DIR = "./cache/"

# 1. Upload PDF

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

previous_qa = []

if uploaded_file:
    # 2. Parse the PDF
    with st.spinner('Extracting text from the uploaded PDF...'):
        uploaded_filename = uploaded_file.name

    st.success("Finished processing. Ask me anything about this doc!")

    
    # 3. Input queries from user
    user_query = st.text_input("Enter your question:")

    if user_query:
        # 4. Generate answer
        with st.spinner('Generating an answer...'):
            answer = "Here's the answer...."
            # Check if 'previous_qa' exists in session_state, if not, create it
            if 'previous_qa' not in st.session_state:
                st.session_state.previous_qa = []
            
            # Store this Q&A to previous_qa in session_state
            st.session_state.previous_qa.append((user_query, answer))

        # 5. Show the answer
        st.subheader("Answer:")
        st.write(answer)



    # Display previous questions and answers in the sidebar
    st.sidebar.title("Previous Questions & Answers")
    for question, answer in st.session_state.get('previous_qa', []):
        st.sidebar.markdown(f"**Q:** {question}")
        st.sidebar.markdown(f"**A:** {answer}")
        st.sidebar.markdown("---")

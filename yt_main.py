import streamlit as st
import lang_helper as lch
import textwrap

st.title("YouTube Q/A Assistant")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Enter the YouTube video URL?",
            max_chars=100
            )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=200,
            key="query"
            )
        openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            key="langchain_search_api_key_openai",
            max_chars=200,
            type="password" 
            )
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        db = lch.create_db_from_youtube_video_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=85))

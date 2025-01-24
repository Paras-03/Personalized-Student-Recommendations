import streamlit as st
import requests
import matplotlib.pyplot as plt
from plots import plot_Score, plot_Accuracy, plot_Mistake_Count, plot_Time
import warnings

warnings.filterwarnings("ignore")

def fetch_recommendations(title, score):
    url = "http://127.0.0.1:8000/recommend"
    payload = {"title": title, "score": score}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching recommendations: {e}")
        return None
    

st.set_page_config(page_title="Student Performance Analysis", layout="wide")
st.title("Student Performance Analysis / Student Persona  and Recommendations")


with st.sidebar:
    st.header("Input Parameters")
    quiz_title = st.text_input("Quiz Title", "human physiology (15)")
    quiz_score = st.number_input("Score", min_value=0, max_value=200, value=108)
    if st.button("Fetch Recommendations"):
        recommendations = fetch_recommendations(quiz_title, quiz_score)
        print(recommendations)
    else:
        recommendations = None

col1, col2 = st.columns(2)


with col1:
    st.subheader("Performance Analysis")
    st.markdown(
        "<h4 style='margin-bottom:10px;'>Score Analysis</h4>", unsafe_allow_html=True
    )
    fig1 = plot_Score()
    st.pyplot(fig1)
    st.markdown(
        "<h4 style='margin-bottom:10px;'>Accuracy Analysis</h4>", unsafe_allow_html=True
    )
    fig2 = plot_Accuracy()
    st.pyplot(fig2)
    st.markdown(
        "<h4 style='margin-bottom:10px;'>Mistake Count Analysis</h4>",
        unsafe_allow_html=True,
    )
    fig3 = plot_Mistake_Count()
    st.pyplot(fig3)
    st.markdown(
        "<h4 style='margin-bottom:10px;'>Time Analysis</h4>", unsafe_allow_html=True
    )
    fig4 = plot_Time()
    st.pyplot(fig4)
with col2:
    st.subheader("Recommendations")
    if recommendations:
        st.markdown(
            f"<p style='font-size:16px; font-weight:bold;'>For Quiz Title: {quiz_title}</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<p style='font-size:16px;'>Current Score: {quiz_score}</p>",
            unsafe_allow_html=True,
        )
        st.write("---")
        for rec in recommendations:
            st.markdown(
                f"<p style='font-size:14px;'>- {rec}</p>", unsafe_allow_html=True
            )
    else:
        st.markdown(
            "<p style='font-size:14px;'>No recommendations yet. Use the sidebar to fetch recommendations.</p>",
            unsafe_allow_html=True,
        )
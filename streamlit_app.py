import streamlit as st

st.set_page_config(layout="wide")

st.markdown("<style> body {background-color: #5e0e0e;}</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Rhythm Guard</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; text-shadow: 3px 3px 6px rgba(255, 255, 255, 0.3);'>A Smarter Beat: Real-Time Heart Monitoring with Machine Learning</h2>", unsafe_allow_html=True)

st.sidebar.markdown("<h1 style = 'font-size: 24px;'>What is the problem? </h1>", unsafe_allow_html= True)

st.sidebar.markdown("""<p style='font-size: 20px;'> Cardiovascular diseases (CVDs) are the leading cause of mortality globally, responsible for millions of deaths annually. Early and accurate monitoring of heart health can prevent severe cardiac events and improve long-term outcomes. Traditional heart monitoring devices are often expensive, bulky, and not designed for continuous use at home.</p>""", unsafe_allow_html=True)

st.sidebar.markdown("<h1 style = 'font-size: 24px;'> What does our Innovation do? </h1>", unsafe_allow_html = True)

st.sidebar.markdown("""<p style='font-size: 20px;'> Our innovation is a portable and real-time heart monitoring system that is both accessible and cost-effective. Using machine learning (LSTM-RL model), we can accurately predict heart rate variability and identify potential cardiac abnormalities. By deploying ECG leads (Lead II, V6, and aVL), we can monitor key aspects of heart function, including overall rhythm and left ventricular activity. </p>""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stButton>button {
            font-size: 70px;  
            padding: 80px 250px;  
            border-radius: 10px;  
            background-color: #a83232;  
            text-color: #ffffff
            color: white;  
            border: none;  
            cursor: pointer;  
            transition: background-color 0.3s;
            display: block; 
            margin: 0 auto;
        }
        .stButton>button:hover {
            background-color: #5e0e0e;
        }
        .stButton>button:center {
            button-align: center;
        }
    </style>
""", unsafe_allow_html=True)


if st.button("Click Here To Upload EKG Data"):
    st.write("monkey")


st.markdown("")

col1, col2, col3 = st.columns(3)
col1.markdown("<h3 style = 'font-size: 24px; text-align: center;'>Early Detection</h3>", unsafe_allow_html = True)
col2.markdown("<h3 style = 'font-size: 24px; text-align: center;'>Personalized Insights</h3>", unsafe_allow_html = True)
col3.markdown("<h3 style = 'font-size: 24px; text-align: center;'>Targeted Monitering</h3>", unsafe_allow_html = True)

col1.markdown("<h3 style = 'font-size: 20px; text-align: center;'>Real-time monitoring helps catch potential heart issues early.</h3>", unsafe_allow_html = True)
col2.markdown("<h3 style = 'font-size: 20px; text-align: center;'>Tailored feedback helps users make informed health decisions.</h3>", unsafe_allow_html = True)
col3.markdown("<h3 style = 'font-size: 20px; text-align: center;'>Focuses on the left ventricle for precise and relevant insights.</h3>", unsafe_allow_html = True)


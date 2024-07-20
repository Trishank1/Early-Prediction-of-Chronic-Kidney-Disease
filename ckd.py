import pickle
import streamlit as st
from PIL import Image

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #87affa;
        font-family: Arial, sans-serif;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the saved model
ckd_model = pickle.load(open('ckd.sav', 'rb'))

# Initialize session state for prediction result
if 'ckd_diagnosis' not in st.session_state:
    st.session_state.ckd_diagnosis = ''

# Function to reset session state
def reset_state():
    st.session_state.ckd_diagnosis = ''

# Function to make prediction
def make_prediction():
    ckd_prediction = ckd_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])
    if ckd_prediction[0] == 1:
        st.session_state.ckd_diagnosis = 'The person is having Chronic Kidney Disease'
    else:
        st.session_state.ckd_diagnosis = 'The person does not have Chronic Kidney Disease'

# Page title
st.title('Chronic Kidney Disease Prediction using ML')

# Navigation bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict CKD"])

if page == "Home":
    st.markdown("<h2>Welcome to the Chronic Kidney Disease Prediction App</h2>", unsafe_allow_html=True)
    st.markdown("This application uses a machine learning model to predict the likelihood of chronic kidney disease based on user inputs.")
    image = Image.open('ChronicKidneyDisease_share.jpg')
    st.image(image, caption='Chronic Kidney Disease Prediction', width=300)
    st.markdown("Select 'Predict CKD' from the navigation bar to start the prediction process.")
elif page == "Predict CKD":
    if st.session_state.ckd_diagnosis:
        # Display the result in big text
        st.markdown(f"<h1 style='text-align: center; color: red;'>{st.session_state.ckd_diagnosis}</h1>", unsafe_allow_html=True)
        st.button("Back", on_click=reset_state)
    else:
        # Page layout
        st.markdown('### Please enter the following details:')
    
        # Input fields
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            age = st.number_input('Age', min_value=0.0, max_value=200.0)
    
        with col2:
            bp = st.number_input('Blood Pressure', min_value=0.0, max_value=200.0)
    
        with col3:
            sg = st.number_input('Specific Gravity', min_value=0.0, max_value=200.0)
    
        with col4:
            al = st.number_input('Albumin', min_value=0.0, max_value=200.0)
    
        with col5:
            su = st.number_input('Sugar', min_value=0.0, max_value=200.0)
    
        with col1:
            rbc = st.selectbox('Red Blood Cells', options=['normal', 'abnormal'])
    
        with col2:
            pc = st.selectbox('Pus Cells', options=['normal', 'abnormal'])
    
        with col3:
            pcc = st.selectbox('Pus Cell Clumps', options=['present', 'notpresent'])
    
        with col4:
            ba = st.selectbox('Bacteria', options=['present', 'notpresent'])
    
        with col5:
            bgr = st.number_input('Blood Glucose Random', min_value=0.0, max_value=200.0)
    
        with col1:
            bu = st.number_input('Blood Urea', min_value=0.0, max_value=200.0)
    
        with col2:
            sc = st.number_input('Serum Creatinine', min_value=0.0, max_value=200.0)
    
        with col3:
            sod = st.number_input('Sodium', min_value=0.0, max_value=200.0)
    
        with col4:
            pot = st.number_input('Potassium', min_value=0.0, max_value=200.0)
    
        with col5:
            hemo = st.number_input('Hemoglobin', min_value=0.0, max_value=200.0)
    
        with col1:
            pcv = st.number_input('Packed Cell Volume', min_value=0.0, max_value=200.0)
    
        with col2:
            wc = st.number_input('White Blood Cell Count', min_value=0.0, max_value=10000.0)
    
        with col3:
            rc = st.number_input('Red Blood Cell Count', min_value=0.0, max_value=200.0)
    
        with col4:
            htn = st.selectbox('Hypertension', options=['yes', 'no'])
    
        with col5:
            dm = st.selectbox('Diabetes Mellitus', options=['yes', 'no'])
    
        with col1:
            cad = st.selectbox('Coronary Artery Disease', options=['yes', 'no'])
    
        with col2:
            appet = st.selectbox('Appetite', options=['good', 'poor'])
    
        with col3:
            pe = st.selectbox('Pedal Edema', options=['yes', 'no'])
    
        with col4:
            ane = st.selectbox('Anemia', options=['yes', 'no'])
    
        # Convert categorical inputs to numerical format if needed
        rbc = 1 if rbc == 'abnormal' else 0
        pc = 1 if pc == 'abnormal' else 0
        pcc = 1 if pcc == 'present' else 0
        ba = 1 if ba == 'present' else 0
        htn = 1 if htn == 'yes' else 0
        dm = 1 if dm == 'yes' else 0
        cad = 1 if cad == 'yes' else 0
        appet = 1 if appet == 'poor' else 0
        pe = 1 if pe == 'yes' else 0
        ane = 1 if ane == 'yes' else 0
    
        # Creating a button for Prediction
        if st.button('Chronic Kidney Disease result'):
            make_prediction()

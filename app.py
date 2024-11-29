import pandas as pd
import streamlit as st
import joblib

# Load the trained KNN model
model = joblib.load('cancer_model.pkl')

# Feature list from the training data (ensure this matches the training data columns exactly)
all_features = [
    'tissue_source_site', 'icd_o_3_site', 'icd_o_3_histology', 'icd_10', 'tissue_prospective_collection_indicator',
    'tissue_retrospective_collection_indicator', 'gender', 'height', 'weight', 'race_list', 'other_dx', 
    'vital_status', 'tobacco_smoking_history', 'alcohol_history_documented', 'reflux_history', 'initial_diagnosis_by', 
    'barretts_esophagus', 'history_of_esophageal_cancer', 'has_new_tumor_events_information', 'day_of_form_completion', 
    'month_of_form_completion', 'year_of_form_completion', 'has_follow_ups_information', 'has_drugs_information', 
    'has_radiations_information', 'stage_event_system_version', 'stage_event_pathologic_stage', 'stage_event_tnm_categories',
    'primary_pathology_esophageal_tumor_cental_location', 'primary_pathology_esophageal_tumor_involvement_sites',
    'primary_pathology_histological_type', 'primary_pathology_neoplasm_histologic_grade', 
    'primary_pathology_age_at_initial_pathologic_diagnosis', 'primary_pathology_initial_pathologic_diagnosis_method',
    'primary_pathology_lymph_node_metastasis_radiographic_evidence', 'primary_pathology_primary_lymph_node_presentation_assessment', 
    'primary_pathology_lymph_node_examined_count', 'primary_pathology_number_of_lymphnodes_positive_by_he',
    'primary_pathology_residual_tumor', 'primary_pathology_radiation_therapy', 'primary_pathology_postoperative_rx_tx', 'Age'
]

# Streamlit UI for user inputs
st.title('Cancer Prediction')

# Define your input fields (these are examples, you need to adjust accordingly)
age = st.number_input('Enter Age', min_value=1, max_value=120, step=1)
gender = st.selectbox('Select Gender', options=['Male', 'Female'])
gender = 1 if gender == 'Male' else 0  # Map gender to numerical value
height = st.number_input('Enter Height', min_value=50, max_value=250, step=1)
weight = st.number_input('Enter Weight', min_value=30, max_value=200, step=1)
tobacco_smoking_history = st.selectbox('Tobacco Smoking History (1=Yes, 0=No)', options=[0, 1])
alcohol_history_documented = st.selectbox('Alcohol History (1=Yes, 0=No)', options=[0, 1])

# Default values for the missing features that you may not collect via the UI
# You should fill in these values with whatever defaults you prefer or based on other inputs
input_data = {
    'tissue_source_site': 0,  # Example default value
    'icd_o_3_site': 0,  # Example default value
    'icd_o_3_histology': 0,  # Example default value
    'icd_10': 0,  # Example default value
    'tissue_prospective_collection_indicator': 0,  # Example default value
    'tissue_retrospective_collection_indicator': 0,  # Example default value
    'gender': gender,
    'height': height,
    'weight': weight,
    'race_list': 0,  # Example default value
    'other_dx': 0,  # Example default value
    'vital_status': 0,  # Example default value
    'tobacco_smoking_history': tobacco_smoking_history,
    'alcohol_history_documented': alcohol_history_documented,
    'reflux_history': 0,  # Example default value
    'initial_diagnosis_by': 0,  # Example default value
    'barretts_esophagus': 0,  # Example default value
    'history_of_esophageal_cancer': 0,  # Example default value
    'has_new_tumor_events_information': 0,  # Example default value
    'day_of_form_completion': 0,  # Example default value
    'month_of_form_completion': 0,  # Example default value
    'year_of_form_completion': 0,  # Example default value
    'has_follow_ups_information': 0,  # Example default value
    'has_drugs_information': 0,  # Example default value
    'has_radiations_information': 0,  # Example default value
    'stage_event_system_version': 0,  # Example default value
    'stage_event_pathologic_stage': 0,  # Example default value
    'stage_event_tnm_categories': 0,  # Example default value
    'primary_pathology_esophageal_tumor_cental_location': 0,  # Example default value
    'primary_pathology_esophageal_tumor_involvement_sites': 0,  # Example default value
    'primary_pathology_histological_type': 0,  # Example default value
    'primary_pathology_neoplasm_histologic_grade': 0,  # Example default value
    'primary_pathology_age_at_initial_pathologic_diagnosis': 0,  # Example default value
    'primary_pathology_initial_pathologic_diagnosis_method': 0,  # Example default value
    'primary_pathology_lymph_node_metastasis_radiographic_evidence': 0,  # Example default value
    'primary_pathology_primary_lymph_node_presentation_assessment': 0,  # Example default value
    'primary_pathology_lymph_node_examined_count': 0,  # Example default value
    'primary_pathology_number_of_lymphnodes_positive_by_he': 0,  # Example default value
    'primary_pathology_residual_tumor': 0,  # Example default value
    'primary_pathology_radiation_therapy': 0,  # Example default value
    'primary_pathology_postoperative_rx_tx': 0,  # Example default value
    'Age': age
}

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Ensure the DataFrame columns match the feature order in the model
input_df = input_df[all_features]

# Make prediction when the button is pressed
if st.button('Predict'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        st.write("Prediction: Cancer")
    else:
        st.write("Prediction: No Cancer")

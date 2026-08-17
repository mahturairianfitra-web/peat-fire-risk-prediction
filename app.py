import streamlit as st

st.set_page_config(
    page_title="Peat Fire Risk Prediction",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 Peat Fire Risk Prediction System")

st.write(
    """
    Web-based decision support system for peat fire risk assessment.
    """
)

st.info(
    "Prototype application. The validated prediction model will be integrated in the next development stage."
)

st.subheader("Environmental Input Parameters")

col1, col2 = st.columns(2)

with col1:
    vpd = st.number_input(
        "Vapor Pressure Deficit - VPD (kPa)",
        min_value=0.0,
        value=0.80,
        step=0.01
    )

    rainfall = st.number_input(
        "Rainfall Anomaly",
        value=0.0,
        step=0.1
    )

with col2:
    vh_heterogeneity = st.number_input(
        "VH Spatial Heterogeneity",
        value=0.0,
        step=0.01
    )

    vh_vv = st.number_input(
        "VH/VV Polarization Ratio (dB)",
        value=-6.20,
        step=0.01
    )

st.divider()

if st.button("Predict Fire Risk"):
    st.warning(
        "Prediction model has not yet been connected. "
        "The trained model will be integrated in the next step."
    )

st.caption(
    "Peat Fire Risk Prediction and Decision Support System"
)

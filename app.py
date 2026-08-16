import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("models/churn_model.pkl")


model = load_model()


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 700;
    }

    .sub-title {
        font-size: 16px;
        color: #B0B0B0;
    }

    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Predict whether a customer is likely to churn based on their '
    'demographic, service, contract and billing information.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.header("Customer Information")

col1, col2, col3 = st.columns(3)


# ---------------- COLUMN 1 ----------------

with col1:

    city = st.text_input(
        "City",
        value="Los Angeles"
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


# ---------------- COLUMN 2 ----------------

with col2:

    tenure_months = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=100,
        value=12,
        step=1
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )


# ---------------- COLUMN 3 ----------------

with col3:

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


# ============================================================
# CONTRACT & BILLING INFORMATION
# ============================================================

st.divider()

st.header("Contract & Billing Information")

col1, col2, col3 = st.columns(3)


# ---------------- COLUMN 1 ----------------

with col1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )


# ---------------- COLUMN 2 ----------------

with col2:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

    monthly_charges = st.number_input(
        "Monthly Charges ($)",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )


# ---------------- COLUMN 3 ----------------

with col3:

    total_charges = st.number_input(
        "Total Charges ($)",
        min_value=0.0,
        max_value=10000.0,
        value=1000.0,
        step=10.0
    )

    cltv = st.number_input(
        "CLTV",
        min_value=0,
        max_value=10000,
        value=4000,
        step=100
    )


# ============================================================
# PREDICTION
# ============================================================

st.divider()

predict_button = st.button(
    "Predict Churn",
    type="primary",
    use_container_width=True
)


if predict_button:

    # --------------------------------------------------------
    # CREATE INPUT DATAFRAME
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        {
            "City": [city],
            "Gender": [gender],
            "Senior Citizen": [senior_citizen],
            "Partner": [partner],
            "Dependents": [dependents],
            "Tenure Months": [tenure_months],
            "Phone Service": [phone_service],
            "Multiple Lines": [multiple_lines],
            "Internet Service": [internet_service],
            "Online Security": [online_security],
            "Online Backup": [online_backup],
            "Device Protection": [device_protection],
            "Tech Support": [tech_support],
            "Streaming TV": [streaming_tv],
            "Streaming Movies": [streaming_movies],
            "Contract": [contract],
            "Paperless Billing": [paperless_billing],
            "Payment Method": [payment_method],
            "Monthly Charges": [monthly_charges],
            "Total Charges": [total_charges],
            "CLTV": [cltv]
        }
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]

        probability = model.predict_proba(input_data)[0][1]

        probability_percent = probability * 100


        # ====================================================
        # PREDICTION RESULT
        # ====================================================

        st.divider()

        st.subheader("Prediction Result")

        result_col1, result_col2 = st.columns([2, 1])


        # ----------------------------------------------------
        # HIGH / LOW RISK
        # ----------------------------------------------------

        with result_col1:

            if prediction == 1:

                st.error(
                    "⚠️ High Risk of Churn"
                )

            else:

                st.success(
                    "✅ Low Risk of Churn"
                )


        # ----------------------------------------------------
        # PROBABILITY
        # ----------------------------------------------------

        with result_col2:

            st.metric(
                "Churn Probability",
                f"{probability_percent:.2f}%"
            )


        # ----------------------------------------------------
        # PROGRESS BAR
        # ----------------------------------------------------

        st.progress(
            min(max(probability, 0.0), 1.0)
        )


        # ----------------------------------------------------
        # BUSINESS MESSAGE
        # ----------------------------------------------------

        if prediction == 1:

            st.warning(
                "This customer has a relatively high probability "
                "of leaving the company. Consider targeted retention "
                "offers or customer support."
            )

        else:

            st.success(
                "This customer has a relatively low probability "
                "of leaving the company. Continue regular engagement "
                "and service monitoring."
            )


        # ====================================================
        # MODEL PERFORMANCE
        # ====================================================

        st.divider()

        st.subheader("Model Performance")

        metric1, metric2, metric3, metric4, metric5 = st.columns(5)


        with metric1:
            st.metric(
                "Accuracy",
                "80.45%"
            )


        with metric2:
            st.metric(
                "Precision",
                "64.10%"
            )


        with metric3:
            st.metric(
                "Recall",
                "60.16%"
            )


        with metric4:
            st.metric(
                "F1 Score",
                "62.07%"
            )


        with metric5:
            st.metric(
                "ROC-AUC",
                "84.32%"
            )


        st.caption(
            "Model: Logistic Regression with preprocessing pipeline"
        )


        # ====================================================
        # KEY BUSINESS INSIGHTS
        # ====================================================

        st.divider()

        st.subheader("Key Business Insights")

        insights = [
            "Month-to-month customers have the highest churn risk.",
            "Customers with shorter tenure are more likely to churn.",
            "Fiber optic customers show higher churn rates.",
            "Electronic check users have the highest churn rate among payment methods.",
            "Customers without dependents show substantially higher churn.",
            "Customers without online security and technical support have higher churn rates."
        ]

        for insight in insights:

            st.write(
                "•",
                insight
            )


    except Exception as e:

        st.error(
            f"Prediction failed: {str(e)}"
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Customer Churn Analysis & Prediction | "
    "Machine Learning Project"
)
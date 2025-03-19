import streamlit as st
import pandas as pd

# Title
st.title("ReadyAPI Virtualization ROI Calculator")

# Input fields for cost factors
st.header("Enter Your Current Costs")
api_cost = st.number_input("3rd-Party API Costs ($/Year)", value=50000)
test_env_cost = st.number_input("Test Environment Maintenance ($/Year)", value=30000)
dev_delays = st.number_input("Development Delays (Lost Hours Cost)", value=40000)
rework_cost = st.number_input("Failed Deployments & Rework Costs ($/Year)", value=20000)

# Compute total cost before virtualization
total_current_cost = api_cost + test_env_cost + dev_delays + rework_cost

st.subheader(f"Total Current Cost: ${total_current_cost:,}")

# Virtualization Savings Estimation
st.header("Estimated Savings with ReadyAPI Virtualization")
savings_percent = st.slider("Estimated Cost Reduction (%)", 10, 90, 70)
savings_amount = total_current_cost * (savings_percent / 100)

# Investment cost
investment_cost = st.number_input("Investment in ReadyAPI Virtualization ($)", value=50000)

# Calculate ROI
net_benefit = savings_amount - investment_cost
roi = (net_benefit / investment_cost) * 100 if investment_cost > 0 else 0

# Display results
st.subheader(f"Estimated Savings: ${savings_amount:,}")
st.subheader(f"Net Benefit: ${net_benefit:,}")
st.subheader(f"ROI: {roi:.2f}%")

# Downloadable report
if st.button("Download ROI Report"):
    roi_data = {
        "Category": ["Total Current Cost", "Estimated Savings", "Investment Cost", "Net Benefit", "ROI (%)"],
        "Value": [total_current_cost, savings_amount, investment_cost, net_benefit, roi],
    }
    df = pd.DataFrame(roi_data)
    df.to_csv("ROI_Report.csv", index=False)
    st.download_button("Download Report", df.to_csv(index=False), "ROI_Report.csv", "text/csv")

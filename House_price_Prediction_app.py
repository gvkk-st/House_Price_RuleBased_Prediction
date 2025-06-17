import streamlit as st

st.title("🏠 Rule-Based House Price Estimator")

area = st.number_input("Enter Area (sq. ft):", min_value=100, max_value=10000, step=50)

bedrooms = st.selectbox("Select Number of Bedrooms:", [1, 2, 3, 4, 5])

location = st.selectbox("Select Location:", ["Urban", "Suburban", "Rural"])

def estimate_price(area, bedrooms, location):
    return area * 100 + bedrooms * 50000 + (100000 if location=="Urban" else 50000 if location=="Suburban" else 20000)

if st.button("Estimate Price"):
    st.success(f"Estimated Price: ₹ {estimate_price(area, bedrooms, location):,.2f}")
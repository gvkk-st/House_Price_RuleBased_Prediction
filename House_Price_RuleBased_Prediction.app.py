import streamlit as st

st.title("🏠 Rule-Based House Price Estimator")

# Area input using slider
area = st.slider("Select Area (sq. ft):", min_value=500, max_value=5000, step=100)

# Bedrooms input using slider
bedrooms = st.slider("Select Number of Bedrooms:", min_value=1, max_value=5, step=1)

# Location input using slider (mapped from integers)
location_index = st.slider("Select Location (0: Rural, 1: Suburban, 2: Urban)", min_value=0, max_value=2, step=1)
location_map = {0: "Rural", 1: "Suburban", 2: "Urban"}
location = location_map[location_index]

# Rule-based price estimation function
def estimate_price(area, bedrooms, location):
    return area * 100 + bedrooms * 50000 + (100000 if location == "Urban" else 50000 if location == "Suburban" else 20000)

# Predict button and result
if st.button("Estimate Price"):
    st.success(f"Estimated Price: ₹ {estimate_price(area, bedrooms, location):,.2f}")

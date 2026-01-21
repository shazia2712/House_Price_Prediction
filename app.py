import pickle
import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv("cleaned_df.csv")

# Load pre-trained model
with open("RF_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page setup
st.set_page_config(page_icon = "🏡", page_title = "House Price Prediction", layout = "wide")

# Sidebar
with st.sidebar:
    st.title("House Price Prediction")
    st.image("house_logo.png")

def get_encoded_loc(location):
    for loc, encoded in zip(df["location"], df["encoded_loc"]):
        if location == loc:
            return encoded

# user input : location, bhk, bath, total sqft
pred = None
with st.container(border = True):      # to create border
    c1, c2 = st.columns(2)
    with c1:
        location = st.selectbox("📍 Location : ", options = df["location"].unique())
        bhk = st.selectbox("🏠 BHK : ", options = sorted(df["bhk"].unique()))

    with c2:
        bath = st.selectbox("🚿 No. of bathrooms : ", options = sorted(df["bath"].unique()))
        sqft = st.number_input("📐 Total Sqft : ", min_value = 300)

    # Convert str loc into encoded loc
    location  = get_encoded_loc(location)
    # st.write(location, bhk, bath, sqft)     # input values

    a1, a2, a3 = st.columns([1.5,1,1])  # to move the button in middle, we increased the a1 col size

    # Prediction
    if a2.button("Predict Price"):   # if you click on the button, price will get printed 
        data = [[sqft, bath, bhk, location]]   # data as 2D      # while training what column sequence --> same sequence we should pass
        pred = model.predict(data)[0]   # predicts price
        pred = f"{pred * 100000:.2f}"
        
if pred is not None:
    st.subheader(f"Predicted Price : Rs. {pred}")
    
# to print this price outside the container we have took pred = None,
# and put this if outside the container code
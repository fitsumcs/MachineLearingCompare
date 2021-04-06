import streamlit as st 

st.title("Streamlit Based App")
st.write(""" 

   This is a Project the allow you to compare Maching learing algorthims !!!


""")

# data set selection 

dataset_choice =  st.sidebar.selectbox("Dataset Selection", ("Breast Cancer", "Wine Dataset", "Iris"))

st.write(dataset_choice)



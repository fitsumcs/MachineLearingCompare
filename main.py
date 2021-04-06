import streamlit as st 
from sklearn import datasets

st.title("Streamlit Based App")
st.write(""" 

   This is a Project the allow you to compare Maching learing algorthims !!!


""")

# data set selection 

dataset_choice =  st.sidebar.selectbox("Dataset Selection", ("Breast Cancer", "Wine Dataset", "Iris"))
algorithm_choice =  st.sidebar.selectbox("Algorithm Selection", ("SVM", "KNN", "RF"))

st.write(dataset_choice)
st.write(algorithm_choice)



def get_data(dataset_choice):
    if dataset_choice == "Dataset Selection":
        data = datasets.load_wine()
    elif dataset_choice == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_iris()



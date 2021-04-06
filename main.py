import streamlit as st 
from sklearn import datasets
import numpy as np

st.title("Streamlit Based App")
st.write(""" 

   This is a Project the allow you to compare Machine learing algorthims !!!


""")

# data set selection 

dataset_choice =  st.sidebar.selectbox("Dataset Selection", ("Breast Cancer", "Wine Dataset", "Iris"))
algorithm_choice =  st.sidebar.selectbox("Algorithm Selection", ("SVM", "KNN", "RF"))



def get_data(dataset_choice):
    if dataset_choice == "Dataset Selection":
        data = datasets.load_wine()
    elif dataset_choice == "Breast Cancer":
        data = datasets.load_breast_cancer()
    else:
        data = datasets.load_iris()
    X = data.data
    y = data.target
    return X,y

# Display the info about the data 
X,y = get_data(dataset_choice)
st.write("Shape : " , X.shape)
st.write("Numbers of Class : " , len(np.unique(y)))


# Add Parameter Configuration 
def parmConfgurationUI(algorithmChoice):
    parameters = dict()
    if algorithmChoice == "KNN":
        K = st.sidebar.slider("K: Number of Nearest Neighbor",1 , 20 )
        parameters["K"] = K
    if algorithmChoice == "SVM":
        C= st.sidebar.slider("C: Regularization Parameter",.01, 10.0 )
        parameters["C"] = C

parmConfgurationUI(algorithm_choice)





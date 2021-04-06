import streamlit as st 
from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 


st.title("Streamlit Based App")
st.subheader(""" 

   This is an Application that allow you to compare Machine learing algorthims !!!


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
def parmConfigurationUI(algorithmChoice):
    parameters = dict()
    if algorithmChoice == "KNN":
        K = st.sidebar.slider("K: Number of Nearest Neighbor",1 , 20 )
        parameters["K"] = K
    if algorithmChoice == "SVM":
        C= st.sidebar.slider("C: Regularization Parameter",.01, 10.0 )
        parameters["C"] = C
    else:
        maximumDepth = st.sidebar.slider("Maximum Depth of Each Tree ",2, 17 )
        treeSize = st.sidebar.slider("Number of Estimators ",1, 100 )
        parameters["maximumDepth"] = maximumDepth
        parameters["treeSize"] = treeSize 
    return parameters

param =  parmConfigurationUI(algorithm_choice)

# Working on each algorithm 
def get_algorithm(algorithmChoice, params):
    if algorithmChoice == "KNN":
        classifier = KNeighborsClassifier(n_neighbors=params["K"])
    if algorithmChoice == "SVM":
        classifier = SVC(C=params["C"])
    else:
        classifier =RandomForestClassifier(n_estimators=params["treeSize"], max_depth=params["maximumDepth"], random_state=1234)
    return classifier

clf = get_algorithm(algorithm_choice, param)

# Performing the classification 
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state=1234)  #20% is used for testing 
clf.fit(X_train,y_train)
y_predict = clf.predict(X_test)
accuracy = accuracy_score(y_test,y_predict)
st.write("Algorithm : " , algorithm_choice)
st.write("Accuracy: " , accuracy)

#plot the data set , making with 2D via PCA 
pca = PCA(2)
x_projected = pca.fit_transform(X)

x1 = x_projected[0:,0]
x2 = x_projected[0:,1]

figure = plt.figure()
plt.scatter(x1,x2,c=y,alpha=0.8,cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
st.pyplot(figure)












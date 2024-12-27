import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Title and description
st.title("Data Analysis and Machine Learning App")
st.write("This web app allows users to upload a dataset, perform basic analysis, and apply machine learning models.")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    # Load the data
    data = pd.read_csv(uploaded_file)
    st.write("### Preview of the Dataset")
    st.dataframe(data.head())

    # Show basic statistics
    st.write("### Dataset Statistics")
    st.write(data.describe())

    # Select features and target
    st.write("### Select Features and Target")
    features = st.multiselect("Select features", options=data.columns)
    target = st.selectbox("Select target", options=data.columns)

    if features and target:
        X = data[features]
        y = data[target]

        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Train a model
        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Display metrics
        st.write("### Model Performance")
        st.text("Classification Report:")
        st.text(classification_report(y_test, predictions))

        # Display confusion matrix
        st.write("### Confusion Matrix")
        fig, ax = plt.subplots()
        cm = confusion_matrix(y_test, predictions)
        ax.matshow(cm, cmap="Blues", alpha=0.7)
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')
        st.pyplot(fig)

## Project 7
### Build data analysis Web app using python and streamlit
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
# title and subheader
st.title("Data Analysis")
st.subheader("Data analysis using Python and Streamlit")
#upload datasrt
upload = st.file_uploader("Please upload your data (In CSV format)")
if upload is not None:
    data= pd.read_csv(upload)
# show dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())       
# check datatype of each column
if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Datatypes")
        st.write(data.dtypes)
# find the shape of the dataset (Number of rows and number of columns)
if upload is not None:
    # if st.checkbox("Shape of the dataset"):
        # st.text("Shape of the dataset")
        # st.write(data.shape)
        # st.text("Number of rows : ")
        # st.write(data.shape[0])
        # st.text("Number of columns : ")
        # st.write(data.shape[1])
    data_shape = st.radio("What dimension do you want to check?",('Rows','Columns'))

    if data_shape == 'Rows':
        st.text("Number of rows : ")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of columns : ")
        st.write(data.shape[1])
# find null values in dataset
if upload is not None:
    value = st.checkbox("Check the null values.")
    if value == True:
        test = data.isnull().values.any() 
        if test == True:
            fig, ax = plt.subplots(figsize=(10,5))
            # fig = Yeh poora "Frame" ya "Canvas" hai.
            # ax = Yeh frame ke andar ka "Plotting Area" hai jahan asli data draw hota hai.
            if st.checkbox("Null values in the dataset"):
                sns.heatmap(data.isnull())
                st.pyplot(fig)
        else:
            st.success("Congratulations! No Null values found")             
# find duplicate values in the dataset
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This dataset contains some duplicates values.")
        dup = st.selectbox("Do you want to remove duplicates values?",("Select One","Yes","No"))
        if dup == "Yes":
            data= data.drop_duplicates()
            st.text("Duplicate values are removed.")
        if dup == "No":
            st.text("There is no duplicates.")    
# get overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset!!"):
        st.write(data.describe(include='all'))
# About section
if st.button("About App"):
    st.text("Build with streamlit.")
    st.text("Thanks to streamlit.")                    





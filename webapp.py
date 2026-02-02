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





# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Page Configuration
# st.set_page_config(page_title="Advanced Data Analyzer", layout="wide")

# st.title("📊 Data Analysis Dashboard")
# st.markdown("---")

# # Sidebar for Upload
# st.sidebar.header("Configuration")
# upload = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

# if upload is not None:
#     data = pd.read_csv(upload)
#     st.success("File Uploaded Successfully!")

#     # Tab System for better organization
#     tab1, tab2, tab3 = st.tabs(["📋 Overview", "🔍 Statistics", "📈 Visualizations"])

#     with tab1:
#         st.subheader("Data Preview")
#         rows = st.slider("Select number of rows to view", 5, 50, 5)
#         st.dataframe(data.head(rows))
        
#         st.subheader("Column Info")
#         st.write(f"**Total Rows:** {data.shape[0]} | **Total Columns:** {data.shape[1]}")
#         st.write(data.dtypes)

#     with tab2:
#         st.subheader("Statistical Summary")
#         st.write(data.describe())
        
#         if st.checkbox("Show Null Values Count"):
#             st.write(data.isnull().sum())

#     with tab3:
#         st.subheader("Visual Data Analysis")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.write("**Missing Values Heatmap**")
#             fig, ax = plt.subplots()
#             sns.heatmap(data.isnull(), cbar=False, cmap='viridis', ax=ax)
#             st.pyplot(fig)

#         with col2:
#             st.write("**Column Distribution**")
#             num_cols = data.select_dtypes(include=['number']).columns.tolist()
#             if num_cols:
#                 selected_col = st.selectbox("Select a column to visualize", num_cols)
#                 fig2, ax2 = plt.subplots()
#                 sns.histplot(data[selected_col], kde=True, ax=ax2)
#                 st.pyplot(fig2)
#             else:
#                 st.info("No numerical columns found for distribution plot.")

# # About Section in Sidebar
# st.sidebar.markdown("---")
# if st.sidebar.button("About App"):
#     st.sidebar.info("Built with ❤️ using Streamlit & Python. Optimized for Render.")
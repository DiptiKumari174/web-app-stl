## Project 7
### Build data analysis Web app using python and streamlit
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Data Analysis App")

# File Uploader
upload = st.file_uploader("Upload your CSV file", type=["csv"])

if upload is not None:
    data = pd.read_csv(upload)
    
    # Checkbox to show data
    if st.checkbox("Show Dataset"):
        st.dataframe(data.head())

    # Checkbox to show null values heatmap
    if st.checkbox("Null values in the dataset"):
        fig, ax = plt.subplots(figsize=(10,5))
        sns.heatmap(data.isnull())
        st.pyplot(fig)

# About button
if st.button("About App"):
    st.text("Built with Streamlit")



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
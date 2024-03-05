import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def app():
 st.write("**:blue[OBJECTIVE:]**")
 st.write(
  "Every individual wish to have a good salary, but however the salary structure depends on various factors such as geographic location, education, experience, industry and many more. The aim is to predict whether"
  " an individual’s income will be greater than $50,000 per year based on several attributes relating to the individual.")
 st.write("**:blue[BENEFIT:]**")
 st.write(
  "To discover one’s earning potential. To find the key areas which impact your salary. Salary insights for certain Job roles.")
 st.write("**:blue[TECDHNOLOGIES USED:]**")
 st.write(
  "Technologies Used Python programming language, NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn, PyCharm, are used to build the whole model.")
 st.link_button("Go to colab", "https://colab.research.google.com/drive/1e29Dt8h40SX70PNMupemeEU8VjgazFuu?usp=sharing")
 st.link_button("dataset", "https://www.kaggle.com/datasets/uciml/adult-census-income")



 # Load data
 data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
 column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
                 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                 'hours_per_week', 'native_country', 'income']
 data = pd.read_csv(data_url, names=column_names, skipinitialspace=True)

 # Title
 st.title(':blue[Adult Census Income Visualization]')

 # Show data
 st.write(data)

 # Comparison Bar Plot
 st.subheader(':blue[Comparison with income]')

 # Select variable for comparison
 variable_to_compare = st.selectbox('Select a  variable for comparison',
                                    ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
                                     'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss',
                                     'hours_per_week', 'native_country', 'income']
                                    )

 # Pivot data to get counts by gender
 pivot_data = data.groupby([variable_to_compare, 'income']).size().unstack()

 # Plot
 fig, ax = plt.subplots(figsize=(10, 8))
 pivot_data.plot(kind='bar', ax=ax)
 plt.xlabel(variable_to_compare.capitalize())
 plt.ylabel('Count')
 plt.title('Income Distribution by {} and Gender'.format(variable_to_compare.capitalize()))
 plt.legend(title='income')
 plt.xticks(rotation=45)
 st.pyplot(fig)






































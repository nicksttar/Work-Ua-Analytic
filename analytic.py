import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def analitics(df, mode=1):
    """Function which model graph by what you need.
    Have 3 modes: 1-Responses, 2-KDE of viewers, 3-Salaries by Experience"""
    
    # Check if the dataframe has any data
    if df.empty:
        st.write('No data found in the given dataframe!')
        return
    
    # Mode 1: Responses
    if mode == 1:
        fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
        sns.countplot(data=df, x='responses', hue='Experience', palette='viridis', ax=ax)
        ax.set_title('Responses')
        st.pyplot(fig)
    
    # Mode 2: KDE of viewers
    elif mode == 2:
        fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
        sns.kdeplot(data=df,x='viewers', hue='Experience', palette='viridis', ax=ax)
        ax.set_title('KDE of viewers')
        st.pyplot(fig)
    
    # Mode 3: Salaries by Experience
    elif mode == 3:
        if df['salaries'].isnull().all():
            st.write('No salary data found in the given dataframe!')
            return
        
        fig, ax = plt.subplots(figsize=(12, 6), dpi=150)
        sns.boxplot(data=df, x='salaries', y='Experience', palette='viridis', ax=ax)
        ax.set_title('Salary from Experience')
        ax.set_xlabel('Salaries')
        ax.set_ylabel('Experience')
        ax.set_xlim(left=0)
        st.pyplot(fig)

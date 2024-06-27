#importing packages
import pandas as pd
import numpy as np
import sklearn # Package for machine learning tools
import matplotlib.pyplot as plt # package for 2D charts
import streamlit as st # package for creating web platform
import seaborn as sns # package for generating charts
from streamlit_option_menu import option_menu #package for creating pages
from sklearn.preprocessing import StandardScaler
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


st.title("Association Rules Mining")
#Global Script
dataset=pd.read_csv("/Users/nancyhayford/Documents/TrialProject1/store_data.csv", header=None)

# encoding the dataset with one hot encoder
encoding = pd.get_dummies(dataset)

def page1():
    st.write("loading data")
    st.write(dataset)
    st.write(encoding)

def page2():
    st.write("Association Rules")
    #Apply Appriori algorithm to find the frequent itemset
    frequent_itemset=apriori(encoding, min_support=0.001, use_colnames=True)
    st.write("frequent_itemset is:")
    st.write(frequent_itemset)

    #Extracting the 10 best frequent itemset
    BestFreqSet = frequent_itemiloc[0:10,0:11]

    #Visualize frequent itemsets
    stwrite("Visualization of the itemset")
    

    #Generating the Association Rules Nb THE RULES IS BASED ON THE FREQUENT ITEM SET
    rules=association_rules(frequent_itemset, metric="confidence", min_threshold=0.95)
    st.write("The generated rules are:")
    st.write(rules)

    #Extract relevant parameters
    relevant_rules=rules[["antecedents","consequents","support","confidence","lift"]]
    st.write(relevant_rules)


pages={
    'loading data': page1,
    'Assocciation rules': page2
}

st.sidebar.header("Market Basket Analysis")
dropdown=st.sidebar.selectbox("open the dropdown", list(pages.keys()))

#Display pages
pages[dropdown]()

